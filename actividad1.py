num1=int(input("Dame un numero "))


def nomFunc(num1):
    
    cont=1
    while cont<11:
        print("{} * {} = {}" .format(num1,cont,num1*cont))
    cont=cont+1
nomFunc(num1)