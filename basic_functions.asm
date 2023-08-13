@ /* funcoes iniciais q tenho q fazer: Add Sub Mul Swap Dup Drop Rot */

add:
    pop {ro, r1}
    add r0, r0, r1
    push {r0}
    mov pc, lr  

sub:
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

mul:
    pop {r0, r1}
    mul r0, r0, r1
    push {r0}
    mov pc, lr  

div:
    pop {r0, r1}
    div r0, r1, r0
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

@ /* Operacoes logicas */

>:
    pop {r0, r1}
    cmp r1, r0
    bgt greater
    mov r2, #0
    pop {r2}
    b end
    greater:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

<:
    pop {r0, r1}
    cmp r1, r0
    blt less
    mov r2, #0
    pop {r2}
    b end
    less:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

==:
    pop {r0, r1}
    cmp r1, r0
    beq equal
    mov r2, #0
    pop {r2}
    b end
    equal:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

!=:
    pop {r0, r1}
    cmp r1, r0
    bne nequal
    mov r2, #0
    pop {r2}
    b end
    equal:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

@ /* Operacoes logicas com 0 */

0=:
    pop {r0}
    comp r0, #0
    beq equal
    mov r2, #0
    pop {r1}
    b end
    equal:
        mov r2, #1
        pop {r1}
    end:
        mov pc, lr  

0<:
    pop {r0}
    cmp r0, #0
    blt less
    mov r2, #0
    pop {r2}
    b end
        less:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

0>:
    pop {r0}
    cmp r0, #0
    bgt greater
    mov r2, #0
    pop {r2}
    b end
        greater:
        mov r2, #1
        pop {r2}
    end:
        mov pc, lr  

@ /* Opoeracoes Logicas or, and, negate */

or:
    @ /* Checa se r0 ou r1 sao diferentes de 0, se for retorna 1, se nn retorna 0 */
    pop {r0, r1}
    cmp r0, #0
    beq passo1
    b escreve1
    passo1:
        cmp r1 #0
        beq zero
        b escreve1
    escreve1:
        mov r2, #1
        push {r2}
        b end
    zero:
        mov r2, #0
        push {r2}
        b end
    end:
        mov pc, lr


and:
    @ /* Checa se r0 e r1 sao maiores que 0, se for retorna 1, se nn retorna 0 */
    pop {r0, r1}
    cmp r0, #0
    beq zero
    cmp r1, #0
    beq zero
    b escreve1
    escreve 1:
        mov r2, #1
        push {r2}
        b end
    zero:
        mov r2, #0
        push {r2}
        b end
    end:
        mov pc, lr  

not:
    @ /* Escreve 0 na pilha se tinha algo diferente de 0, escreve 1 na pilha se tinha 0  */
    pop {r0}
    cmp r0, #0
    beq escreve1
    b escreve0
    b menor
    escreve0:
        mov r2, #0
        push {r2}
        b end
    escreve1:
        mov r2, #1
        push {r2}
        b end
    end:
        mov pc, lr

