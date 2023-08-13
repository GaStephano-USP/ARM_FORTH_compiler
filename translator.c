#include <stdio.h>
#include <string.h>
#define LINEMAX 100
int main(int args, char *argv[]) {
    char fonte[LINEMAX] = argv[0];
    char resultado[LINEMAX] = argv[1];
    FILE* entrada;
    FILE* saida;
    entrada = fopen(fonte, "r");
    saida = fopen(resultado, "w");
    if (entrada != NULL) {
        char symbol[LINEMAX];
        int num = 0;
        while (symbol != EOF){
            fgets(symbol, LINEMAX, entrada);
            if (isNumber(symbol) == 1)
                fprintf(saida, "\tmov r0, #%s\n\t push{r0}\n", symbol); // push number in stack
            else if (symbol == "IF");
            //    fprintf(saida, "\tbz L%d\n", num);
            else if (symbol == "ELSE");
            //    fprintf(saida, "L%d:\n\t beq L%d\n", num, ++num);
            else if (symbol == "THEN")
                fprintf(saida, "L%d:\n", num++);
            else if (symbol == ";")
                fprintf(saida, "mov pc, lr\n"); // function return
            else if (symbol[0] == ":")
            {
                memmove(symbol, symbol+2, strlen(symbol));
                fprintf("%s:\n", symbol);
            }
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
