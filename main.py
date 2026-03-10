from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_galones_litros import VentanaGalonesLitros
from load.load_ventana_millas_km import VentanaMillasKm
from load.load_ventana_temperatura import VentanaTemperatura
from load.load_menu_principal import MenuPrincipal

from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    venti = MenuPrincipal()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
