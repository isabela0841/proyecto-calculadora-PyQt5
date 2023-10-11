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
        self.findChild(QPushButton, 'btnProm').clicked.connect(self.promedio)
        self.findChild(QPushButton, 'btnMax').clicked.connect(self.maximo)
        self.findChild(QPushButton, 'btnMin').clicked.connect(self.minimo)
        self.findChild(QPushButton, 'btnSen').clicked.connect(self.seno)
        self.findChild(QPushButton, 'btnCos').clicked.connect(self.coseno)
        self.findChild(QPushButton, 'btnTan').clicked.connect(self.tangente)
        self.findChild(QPushButton, 'btnIgual').clicked.connect(self.calcular)
        self.findChild(QPushButton, 'btnBorrar').clicked.connect(self.clear)
        self.findChild(QPushButton, 'btnOpen').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnClose').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnDel').clicked.connect(self.borrar)
        self.findChild(QPushButton, 'btnPunto').clicked.connect(self.button_click)
        self.findChild(QPushButton, 'btnComa').clicked.connect(self.button_click)

        self.result_label = self.findChild(QLabel, 'label_result')
        self.input_line = self.findChild(QLabel, 'label_prev')


    def button_click(self):
        button = self.sender()
        current_text = self.input_line.text()
        new_text = current_text + button.text()
        self.input_line.setText(new_text)

    def seno(self):
        text = self.input_line.text()
        self.input_line.setText(text + "sen(")

    def coseno(self):
        text = self.input_line.text()
        self.input_line.setText(text + "cos(")

    def tangente(self):
        text = self.input_line.text()
        self.input_line.setText(text + "tan(")

    def promedio(self):
        text = self.input_line.text()
        self.input_line.setText(text + "P(")

    def maximo(self):
        text = self.input_line.text()
        self.input_line.setText(text + "max(")

    def minimo(self):
        text = self.input_line.text()
        self.input_line.setText(text + "min(")



    def calcular(self):
        funcion = ""
        angulo = ""
        ecuacion = self.input_line.text()
        newEcuacion = ""
        resultado = ""
        lista = []
        valoresLista = ""
        try:
            for i in ecuacion:
                if i == ",":
                    if funcion == "max" or funcion == "min" or funcion == "P":
                        valoresLista = valoresLista + i
                    continue
                elif i.isdigit():
                    if funcion == "sen" or funcion == "cos" or funcion == "tan":
                        angulo = angulo + i
                    elif funcion == "max" or funcion == "min" or funcion == "P":
                        valoresLista = valoresLista + i
                    else:
                        newEcuacion = newEcuacion + i
                elif i == "+":
                    newEcuacion = newEcuacion + i
                elif i == "-":
                    newEcuacion = newEcuacion + i
                elif i == "*":
                    newEcuacion = newEcuacion + i
                elif i == "/":
                    newEcuacion = newEcuacion + i
                elif i == "(":
                    continue
                elif i == ")":
                    if funcion == "sen":
                        resultado = str(Operaciones.sen(self, int(angulo)))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        angulo = ""
                    if funcion == "cos":
                        resultado = str(Operaciones.cos(self, int(angulo)))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        angulo = ""
                    if funcion == "tan":
                        resultado = str(Operaciones.tan(self, int(angulo)))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        angulo = ""
                    if funcion == "max":
                        lista = valoresLista.split(",")
                        resultado = str(Operaciones.maxi(self, lista))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        lista = []
                        valoresLista = ""
                    if funcion == "min":
                        lista = valoresLista.split(",")
                        resultado = str(Operaciones.mini(self, lista))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        lista = []
                        valoresLista = ""
                    if funcion == "P":
                        lista = valoresLista.split(",")
                        resultado = str(Operaciones.prome(self, lista))
                        newEcuacion = newEcuacion + resultado
                        funcion = ""
                        lista = []
                        valoresLista = ""
                    continue
                else:
                    funcion = funcion + i
                    self.result_label.setText("true")

            ans = eval(newEcuacion)
            self.result_label.setText(str(ans))

        except Exception as inst:
            print(type(inst))  # the exception type
            print(inst.args)  # arguments stored in .args
            print(inst)
            self.result_label.setText("Syntax Error")

        #conversor = ConversionNumeroTexto
        #resultado_texto = conversor.convertir_a_texto(resultado)

        #self.result_label.setText(resultado_texto)

    def clear(self):
        self.input_line.clear()
        self.result_label.clear()

    def borrar(self):
        valor = self.input_line.text()
        self.input_line.setText(valor[:-1])
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
