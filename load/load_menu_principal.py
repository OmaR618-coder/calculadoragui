from PyQt5 import QtWidgets,uic
from load.load_ventana_calculadora import VentanaCalculadora #Importamos por que esta en otro archivo
from load.load_ventana_galones_litros import VentanaGalonesLitros
from load.load_ventana_millas_km import VentanaMillasKm
from load.load_ventana_temperatura import VentanaTemperatura

class MenuPrincipal(QtWidgets.QMainWindow): #HEREDAS DE UN MAIN WINDOW
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui",self) #NOMBRE ARCHIVO
        self.showMaximized()
        
        
        self.actionCalculadora.triggered.connect(self.ingresarCalculadora) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)
        """self.boton_sumar.clicked.connect(self.botonSumarClick)"""
        self.actionGalitros.triggered.connect(self.ingresarGalitros) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

        self.actionMillasKm.triggered.connect(self.ingresarMillasKm) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

        self.actionTemp.triggered.connect(self.ingresarTemp) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

    def ingresarCalculadora(self):
        calculadora = VentanaCalculadora()
        calculadora.exec()
    
    def ingresarGalitros(self):
        galitros = VentanaGalonesLitros()
        galitros.exec()

    def ingresarMillasKm(self):
        millasKm = VentanaMillasKm()
        millasKm.exec()

    def ingresarTemp(self):
        temp = VentanaTemperatura()
        temp.exec()

    def salir(self):
        self.close()
    