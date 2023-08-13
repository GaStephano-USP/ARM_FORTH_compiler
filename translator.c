#include <stdio.h>
#include <string.h>
#define LINEMAX 100
int main() {
    char fonte[LINEMAX] = "fonte.fth";
    char resultado[LINEMAX] = "resul.s";
    FILE* entrada;
    FILE* saida;
    entrada = fopen(fonte, "r");
    saida = fopen(resultado, "w");
    if (entrada != NULL) {
        char symbol[LINEMAX];
        while (symbol != EOF){
            fgets(symbol, LINEMAX, entrada);
            if (isNumber(symbol) == 1)
                fprintf(saida, "mov r0, #%s\n push{r0}\n", symbol); // push number in stack
            else if (symbol == ";")
                fprintf(saida, "mov pc, lr\n"); // function return
            else
                fprintf(saida, "bl %s\n", symbol); // branch to a label
        };
    }
    else {
        printf("arquivo não encontrado\n");
        return -1;
    }
    fclose(entrada);
    fclose(saida);
    return 0;
}

//checa se a string só contém números
int isNumber(char *text)
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
