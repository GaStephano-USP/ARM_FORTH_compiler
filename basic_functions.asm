@ /* funcoes iniciais q tenho q fazer: Add Sub Mul Swap Dup Drop Rot */

add_routine:
    pop {r0, r1}
    add r0, r0, r1
    push {r0}
    mov pc, lr  

sub_routine:
    @ /* Tem que lembrar que forth é polonesa reversa, logo sub: segundo da fila - primeiro da fila */
    pop {r0, r1}
    sub r0, r1, r0 
    push {r0}
    mov pc, lr 

dup:
    pop {r0}
    push {r0}
    push {r0}
    mov pc, lr  

neg:
    pop {r0}
    mov r1, #0
    sub, r0, r1, r0
    push {r0}
    mov pc, lr  

mul_routine:
    pop {r0, r1}
    mul r0, r1, r0
    push {r0}
    mov pc, lr  

div:
    pop {r0, r1}
    sdiv r0, r1, r0
    push {r0}
    mov pc, lr  

rot:
    pop {r0, r1, r2}
    push {r1}
    push {r0}
    push {r2}
    mov pc, lr  

swap:
    pop {r0, r1}
    push {r0}
    push {r1}
    mov pc, lr  

drop:
    add sp, #4
    mov pc, lr  
    @ /* Movo stack pointer pra baixo */

over:
    pop {r0, r1}
    push {r1}
    push {r0}
    push {r1}
    mov pc, lr

pick:
    pop {r0}
    mov r1, #4
    mul r0, r1, r0
    add sp, sp, r0
    ldr r1, [sp]
    sub sp, sp, r0
    push {r1}
    mov pc, lr

tuck:
    pop {r0}
    pop {r1}
    push {r0}
    push {r1}
    push {r0}
    mov pc, lr


@ /* Operacoes logicas */

greater_then:
    pop {r0, r1}
    cmp r1, r0
    bgt greater
    mov r2, #0
    pop {r2}
    b end_greater_then
    greater:
        mov r2, #1
        pop {r2}
        b end_greater_then
    end_greater_then:
        mov pc, lr  

less_then:
    pop {r0, r1}
    cmp r1, r0
    blt less
    mov r2, #0
    pop {r2}
    b end_less_then
    less:
        mov r2, #1
        pop {r2}
        b end_less_then
    end_less_then:
        mov pc, lr  

equal_rotine:
    pop {r0, r1}
    cmp r1, r0
    beq equal
    mov r2, #0
    pop {r2}
    b end_equal
    equal:
        mov r2, #1
        pop {r2}
        b end_equal
    end_equal:
        mov pc, lr  

n_equal:
    pop {r0, r1}
    cmp r1, r0
    bne nequal
    mov r2, #0
    pop {r2}
    b end_nequal
    nequal:
        mov r2, #1
        pop {r2}
        b end_nequal
    end_nequal:
        mov pc, lr  

@ /* Operacoes logicas com 0 */

equal_zero:
    pop {r0}
    cmp r0, #0
    beq equal
    mov r2, #0
    pop {r1}
    b end_equal_zero
    equal:
        mov r2, #1
        pop {r1}
        b end_equal_zero
    end_equal_zero:
        mov pc, lr  

less_then_zero:
    pop {r0}
    cmp r0, #0
    blt less_zero
    mov r2, #0
    pop {r2}
    b end_less_then_zero
        less_zero:
        mov r2, #1
        pop {r2}
        b end_less_then_zero
    end_less_then_zero:
        mov pc, lr  

greater_then_zero:
    pop {r0}
    cmp r0, #0
    bgt greater_zero
    mov r2, #0
    pop {r2}
    b end_greater_then_zero
        greater_zero:
        mov r2, #1
        pop {r2}
        b end_greater_then_zero
    end_greater_then_zero:
        mov pc, lr  

@ /* Opoeracoes Logicas or, and, negate */

or_routine:
    @ /* Checa se r0 ou r1 sao diferentes de 0, se for retorna 1, se nn retorna 0 */
    pop {r0, r1}
    cmp r0, #0
    beq passo1
    b escreve1
    passo1:
        cmp r1 #0
        beq zero_or
        b escreve1
    escreve1:
        mov r2, #1
        push {r2}
        b end_or
    zero_or:
        mov r2, #0
        push {r2}
        b end_or
    end_or:
        mov pc, lr


and_routine:
    @ /* Checa se r0 e r1 sao maiores que 0, se for retorna 1, se nn retorna 0 */
    pop {r0, r1}
    cmp r0, #0
    beq zero_and
    cmp r1, #0
    beq zero_and
    b escreve1_and
    escreve1_and:
        mov r2, #1
        push {r2}
        b end_and
    zero_and:
        mov r2, #0
        push {r2}
        b end_and
    end_and:
        mov pc, lr  

negate_routine:
    @ /* Escreve 0 na pilha se tinha algo diferente de 0, escreve 1 na pilha se tinha 0  */
    pop {r0}
    cmp r0, #0
    beq escreve1_negate
    b escreve0
    b menor
    escreve0:
        mov r2, #0
        push {r2}
        b end_negative
    escreve1_negate:
        mov r2, #1
        push {r2}
        b end_negative
    end_negative:
        mov pc, lr

