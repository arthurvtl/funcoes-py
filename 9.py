def fatorial (k):
    k_fat = 1
    for i in range(k,1,-1):
        k_fat=k_fat*i
    return k_fat

k = int(input('digite um valor para k: '))
result = fatorial(k)
print(result)