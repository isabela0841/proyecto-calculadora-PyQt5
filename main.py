import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox
from conversor_texto import ConversionNumeroTexto
from operaciones import Operaciones

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        uic.loadUi("diseñocalculadora.ui", self)
        self.findChild(QPushButton, 'btn0').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn1').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn2').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn3').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn4').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn5').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn6').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn7').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn8').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btn9').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnSuma').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnResta').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnMulti').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnDivision').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnProm').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnMax').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnMin').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnSen').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnCos').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnTan').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnIgual').clicked.connect(self.calcular)
        self.findChild(QPushButton, 'btnBorrar').clicked.connect(self.clear)

        self.result_label = self.findChild(QLabel, 'label_result')
        self.input_line = self.findChild(QLabel, 'label_prev')


    def button_click(self):
        button = self.sender()
        current_text = self.input_line.text()
        new_text = current_text + button.text()
        self.input_line.setText(new_text)

    def calcular(self):
        ecuacion = self.input_line.text()
        try:
            ans = eval(ecuacion)
            self.result_label.setText(str(ans))

        except:
            self.result_label.setText("Syntax Error")

        #conversor = ConversionNumeroTexto
        #resultado_texto = conversor.convertir_a_texto(resultado)

        #self.result_label.setText(resultado_texto)

    def clear(self):
        self.input_line.clear()
        self.result_label.clear()
    def cambiar_signo(self):
        current_text = self.input_line.text()
        if current_text and current_text[0] == '-':
            self.input_line.setText(current_text[1:])
        else:
            self.input_line.setText('-' + current_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
