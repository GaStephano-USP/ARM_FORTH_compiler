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

int main() {
    FILE* entrada;
    FILE* saida;
    entrada = fopen("target.fth", "r");
    saida = fopen("target.s", "w");
    if (entrada == NULL) {
        printf("arquivo não encontrado\n");
        return -1;
    }
    char symbol[LINEMAX];
    int num = 0;
    while (fgets(symbol, LINEMAX, entrada)){
        //remove o \n
        size_t len = strlen(symbol);
        if (len > 0 && symbol[len - 1] == '\n') {
            symbol[len - 1] = '\0';
        }
        if (isNumber(symbol))
            fprintf(saida, "\tmov r0, #%s\n\tpush{r0}\n", symbol); // push number in stack
        else if (symbol[0] == 'I' && symbol[1] == 'F' && symbol[2] == '\0')
                fprintf(saida, "\tpop {r0}\n\tmov r1, #0\n\tbeq L%d\n", num); //start IF loop
        else if (symbol[0] == 'E' && symbol[1] == 'L' && symbol[2] == 'S' && symbol[3] == 'E' && symbol[4] == '\0')
            {
                fprintf(saida, "L%d:\n\tpop {r0}\n\tmov r1, #0\n\tbeq L%d\n", num, num+1);
                num++;
            }
        else if (symbol[0] == 'T' && symbol[1] == 'H' && symbol[2] == 'E' && symbol[3] == 'N' && symbol[4] == '\0')
            fprintf(saida, "L%d:\n", num++);
        else if (symbol[0] == ';')
            fprintf(saida, "\tmov pc, lr\n"); // function return
        else if (symbol[0] == ':')
        {
            memmove(symbol, symbol+2, strlen(symbol));
            fprintf(saida, "%s:\n", symbol);
        }
        else
            fprintf(saida, "\tbl %s\n", symbol); // branch to a label
        printf("%s\n", symbol);
    };
    fclose(entrada);
    fclose(saida);
    return 0;
}

