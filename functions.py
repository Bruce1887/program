a = 3
b = 14

def double(n):
    return(2*n)

def triple(n):
    return(3*n)

def quadruple(n):
    return(4*n)

def funky(n, m):
    return(triple(n) + quadruple(m))

d1 = double(a)       # 6
d2 = double(b)       # 28

t1 = triple(a)       # 9
t2 = triple(b)       # 42

q1 = quadruple(a)    # 12
q2 = quadruple(b)    # 56

f1 = funky(a, b)     # 65
f2 = funky(b, b)     # 98