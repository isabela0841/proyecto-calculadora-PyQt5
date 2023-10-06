import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from diseñocalculadora import Ui_MainWindow  # Importa la clase generada desde ui_tu_archivo.py

class MiVentana(QMainWindow):
    def _init_(self):
        super()._init_()

        # Crea una instancia de la clase Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Configura la interfaz de usuario en la ventana principal

if __name__ == "_main_":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())


