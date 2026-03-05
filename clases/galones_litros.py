class GalonesLitros():
    def __init__(self, gal): #recibe atributo gal
        self.galones = gal #No ponemos input ya que lo tenemos en interfaz ya
        self.litros = 0 #resultado

    def calcularLitros(self):
        self.litros = float(self.galones*3.7854)


        """print("Cantidad convertida a litros: ", float(self.litros))"""