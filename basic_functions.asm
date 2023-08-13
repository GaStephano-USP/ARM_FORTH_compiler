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
    @ /* Movo stack pointer pra baixo */
    mov pc, lr

over:
    pop {r0, r1}
    push {r1}
    push {r0}
    push {r1}
    mov pc, lr

pick:
    pop {r0}
    mov r1, #4
    mul r0, r0, r1
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
    end
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
    end
    mov pc, lr

=:
    pop {r0, r1}
    cmp r1, r0
    beq equal
    mov r2, #0
    pop {r2}
    b end
    equal:
    mov r2, #1
    pop {r2}
    end
    mov pc, lr

<>:
    pop {r0, r1}
    cmp r1, r0
    bne nequal
    mov r2, #0
    pop {r2}
    b end
    nequal:
    mov r2, #1
    pop {r2}
    end
    mov pc, lr
