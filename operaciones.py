import math
class Operaciones:
    def __init__(self, num1: object, num2: object) -> object:
        self.num1 = int(num1)
        self.num2 = int(num2)

    def suma(self, num1, num2):
        resultado = num1 + num2
        print(f"Suma: {num1} + {num2} = {resultado}")
        return resultado

    def resta(self, num1, num2):
        resultado = num1 - num2
        print(f"Resta: {num1} - {num2} = {resultado}")
        return resultado

    def multi(self, num1, num2):
        resultado = num1 * num2
        print(f"Multiplicación: {num1} * {num2} = {resultado}")
        return resultado

    def divi(self, num1, num2):
        if num2 != 0:
            resultado = num1 / num2
            print(f"División: {num1} / {num2} = {resultado}")
            return resultado
        else:
            print("Error: División por cero")
            return "Error: División por cero"

    def maxi(self, lista):
        resultado = max(lista)
        print(f"Máximo: {resultado}")
        return resultado

    def mini(self, lista):
        resultado = min(lista)
        print(f"Mínimo: {resultado}")
        return resultado

    def sen(self, angulo):
        resultado = math.sin(math.radians(angulo))
        print(f"Seno: sin({angulo}°) = {resultado}")
        return resultado

    def cos(self, angulo):
        resultado = math.cos(math.radians(angulo))
        print(f"Coseno: cos({angulo}°) = {resultado}")
        return resultado

    def tan(self, angulo):
        resultado = math.tan(math.radians(angulo))
        print(f"Tangente: tan({angulo}°) = {resultado}")
        return resultado

    def prome(self, lista):
        resultado = sum(lista) / len(lista)
        print(f"Promedio: {resultado}")
        return resultado



