def addr(r, a, b, c):
    r[c] = r[a] + r[b]

def addi(r, a, b, c):
    r[c] = r[a] + b

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]

def muli(r, a, b, c):
    r[c] = r[a] * b

def banr(r, a, b, c):
    r[c] = r[a] & r[b]

def bani(r, a, b, c):
    r[c] = r[a] & b

def borr(r, a, b, c):
    r[c] = r[a] | r[b]

def bori(r, a, b, c):
    r[c] = r[a] | b

def setr(r, a, b, c):
    r[c] = r[a]

def seti(r, a, b, c):
    r[c] = a

def gtir(r, a, b, c):
    r[c] = int(a > r[b])

def gtri(r, a, b, c):
    r[c] = int(r[a] > b)

def gtrr(r, a, b, c):
    r[c] = int(r[a] > r[b])

def eqir(r, a, b, c):
    r[c] = int(a == r[b])

def eqri(r, a, b, c):
    r[c] = int(r[a] == b)

def eqrr(r, a, b, c):
    r[c] = int(r[a] == r[b])  

funcs = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
    ]

funcs_by_name = {f.__name__: f for f in funcs}