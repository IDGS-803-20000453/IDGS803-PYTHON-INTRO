import sys

class Calculadora:
    
    def main(self):
        num2 = int(input("Escoge tu primer numero "))
        num3 = int(input("Escoge tu segundo numero "))
        menu = "1.- Suma || 2.- Resta || 3.-Multiplicacion || 4.-Division|| 5.-Salir"
        print(menu)
        num1 = int(input("Escoge una opcion entre la 1 y la 5: "))
        
        if num1 == 1:
            self.sumar(num2, num3)
        elif num1 == 2:
            self.restar(num2, num3)
        elif num1 == 3:
            self.multiplicar(num2, num3)
        elif num1 == 4:
            self.dividir(num2, num3)
        elif num1 == 5:
            print("Adios")
            sys.exit()
        else:
            print("Ingrese un número valido")
            self.main()

    def sumar(self, a, b):
        suma = a + b  
        print(suma)
        self.main()

    def restar(self, a, b):
        resta = a - b
        print(resta)
        self.main()

    def multiplicar(self, a, b):
        multipli = a * b
        print(multipli)
        self.main()

    def dividir(self, a, b):
        division = a / b
        print(division)
        self.main()
        
if __name__ == "__main__":
    operaciones = Calculadora()
    operaciones.main()