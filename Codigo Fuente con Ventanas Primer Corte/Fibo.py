import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 

class VentanaFibo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/fibonacci.ui",self)
        self.boton.clicked.connect(self.calcular)
        
    def calcular(self):
        a,b,maxi,check = 0,1,int(self.testo.text()),True 
        resultados = []
        for n in range(0,maxi):
            if(check):
                resultados.append(a); resultados.append(b); check = False
            c = a + b; a = b; b = c; resultados.append(c)
        if(self.radioButton.isChecked()):
           resultados.remove(0)
           resultados.remove(1)
        QMessageBox.about(self, "Resultados", "Se han calculado %s números de la secuencia: %s"%(self.testo.text(),str(resultados)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Fibo = VentanaFibo()
    Fibo.show()
    sys.exit(app.exec_())