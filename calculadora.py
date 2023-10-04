from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from operaciones import Operaciones
from conversor_texto import ConversorTexto

class CalculadoraGUI(QMainWindow):
    def __init__(self, iu_file):
        super().__init__()
        uic.loadUi(iu_file, self)
        self.initIU()

        self.operaciones = Operaciones()
        self.conversor = ConversorTexto()

        self.pushButtonCalcular.clicked.connect(self.calcular)

        def initUI(self):
            self.setWindowTitle('Calculadora')
            self.show()

        def calcular(self):
            num1 = float(self.lineEditNumero1.text())
            num2 = float(self.lineEditNumero2.text())
            operacion = self.comboBoxOperacion.currentText()

            if operacion == "Suma":
                resultado = self.operaciones.suma(num1, num2)
            elif operacion == "Resta":
                resultado = self.operaciones.resta(num1, num2)
            elif operacion == "Multiplicación":
                resultado = self.operaciones.multiplicacion(num1, num2)
            elif operacion == "División":
                resultado = self.operaciones.division(num1, num2)
            elif operacion == "Máximo":
                resultado = self.operaciones.maximo([num1, num2])
            elif operacion == "Mínimo":
                resultado = self.operaciones.minimo([num1, num2])
            elif operacion == "Seno":
                resultado = self.operaciones.seno(num1)
            elif operacion == "Coseno":
                resultado = self.operaciones.coseno(num1)
            elif operacion == "Tangente":
                resultado = self.operaciones.tangente(num1)
            elif operacion == "Promedio":
                resultado = self.operaciones.promedio([num1, num2])
            else:
                resultado = "Operación no válida"

            self.labelResultado.setText(str(resultado))
            resultado_texto = self.conversor.convertir_a_texto(resultado)
            QMessageBox.information(self, 'Resultado', resultado_texto)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = CalculadoraGUI("diseñocalculadora.ui")
        sys.exit(app.exec_())