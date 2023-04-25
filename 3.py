def ordena (x,y):
    if x>y:
        return y,x
    else:
        return x,y

def somaNum (x,y):
    soma = 0
    for i in range(x+1,y):
        soma += i
    return soma


a = int(input('digite um valor para a: '))
b = int(input('digite um valor para b: '))
menor,maior = ordena(a,b)
print(menor,maior)

result = somaNum(menor,maior)
print(result)
print(' ')
result = somaNum(10,14)
print(result)