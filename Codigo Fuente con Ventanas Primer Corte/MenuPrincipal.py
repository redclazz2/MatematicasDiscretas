import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
from Primos import VentanaPrimos
from Bases import VentanaBases
from Fibo import VentanaFibo

class menuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/menuPrincipal.ui",self)
               
        self.Archivo_AbrirVentana1.triggered.connect(self.submenuPrimos)
        self.actionAbrir_calculadora_de_bases.triggered.connect(self.submenuBases)
        self.Archivo_AbrirVentana2.triggered.connect(self.submenuFibo)
        self.Archivo_Salir.triggered.connect(self.close)
        self.pushButton.clicked.connect(self.botonLanzador)
        self.pushButton_2.clicked.connect(self.close)
        
    def submenuPrimos(self): 
        self.ventanita1 = VentanaPrimos()
        self.ventanita1.show()
    
    def submenuBases(self):
        self.ventanita2 = VentanaBases()
        self.ventanita2.show()
        
    def submenuFibo(self):
        self.ventanita3 = VentanaFibo()
        self.ventanita3.show()
        
    def botonLanzador(self):
        if(self.comboBox.currentText() == "Seleccione una aplicación"):
            QMessageBox.about(self, "Alerta", "Seleccione una opción válida.")
        if(self.comboBox.currentText() == "Calculadora números primos"):
            self.submenuPrimos()
        if(self.comboBox.currentText() == "Calculadora secuencia Fibonacci"):
            self.submenuFibo()
        if(self.comboBox.currentText() == "Calculadora de bases numéricas"):
            self.submenuBases()
            
        
    def closeEvent(self,event):
        respuesta = QMessageBox.question(self,"Confirmación","Quiere finalizar la ejecución del programa?",
                                         QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = menuPrincipal()
    menu.show()
    sys.exit(app.exec_())
