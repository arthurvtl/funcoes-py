def fatorial (n):
    n_fat = 1
    for i in range(n,1,-1):
        n_fat=n_fat*i
    return n_fat

def arranjo (n,p):
    if n < p:
        return -1
    else:
        return fatorial(n)/fatorial(n-p)



n = int(input('digite um valor para n: '))
p = int(input('digite um valor para p: '))
result = fatorial(n)
# result2 = fatorial(n-p)
# result3 = result/result2
# print(result3)
result2 = arranjo(n,p)
print(result2)