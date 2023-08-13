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
