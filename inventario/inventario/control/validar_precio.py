def validar_precio(precio):
    if precio > 0:
        return True
    else:
        print("El precio debe ser mayor que cero.")
        return False

