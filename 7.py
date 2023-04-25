def elevado(x,y):
    result = 1
    for i in range(y):
        result = result * x
    return result

x = int(input('digite um valor para x: '))
y = int(input('digite um valor para y: '))
result = elevado(x,y)
print(result)