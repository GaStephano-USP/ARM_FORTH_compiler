# Compilador de FORTH em ARM
O projeto é composto por um programa que implementa um analisador léxico e sintático, um programa que gera o código e um programa que implementa as funções básicas da linguagem e eles podem ser utilizados separadamente, porém o intuito é executá-los em sequência
## Configurações
Para o fluxo de execução são utilizados módulos do GNU em ARM, então é necessário ter esses módulos instalados, além disso é necessário o gcc e um interpretador de python
```
sudo apt install binutils-arm-none-eabi gcc-arm-none-eabi
sudo apt install gdb-multiarch openocd make
```
## Instruções de execução
### Analisador
Para o analisador é necessário python
```
python analyser.py <nome do arquivo de entrada>
```
### Gerador de código
Primeiramente é necessário compilar o gerador de código com o gcc
```
gcc -o <nome do executável> translator.c 
```
Depois executamos ele (o arquivo fonte deve estar fora da pasta
```
./ARM_FORTH_compiler/translator
```
### Linker e funções básicas
Compilando o basic_functions e target
```
arm-none-eabi-gcc -c basic_functions.s
arm-none-eabi-gcc -c target.s
```
Isso gera os arquivos basic_functions.o e target.o
Com isso podemos juntar com o mapa de memória e o linker
```
arm-none-eabi-ld target.o basic_function.o -T kernel.ld -o target.elf
```
Se quiser conferir o resultado você pode usar o 
```
arm-none-eabi-objdump target.elf
```
Para gerar o assembler do resultado
