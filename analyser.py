symbols = {'+'      : 'add_routine',
           '-'      : 'sub_routine',
           '*'      : 'mul_routine',
           '/'      : '',
           '.'      : '',
           '='      : 'equal',
           '>'      : 'greater_then',
           '<'      : 'less_then',
           '<>'     : 'n_equal',
           '0='     : 'equal_zero',
           '0>'     : 'greater_then_zero',
           '0<'     : 'less_then_zero',
           'OR'     : 'or_routine',
           'AND'    : 'and_routine',
           'NEGATE' : 'negate_routine',
           'DROP'   : 'drop',
           'SWAP'   : 'swap',
           'ROT'    : 'rot',
           'DUP'    : 'dup',
           'OVER'   : 'over',
           'TUCK'   : 'tuck',
           'PICK'   : 'pick',
           'ROLL'   : 'roll',
           'IF'     : 'IF',
           'ELSE'   : 'ELSE',
           'THEN'   : 'THEN',
           'DO'     : 'DO',
           'I'      : 'i',
           'J'      : 'j',
           'K'      : 'k',
           'LOOP'   : 'LOOP',}
extensions = ['fth', 'fs', '4th', 'frt', 'forth']

from sys import argv # argumentos de linha de comando

if len(argv) > 2:
    print('AVISO: Analisador recebe apenas um argumento.')
elif len(argv) < 2:
    print('ERRO: Analisador precisa do nome do arquivo.')
    exit(-1)

sourceFilename = argv[1]
sourceWords = sourceFilename.rsplit('.', 1)
if len(sourceWords) < 2 or not (sourceWords[1] in extensions) :
    print('ERRO: Nome inválido de arquivo de origem. Certifique-se de que ele possui uma extensão válida, como \".fth\".')
    exit(-1)
outputFilename = sourceWords[0] + '.bck'

source = open(sourceFilename, 'r')
output = open(outputFilename, 'w')

statestack = ['n'] # para manter controle das mudanças de estado; statestack[-1] é o estado atual
                   # 'n' (normal), 'w' (word - entre : e ;), 'c' (comentário), 'lc' (comentário de linha), 'l' (loop), 'i' (condicional)

def close():
    source.close()
    output.close()
    return

def isSigned(string) :
    if len(string) == 0 :
        return False
    if string[0] == '-' :
        return string[1:].isnumeric()
    return string.isnumeric()
    

lineNum = 0
for line in source :
    lineNum += 1
    args = line.split()
    i = 0
    while i < len(args) :
        
        # Estado: comentário multilinha
        if statestack[-1] == 'c' and args[i] == ')' :
            statestack.pop()
        
        # Estado: normal 
        elif statestack[-1] == 'n' :
            if args[i] == ':' :
                statestack.append('w')
                if args[i+1].isnumeric() :
                    print(f"ERRO: Nome inválido (linha {lineNum})")
                    close()
                    exit(-1)
                elif args[i+1].upper() in symbols.keys():
                    print(f"ERRO: Nome \"{args[i+1]}\" já tem definição (linha {lineNum})")
                    close()
                    exit(-1)
                else :
                    symbols[args[i+1]] = args[i+1].upper()
                    output.write(": " + args[i+1].upper() + '\n')
                    i += 1
            elif args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'IF' :
                output.write('IF\n')
                statestack.append('i')
            elif args[i].upper() == 'DO' :
                output.write('DO\n')
                statestack.append('l')
            elif args[i].upper() in [';', ')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif isSigned(args[i]) :
                output.write(args[i] + '\n')
            elif args[i].upper() in symbols.keys() :
                output.write(symbols[args[i]] + '\n')
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: word
        elif statestack[-1] == 'w' :
            if args[i] == ';' :
                output.write(';\n')
                statestack.pop()
            elif args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'IF' :
                output.write('IF\n')
                statestack.append('i')
            elif args[i].upper() == 'DO' :
                output.write('DO\n')
                statestack.append('l')
            elif args[i].upper() in [')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif args[i] == ':' :
                print(f"ERRO: Nome não pode ser definido dentro da definição de outro (linha {lineNum})")
                close()
                exit(-1)
            elif isSigned(args[i]) :
                output.write(args[i] + '\n')
            elif args[i].upper() in symbols.keys() :
                output.write(symbols[args[i]] + '\n')
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: loop
        elif statestack[-1] == 'l' :
            if args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'LOOP' :
                output.write('LOOP\n')
                statestack.pop()
            elif args[i].upper() == 'IF' :
                if statestack[-2] != 'l' :
                    output.write('IF\n')
                    statestack.append('i')
                else:
                    print(f"ERRO: Tentativa de aninhamento (linha {lineNum})")
                    close()
                    exit(-1)
            elif args[i].upper() == 'DO' :
                print(f"ERRO: Tentativa de aninhamento (linha {lineNum})")
                close()
                exit(-1)
            elif args[i] == ':' :
                print(f"ERRO: Nome não pode ser definido dentro da definição de outro (linha {lineNum})")
                close()
                exit(-1)
            elif args[i].upper() in [';', ')', 'THEN', 'ELSE'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif isSigned(args[i]) :
                output.write(args[i] + '\n')
            elif args[i].upper() in symbols.keys() :
                output.write(symbols[args[i]] + '\n')
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: condicional
        elif statestack[-1] == 'i' :
            if args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'THEN' :
                output.write('THEN\n')
                statestack.pop()
            elif args[i].upper() == 'DO' :
                if statestack[-2] != 'i' :
                    output.write('DO\n')
                    statestack.append('l')
                else:
                    print(f"ERRO: Tentativa de aninhamento (linha {lineNum})")
                    close()
                    exit(-1)
            elif args[i].upper() == 'DO' :
                print(f"ERRO: Tentativa de aninhamento (linha {lineNum})")
                close()
                exit(-1)
            elif args[i] == ':' :
                print(f"ERRO: Nome não pode ser definido dentro da definição de outro (linha {lineNum})")
                close()
                exit(-1)
            elif args[i].upper() in [';', ')', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif isSigned(args[i]) :
                output.write(args[i] + '\n')
            elif args[i].upper() in symbols.keys() :
                output.write(symbols[args[i]] + '\n')
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        i += 1
    
    # Sai de comentário de linha ao final dela
    if statestack[-1] == 'lc' :
        statestack.pop()

if statestack[-1] == 'l':
    print('ERRO: Há um \'LOOP\' faltando.')
elif statestack[-1] == 'i':
    print('ERRO: Há um \'THEN\' faltando.')

print(f'Programa analisado com sucesso!\nSaída salva em {outputFilename}')
close()
