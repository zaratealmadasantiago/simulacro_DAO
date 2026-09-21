from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca("material.csv")
    
    # Imprimir resultados de los métodos de la clase Biblioteca
    print("Cantidad de materiales por tipo:")
    print(biblioteca.cantidad_por_tipo())
    
    print("\nPromedio de precios base:")
    print(biblioteca.calcular_promedio_precios_base())
    
    print("\nMaterial con mayor costo de mantenimiento:")
    material_caro = biblioteca.obtener_material_mayor_costo_mantenimiento()
    print(f"Código: {material_caro.codigo}, Título: {material_caro.titulo}, Costo: {material_caro.calcular_costo_mantenimiento()}")
    
    print("\nSuma del costo de mantenimiento:")
    print(biblioteca.calcular_suma_costo_mantenimiento())
    
    print("\nCantidad de libros prestados más de 30 días:")
    print(biblioteca.contar_libros_mas_30_dias())
    
    print("\nCantidad de revistas importadas:")
    print(biblioteca.contar_revistas_importadas())

if __name__ == "__main__":
    main()