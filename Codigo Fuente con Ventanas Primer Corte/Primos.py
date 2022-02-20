#Inicio
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math


class VentanaPrimos(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/primos.ui",self)
        self.buton.clicked.connect(self.calcular)
        
    def calcular(self):
        n = int(self.tesbos.text())
        n2 = int(self.tesbos2.text())
        listaResultado = [o for o in range(n,n2+1) if all(o % u != 0 for u in range(2,math.isqrt(o)+1))]
        if n == 0 and len(listaResultado)>0:
            listaResultado.remove(0); listaResultado.remove(1)
        QMessageBox.about(self, "Resultado", "Hay un total de: %s números. Específicamente: %s" %(len(listaResultado),str(listaResultado)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prim = VentanaPrimos()
    prim.show()
    sys.exit(app.exec_())