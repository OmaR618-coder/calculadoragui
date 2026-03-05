from PyQt5 import QtWidgets,uic
from clases.temperatura import Temperatura #Importamos por que esta en otro archivo

class VentanaTemperatura(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_temperatura.ui",self) #load codigo ui en gui
        self.show()
        
        self.buttonPush.clicked.connect(self.botonConvertirClick) #nombre boton push 

    def botonConvertirClick(self):
        faren = int(self.lineEdit_farenheit.text())
        convertir = Temperatura(faren) #NUEVA VARIABLE PARA GUARDAR 
        convertir.calcularCentigrados() #LLAMAMAOS METODO
        self.label_resultado.setText(str(convertir.centigrados)) #nombre del label de qt
    
        