import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 

class VentanaBases(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/bases.ui",self)
        self.boton1.clicked.connect(self.partidaBaseDistintaDiezADiez)
        self.boton2.clicked.connect(self.funcionPartidaBaseDiezAOtraBase)
        self.boton3.clicked.connect(self.baseDistintaDiezADistintaDiez)
        
    def partidaBaseDistintaDiezADiez(self):
        resultado = funcion1(self.entrada1.text(),self.entradaBase1.text())
        self.salida1.setText("El número en base 10 \nes: %s" %resultado)
        if self.radioButton.isChecked():
            QMessageBox.about(self, "Resultados", "El número en base 10 \nes: %s" %resultado)

    def funcionPartidaBaseDiezAOtraBase(self):
        resultado = funcion2(self.entrada2.text(),self.entradaBase2.text())
        self.salida2.setText("El número en base %s \nes: %s" %(self.entradaBase2.text(),resultado))
        if self.radioButton.isChecked():
            QMessageBox.about(self, "Resultados", "El número en base %s \nes: %s" %(self.entradaBase2.text(),resultado))
    
    def baseDistintaDiezADistintaDiez(self):
        w = funcion1(self.entrada3.text(),self.entrada4.text())
        resultado = funcion2(w,self.entrada5.text())
        self.salida3.setText("El número en base %s \nes: %s" %(self.entrada5.text(),resultado))
        if self.radioButton.isChecked():
            QMessageBox.about(self, "Resultados", "El número en base %s \nes: %s" %(self.entrada5.text(),resultado))
              
def funcion1(numero,base):
    negativo = False
    almacenTemp = 0
    arrayNumero = list(numero)
    if(arrayNumero[0]=="-"):
            negativo = True
            arrayNumero.remove("-")
    longitudBucle = len(arrayNumero)
    for n in range(0,longitudBucle):
        almacenTemp += int(arrayNumero[n]) * (pow(int(base),longitudBucle-(n+1)))
    if(negativo):
        return "-"+str(almacenTemp)
    else:
        return str(almacenTemp)

def funcion2(numero,base):
    negativo = False
    cociente = 1
    if("-" in str(numero)):
        negativo = True
        tempListConvertir = list(str(numero))
        tempListConvertir.remove("-")
        numero = "".join(map(str,tempListConvertir))
    dividiendo = int(numero)
    storeResultado = []
    while(cociente != 0):
        resto = dividiendo % int(base)
        cociente = dividiendo // int(base)
        dividiendo = cociente
        storeResultado.append(resto)
    if(negativo):
        resultado = "-"+"".join(map(str,reversed(storeResultado)))
        return resultado
    else:
        return "".join(map(str,reversed(storeResultado)))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    bass = VentanaBases()
    bass.show()
    sys.exit(app.exec_())