#include <stdio.h>
#include <string.h>
#define LINEMAX 100

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

int main(int args, char *argv[]) {
    FILE* entrada;
    FILE* saida;
    entrada = fopen(argv[0], "r");
    saida = fopen(argv[1], "w");
    if (entrada == NULL) {
        printf("arquivo não encontrado\n");
        return -1;
    }
    char symbol[LINEMAX];
    int num = 0;
    printf( "%s", symbol);
    while (fgets(symbol, LINEMAX, entrada)){
        //remove o \n
        size_t len = strlen(symbol);
        if (len > 0 && symbol[len - 1] == '\n') {
            symbol[len - 1] = '\0';
        }
        if (isNumber(symbol))
            fprintf(saida, "\tmov r0, #%s\n\tpush{r0}\n", symbol); // push number in stack
        else if (symbol == "IF")
                fprintf(saida, "\tpop {r0}\n\tbz L%d", num);
        else if (symbol == "ELSE");
            //    fprintf(saida, "L%d:\n\t beq L%d\n", num, ++num);
        else if (symbol == "THEN")
            fprintf(saida, "L%d:\n", num++);
        else if (symbol == ";")
            fprintf(saida, "mov pc, lr"); // function return
        else if (symbol == "a")
        {
            memmove(symbol, symbol+2, strlen(symbol));
            fprintf(saida, "%s:", symbol);
        }
        else
            fprintf(saida, "\tbl %s\n", symbol); // branch to a label
        printf("%s", symbol);
    };
    fclose(entrada);
    fclose(saida);
    return 0;
}

