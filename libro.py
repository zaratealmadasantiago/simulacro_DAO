from material import Material
import math

class Libro(Material):
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self.dias_prestados = dias_prestados
        self.tipo = 1
    
    def calcular_costo_mantenimiento(self):
        costo = 0
        if self.dias_prestados > 0:
            costo = 100 * math.ceil(self.dias_prestados/30)
        return costo
    

    
