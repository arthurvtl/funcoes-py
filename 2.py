def maior (x,y):
    if x>y:
        return('{} é maior'.format(x))
    else:
        return('{} é maior'.format(y))

x = int(input('digite um valor para x: '))
y = int(input('digite um valor para y: '))
print(maior(x,y))