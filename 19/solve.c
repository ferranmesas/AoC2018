#include <stdio.h>
typedef enum {
    addr, 
    addi,

    mulr,
    muli,

    banr,
    bani,

    borr,
    bori,
    
    setr,
    seti,

    gtir,
    gtri,
    gtrr,

    eqir,
    eqri,
    eqrr
} operation;

typedef struct {
    operation op_id;
    int a, b, c;
} line;

int ip = 4;
line program[] = {
{addi, 4, 16, 4},
{seti, 1, 5, 1},
{seti, 1, 2, 2},
{mulr, 1, 2, 3},
{eqrr, 3, 5, 3},
{addr, 3, 4, 4},
{addi, 4, 1, 4},
{addr, 1, 0, 0},
{addi, 2, 1, 2},
{gtrr, 2, 5, 3},
{addr, 4, 3, 4},
{seti, 2, 7, 4},
{addi, 1, 1, 1},
{gtrr, 1, 5, 3},
{addr, 3, 4, 4},
{seti, 1, 9, 4},
{mulr, 4, 4, 4},
{addi, 5, 2, 5},
{mulr, 5, 5, 5},
{mulr, 4, 5, 5},
{muli, 5, 11, 5},
{addi, 3, 1, 3},
{mulr, 3, 4, 3},
{addi, 3, 18, 3},
{addr, 5, 3, 5},
{addr, 4, 0, 4},
{seti, 0, 3, 4},
{setr, 4, 2, 3},
{mulr, 3, 4, 3},
{addr, 4, 3, 3},
{mulr, 4, 3, 3},
{muli, 3, 14, 3},
{mulr, 3, 4, 3},
{addr, 5, 3, 5},
{seti, 0, 4, 0},
{seti, 0, 5, 4},
};

int program_length = sizeof(program)/sizeof(line);

void exec(int r[6]) {
    for(;;) {
        r[ip]++;
        int program_offset = r[ip];
        if (program_offset > program_length) {
            return;
        }

        line l = program[program_offset];
        switch(l.op_id) {
            case addr:
                r[l.c] = r[l.a] + r[l.b];
                break;
            case addi:
                r[l.c] = r[l.a] + l.b;
                break;
            case mulr:
                r[l.c] = r[l.a] * r[l.b];
                break;
            case muli:
                r[l.c] = r[l.a] * l.b;
                break;
            case banr:
                r[l.c] = r[l.a] & r[l.b];
                break;
            case bani:
                r[l.c] = r[l.a] & l.b;
                break;
            case borr:
                r[l.c] = r[l.a] | r[l.b];
                break;
            case bori:
                r[l.c] = r[l.a] | l.b;
                break;
            case setr:
                r[l.c] = r[l.a];
                break;
            case seti:
                r[l.c] = l.a;
                break;
            case gtir:
                r[l.c] = l.a > r[l.b];
                break;
            case gtri:
                r[l.c] = r[l.a] > l.b;
                break;
            case gtrr:
                r[l.c] = r[l.a] > r[l.b];
                break;
            case eqir:
                r[l.c] = l.a == r[l.b];
                break;
            case eqri:
                r[l.c] = r[l.a] == l.b;
                break;
            case eqrr:
                r[l.c] = r[l.a] == r[l.b];
                break;
        };
    }
};

int main(void) {
    int registers[6] = { 0, 0, 0, 0, -1, 0 };
    exec(registers);
    printf("%d\n", registers[0]);
    return 0;
}