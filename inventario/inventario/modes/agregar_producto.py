def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
    precio = float(input(f"Ingrese el precio de '{nombre}': "))

    from agregar_producto import validar_precio

    if validar_precio(precio):
        inventario.agregar_producto(nombre, cantidad, precio)



