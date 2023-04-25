def verificaPrimo (x):
    cont = 0
    for i in range(1,x+1):
        if x%i == 0:
            cont += 1
    return cont

def tf (cont):
    if cont <= 2:
        return True
    else:
        return False

x = int(input('digite um valor para x: '))
cont = verificaPrimo(x)
resposta = tf(cont)
print(resposta)
