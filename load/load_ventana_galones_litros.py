from PyQt5 import QtWidgets,uic
from clases.galones_litros import GalonesLitros #Importamos por que esta en otro archivo

class VentanaGalonesLitros(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_galones_litros.ui",self) #load codigo ui en gui
        self.show()
        
        self.convertir.clicked.connect(self.botonConvertirClick) #nombre boton push 

    def botonConvertirClick(self):
        gal = int(self.lineEdit_2.text())
        conversion = GalonesLitros(gal) #NUEVA VARIABLE PARA GUARDAR 
        conversion.calcularLitros() #LLAMAMAOS METODO
        self.label_resultado.setText(str(conversion.litros)) #nombre del label de qt
    
        
    