from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(codigo, titulo, autor, precio_base)
        self.origen = origen
        self.tipo = 3

    def calcular_costo_mantenimiento(self):
        if self.origen == "nacional":
            costo = 50
        else: 
            costo = 60
        return costo