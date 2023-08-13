symbols = ['+', '-', '*', '/', '.', '=', '>', '<', '<>', '0=', '0>', '0<',
           'DROP', 'SWAP', 'ROT', 'DUP', 'OVER', 'TUCK', 'PICK', 'ROLL',
           'IF', 'ELSE', 'THEN', 'DO', 'LOOP']
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

lineNum = 0
for line in source :
    lineNum += 1
    args = line.split()
    for i in range(len(args)) :
        
        # Estado: comentário multilinha
        if statestack[-1] == 'c' and args[i] == ')' :
            statestack.pop()
        
        # Estado: normal 
        elif statestack[-1] == 'n' :
            if args[i] == ':' :
                statestack.append['w']
                if args[i+1].isnumeric() :
                    print(f"ERRO: Nome inválido (linha {lineNum})")
                    close()
                    exit(-1)
                elif args[i+1].upper() in symbols:
                    print(f"ERRO: Nome \"{args[i+1]}\" já tem definição (linha {lineNum})")
                    close()
                    exit(-1)
                else :
                    symbols.append(args[i+1].upper())
                    output.write(": " + args[i+1].upper())
                    i += 1
            elif args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'IF' :
                statestack.append('i')
            elif args[i].upper() == 'DO' :
                statestack.append('l')
            elif args[i].upper() in [';', ')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif (args[i].upper() in symbols) or (args[i].isnumeric()) :
                output.write(args[i].upper())
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: word
        elif statestack[-1] == 'w' :
            if args[i] == ';' :
                statestack.pop()
            elif args[i] == '\\' :
                statestack.append('lc')
            elif args[i] == '(' :
                statestack.append('c')
            elif args[i].upper() == 'IF' :
                statestack.append('i')
            elif args[i].upper() == 'DO' :
                statestack.append('l')
            elif args[i].upper() in [')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif args[i] == ':' :
                print(f"ERRO: Nome não pode ser definido dentro da definição de outro (linha {lineNum})")
                close()
                exit(-1)
            elif (args[i].upper() in symbols) or (args[i].isnumeric()) :
                output.write(args[i].upper())
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: loop
        elif statestack[-1] == 'l' :
            if args[i] == '\\' :
                output.write('\\')
                statestack.append('lc')
            elif args[i] == '(' :
                output.write('(')
                statestack.append('c')
            elif args[i].upper() == 'IF' :
                if statestack[-2] != 'l' :
                    output.write('IF')
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
            elif args[i].upper() in [';', ')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif (args[i].upper() in symbols) or (args[i].isnumeric()) :
                output.write(args[i].upper())
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
        
        # Estado: condicional
        elif statestack[-1] == 'l' :
            if args[i] == '\\' :
                output.write('\\')
                statestack.append('lc')
            elif args[i] == '(' :
                output.write('(')
                statestack.append('c')
            elif args[i].upper() == 'DO' :
                if statestack[-2] != 'i' :
                    output.write('DO')
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
            elif args[i].upper() in [';', ')', 'THEN', 'ELSE', 'LOOP'] :
                print(f"ERRO: Termo \"{args[i]}\" inesperado (linha {lineNum})")
                close()
                exit(-1)
            elif (args[i].upper() in symbols) or (args[i].isnumeric()) :
                output.write(args[i].upper())
            else:
                print(f"ERRO: Termo \"{args[i]}\" desconhecido (linha {lineNum})")
                close()
                exit(-1)
    
    # Sai de comentário de linha ao final dela
    if statestack[-1] == 'lc' :
        statestack.pop()

close()
