from PyQt5 import QtWidgets,uic
from clases.millas_km import MillasKm #Importamos por que esta en otro archivo

class VentanaMillasKm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_millas_km.ui",self) #load codigo ui en gui
        self.show()
        
        self.pushButton.clicked.connect(self.botonConvertirClick) #nombre boton push 

    def botonConvertirClick(self):
        mil = int(self.lineEdit_millas.text())
        conversiones = MillasKm(mil) #NUEVA VARIABLE PARA GUARDAR 
        conversiones.calcularKm() #LLAMAMAOS METODO
        self.label_resultado_km.setText(str(conversiones.km)) #nombre del label de qt
    
        