@ /* funcoes iniciais q tenho q fazer: Add Sub Mul Swap Dup Drop Rot */

add:
    pop {ro, r1}
    add r0, r0, r1
    push {r0}
    mov pc, lr  

sub:
    pop {r0, r1}
    sub r0, r0, r1
    push {r0}
    mov pc, lr 

dup:
    pop {r0}
    push {r0}
    push {r0}

neg:
    pop {r0}
    mov r1, #0
    sub, r0, r1, r0
    push {r0}

mul:
    pop {r0, r1}
    mul r0, r0, r1
    push {r0}

rot:
    pop {r0, r1, r2}
    push {r1}
    push {r2}
    push {r0}

swap:
    pop {r0, r1}
    push {r1}
    push {r0}

drop:
    add sp, #4
    @ /* Movo stack pointer pra baixo */
