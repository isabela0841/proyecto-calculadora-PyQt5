class ConversionNumeroTexto:
    def __init__(self):
        self.unidades = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
        self.decenas = ["", "Diez", "Veinte", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
        self.especiales = ["", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciséis", "Diecisiete", "Dieciocho", "Diecinueve"]

    def convertir_a_texto(self, numero):
        if numero < 10:
            return self.unidades[numero]
        elif 10 <= numero < 20:
            return self.especiales[numero - 10]
        else:
            unidad = numero % 10
            decena = numero // 10
            return f"{self.decenas[decena]} {self.unidades[unidad]}"


