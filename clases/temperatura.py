class Temperatura():
    def __init__(self, faren):
        self.farenheit = faren 
        self.centigrados = 0
    
    def calcularCentigrados(self):
        self.centigrados = (self.farenheit-32)*5/9
        
        
        """print("Temperatura en grados Centigrados: ",int(self.centigrados),"°C")"""