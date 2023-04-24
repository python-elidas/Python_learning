class Bici:
    def __init__(self, rueda, rgb=(255,255,255)):
        rueda_d = rueda
        rueda_t = rueda
        self.color = rgb
        self.rueda = [rueda_d, rueda_t]
        
    def rayon(self):
        if caida == True:
            self.color = (255,255,200)
            
    def pinchazo(self):
        if clavo == True:
            self.rueda[1] = 0
        
mi_bici = Bici()