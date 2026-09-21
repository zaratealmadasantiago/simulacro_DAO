from pathlib import Path
from libro import Libro
from ebook import Ebook
from revista import Revista

class Biblioteca():
    def __init__(self, path):
        if (not(Path(path).exists())):
            raise FileNotFoundError
        self.path  = path
        self.materiales = self.agregar()

    def agregar(self):
        with open(self.path, 'r', encoding="utf-8") as n:
            mat = n.readlines()
            materiales = []
            for m in mat:
                tipo, codigo, titulo, autor, precio_base, extra= m.strip().split(",")
                precio_base = float(precio_base)
                if tipo == "1":
                    dias_prestados = int(extra)
                    materiales.append(Libro(codigo,titulo,autor,precio_base,dias_prestados))
                elif tipo == "2":
                    valor_venta = int(extra)
                    materiales.append(Ebook(codigo,titulo,autor,precio_base,valor_venta))
                else:
                    origen = extra
                    materiales.append(Revista(codigo,titulo,autor,precio_base,origen))
        return materiales
    
    def cantidad_materiales(self):
        return self.materiales
    
    def cantidad_por_tipo(self):
        material_x_tipo = {"Libro": 0, "Ebook": 0, "Revista": 0 }
        for m in self.materiales:
            if isinstance(m, Libro):
                material_x_tipo["Libro"] +=1
            if isinstance(m, Ebook):
                material_x_tipo["Ebook"] +=1
            if isinstance(m, Revista):
                material_x_tipo["Revista"] +=1
        return material_x_tipo
    
    def calcular_promedio_precios_base(self):
        if not self.materiales:
            return 0
        
        sum_precio = 0
        acu_precio = 0
        for m in self.materiales:
            sum_precio += m.precio_base
            acu_precio += 1
        promedio = sum_precio/acu_precio
        return promedio
    
    def obtener_material_mayor_costo_mantenimiento(self):
        material = None
        for m in self.materiales:
            if material != None:
                if m.calcular_costo_mantenimiento() > material.calcular_costo_mantenimiento():
                    material = m
            else: material = m
        return material
    
    def calcular_suma_costo_mantenimiento(self):
        sum = 0
        for m in self.materiales:
            sum += m.calcular_costo_mantenimiento()
        return sum
    
    def contar_libros_mas_30_dias(self):
        cant_libros_mas_30 = 0
        for m in self.materiales:
            if isinstance(m, Libro) and m.dias_prestados > 30:
                cant_libros_mas_30 += 1
        return cant_libros_mas_30

    def contar_revistas_importadas(self):
        cant_rev_importadas = 0
        for m in self.materiales:
            if isinstance(m, Revista) and m.origen == "importada":
                cant_rev_importadas += 1
        return cant_rev_importadas
