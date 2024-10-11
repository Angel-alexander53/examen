class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, manzana, cantidad, precio):
        if manzana in self.productos:
            print(f"El producto '{manzana}' ya existe en el inventario.")
        else:
            self.productos[manzana] = {"cantidad": cantidad, "precio": precio}
            print(f"Producto '{manzana}' agregado correctamente.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for nombre, datos in self.productos.items():
                print(f"Producto: {nombre} - Cantidad: {datos['cantidad']} - Precio: {datos['precio']}")

    def valor_total(self):
        total = sum(datos["cantidad"] * datos["precio"] for datos in self.productos.values())
        print(f"El valor total del inventario es: {total}")

    def actualizar_precio(self, nombre, nuevo_precio):
        if nombre in self.productos:
            self.productos[nombre]["precio"] = nuevo_precio
            print(f"Precio de '{nombre}' actualizado a {nuevo_precio}.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        if nombre in self.productos:
            self.productos[nombre]["cantidad"] = nueva_cantidad
            print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def actualizar_nombre(self, nombre_antiguo, nombre_nuevo):
        if nombre_antiguo in self.productos:
            self.productos[nombre_nuevo] = self.productos.pop(nombre_antiguo)
            print(f"Nombre del producto actualizado de '{nombre_antiguo}' a '{nombre_nuevo}'.")
        else:
            print(f"El producto '{nombre_antiguo}' no existe en el inventario.")