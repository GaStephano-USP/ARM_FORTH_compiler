#include <stdio.h>
#include <string.h>
#define LINEMAX 100
int main() {
    char fonte[100] = "fonte.fth";
    char resultado[100] = "resul.s";
    FILE* entrada;
    FILE* saida;
    entrada = fopen(fonte, "r");
    saida = fopen(resultado, "w");
    if (entrada != NULL) {
        char symbol[LINEMAX];
        while (symbol != EOF){
            fgets(symbol, LINEMAX, entrada);
            if (isNumber(symbol) == 1)
                fprintf(saida, "mov r0, #%s\n push{r0}\n", symbol);
            //else if (symbol == ":")
            //{
            //    escreve na tabela de simbolos essa label
            //}
            //
            //else if (symbol == tabela de simbolos)
            //{
            //    escreve no arquivo {bl symbol}
            //}
            else
                printf("simbolo inválido\n");
                return -1;
        };
    }
    else {
        printf("arquivo não encontrado\n");
        return -1;
    }
    return 0;
}
char isNumber(char *text)
{
    int j;
    j = strlen(text);
    while(j--)
    {
        if(text[j] >= '0' && text[j] <= '9')
            continue;

        return 0;
    }
    return 1;
}
