class MillasKm():
    def __init__(self, mil): #Recibe atributo mil
        self.millas = mil #No ponemos input ya que este ya tiene su boton en interfaz
        self.km = 0 #resultado
        
    def calcularKm(self):
        self.km = self.millas*1.609344
        
        
        """print("km: ",self.km)"""