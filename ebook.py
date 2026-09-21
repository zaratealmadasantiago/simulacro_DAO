from material import Material

class Ebook(Material):
    def __init__(self, codigo, titulo, autor, precio_base, valor_venta):
        super().__init__(codigo, titulo, autor, precio_base)
        self.valor_venta = valor_venta
        self.tipo = 2
    
    def calcular_costo_mantenimiento(self):
        costo = 0.05 * self.valor_venta
        return costo
