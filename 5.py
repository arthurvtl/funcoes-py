def mtp(x,y):
    result = 0
    for i in range(y):
        result = result + x
    return result

x = int(input('digite um valor para x: '))
y = int(input('digite um valor para y: '))
result = mtp(x,y)
print(result)