import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox
from operaciones import Operaciones
from conversor_texto import ConversionNumeroTexto

class CalculadoraGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("diseñocalculadora.ui", self)  # Cambiar el nombre del archivo .ui

        self.setWindowTitle('Calculadora')
        self.setGeometry(100, 100, 400, 600)

        # Conectar los botones a sus funciones correspondientes
        self.findChild(QPushButton, 'pushButton_1').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_2').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_3').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_4').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_5').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_6').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_7').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_8').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_9').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_0').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_suma').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_resta').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_multiplicacion').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_division').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_seno').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_coseno').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_tangente').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_maximo').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_minimo').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'pushButton_igual').clicked.connect(self.calcular)
        self.findChild(QPushButton, 'pushButton_c').clicked.connect(self.clear)
        self.findChild(QPushButton, 'pushButton_signo').clicked.connect(self.cambiar_signo)

        self.result_label = self.findChild(QLabel, 'labelResultado')
        self.input_line = self.findChild(QLineEdit, 'lineEditEntrada')
        self.operation_combo = self.findChild(QComboBox, 'comboBoxOperacion')

    def button_click(self):
        button = self.sender()
        current_text = self.input_line.text()
        new_text = current_text + button.text()
        self.input_line.setText(new_text)

    def calcular(self):
        num1 = float(self.input_line.text())
        operacion = self.operation_combo.currentText()

        operaciones = Operaciones
        resultado = operaciones.realizar_operacion(num1, operacion)

        conversor = ConversorTexto()
        resultado_texto = conversor.convertir_a_texto(resultado)

        self.result_label.setText(resultado_texto)

    def clear(self):
        self.input_line.clear()
        self.result_label.clear()

    def cambiar_signo(self):
        current_text = self.input_line.text()
        if current_text and current_text[0] == '-':
            self.input_line.setText(current_text[1:])
        else:
            self.input_line.setText('-' + current_text)

