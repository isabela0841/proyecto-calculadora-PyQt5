import sys
from PyQt5.QtWidgets import QApplication
from calculadora import CalculadoraGUI
from operaciones import Operaciones
from conversor_texto import ConversorTexto

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_file = "diseñocalculadora.ui"
    window = CalculadoraGUI(ui_file)
    window.show()
    sys.exit(app.exec_())

