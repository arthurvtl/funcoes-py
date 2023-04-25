def elevado(x,y):
    z = 0
    z = x**y
    return z

x = int(input('digite um valor para x: '))
y = int(input('digite um valor para y: '))

result = elevado(x,y)
print(result)