 
def main():
    num2=int(input("Escoge tu primer numero "))
    num3=int(input("Escoge tu segundo numero "))
    menu="1.- Suma || 2.- Resta || 3.-Multiplicacion || 4.-Division|| 5.-Adios"
    print(menu)
    num1=int(input("Escoge una opcion "))

    if num1==1:
        sumar(num2,num3)
    elif num1==2:
        restar(num2,num3)
    elif num1==3:
        multiplicar(num2,num3)
    elif num1==4:
        dividir(num2,num3)
    elif num1==5:
        print("Adios")
    else:
        print("Ingrese un número valido")
        main()

def sumar(a,b):
    suma=a+b  
    print(suma)
    main()

def restar(a,b):
    resta=(a-b)
    print(resta)
    main()

def multiplicar(a,b):
    multipli=(a*b)
    print(multipli)
    main()

def dividir(a,b):
    division=(a/b)
    print(division)
    main()

if __name__ == "__main__":
    main()