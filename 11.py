def fatorial (n):
    n_fat = 1
    for i in range(n,1,-1):
        n_fat=n_fat*i
    return n_fat

def combinacao (n,p,np):
    combinacao = resultn / (resultp*resultnp)
    return combinacao

n = int(input('digite um valor para n: '))
p = int(input('digite um valor para p: '))
np = n-p
resultn = fatorial(n)
resultp = fatorial(p)
resultnp = fatorial(np)
resposta = combinacao(n, p, np)
print(resposta)
print(resultnp)