productos = []
ultimoId = 0
capacidadSecciones = {'a': 50, 'b': 50, 'c': 50, 'd': 50}

print("******************")
print("¡TIENDA DE COMICS!")
print("******************")
print()

opcion = 100
while opcion != 6:
    print("1. Registrar producto")
    print("2. Buscar cantidad de productos en bodega")
    print("3. Mostrar información de productos")
    print("4. Modificar cantidad de productos comprados")
    print("5. Eliminar un producto")
    print("6. Salir")

    formatoOpcion = input("Digita una opción del menú: ")

    if formatoOpcion.isdigit() and 1 <= int(formatoOpcion) <= 6:
        opcion = int(formatoOpcion)
    else:
        print("Por favor digita una opción válida entre 1 y 6.")
        continue

    if opcion == 1:
        while True:
            producto = {}
            ultimoId += 1
            if ultimoId > 100:
                print("Se ha alcanzado el límite de productos permitidos.")
                break  
            producto["id"] = ultimoId
            producto["nombre"] = input("Ingresa el nombre del producto: ")
            producto["precio"] = input("Ingresa el precio unitario del producto: ")
            while True:
                ubicacion = input("Indícanos en qué sección se almacenará el producto (A, B, C o D): ").lower()
                if ubicacion in ('a', 'b', 'c', 'd'):
                    if capacidadSecciones[ubicacion] > 0: 
                        producto["ubicacion"] = ubicacion
                        break
                    else:
                        print(f"No hay suficiente espacio en la sección {ubicacion.upper()} para almacenar el producto.")
                else:
                    print("Sección no válida. Por favor ingresa una sección válida (A, B, C o D).")
            while True:
                cantidad = int(input("¿Cuántas cantidades deseas agregar?: "))
                if cantidad > 0:  
                    if cantidad <= capacidadSecciones[producto["ubicacion"]]:
                        producto["cantidad"] = cantidad
                        capacidadSecciones[producto["ubicacion"]] -= cantidad
                        break
                    else:
                        print(f"No hay suficiente espacio en la sección {ubicacion.upper()} para almacenar {cantidad} unidades.")
                        print(f"Unidades disponibles en la sección {ubicacion.upper()}: {capacidadSecciones[ubicacion]}")
                else:
                    print("Por favor ingresa una cantidad mayor que 0.")
            producto["descripcion"] = input("Ingresa la descripción del producto: ")
            producto["casa"] = input("Ingresa la casa donde pertenece el producto (Marvel, DC...): ")
            producto["referencia"] = input("Ingresa la referencia del producto: ")
            producto["pais"] = input("Ingresa el país del producto: ")
            
            while True:
                garantia = input("¿Producto con garantía extendida? (Digita True o False): ").strip().lower()
                if garantia == "true" or garantia == "false":
                    producto["garantia"] = garantia.capitalize() 
                    break
                else:
                    print("Por favor, ingresa 'True' o 'False'.")
            
            productos.append(producto)
            print(f"Se agregaron {producto['cantidad']} unidades del producto '{producto['nombre']}' en la sección {producto['ubicacion'].upper()}")
            
            continuar = input("¿Quieres agregar otro producto? (Sí/No): ").lower()
            if continuar != "si":
                break

    elif opcion == 2:
        if productos:
            print("PRODUCTOS EN BODEGA:")
            for producto in productos:
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Ubicación: {producto['ubicacion']}")
                print(f"Cantidad: {producto['cantidad']}")
                print()
        else:
            print("No hay productos almacenados en la bodega.")

    elif opcion == 3:
        productoBuscado = input("Digita el nombre del producto que estás buscando: ")
        productosEncontrados = [producto for producto in productos if producto["nombre"].lower() == productoBuscado.lower()]
        if productosEncontrados:
            print("PRODUCTO ENCONTRADO:")
            for producto in productosEncontrados:
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio unitario: {producto['precio']}")
                print(f"Ubicación: {producto['ubicacion']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Descripción: {producto['descripcion']}")
                print(f"Casa: {producto['casa']}")
                print(f"Referencia: {producto['referencia']}")
                print(f"País: {producto['pais']}")
                print(f"Garantía extendida: {producto['garantia']}")
                print()
        else:
            print("¡Ups! No se encontraron productos que coincidan con la búsqueda.")

    elif opcion == 4:
        if productos:
            nombreProducto = input("Ingresa el nombre del producto que deseas modificar: ")
            productoEncontrado = False
            for producto in productos:
                if producto['nombre'].lower() == nombreProducto.lower():
                    productoEncontrado = True
                    print("Información del producto seleccionado:")
                    print(f"ID: {producto['id']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio unitario: {producto['precio']}")
                    print(f"Ubicación: {producto['ubicacion']}")
                    print(f"Cantidad: {producto['cantidad']}")
                    print(f"Descripción: {producto['descripcion']}")
                    print(f"Casa: {producto['casa']}")
                    print(f"Referencia: {producto['referencia']}")
                    print(f"País: {producto['pais']}")
                    print(f"Garantía extendida: {producto['garantia']}")
                    print()

                    print("¿Qué información deseas modificar?")
                    opcionesModificar = ["nombre", "precio", "ubicacion", "cantidad", "descripcion", "casa", "referencia", "pais", "garantia"]
                    for i, opcion in enumerate(opcionesModificar, 1):
                        print(f"{i}. {opcion.capitalize()}")
                    
                    opcionModificar = int(input("Selecciona el número correspondiente: "))
                    opcionModificar -= 1  
                    if 0 <= opcionModificar < len(opcionesModificar):
                        campoModificar = opcionesModificar[opcionModificar]
                        nuevoValor = input(f"Ingrese el nuevo valor para '{campoModificar.capitalize()}': ")
                        producto[campoModificar] = nuevoValor
                        print(f"Se ha modificado '{campoModificar.capitalize()}' del producto '{producto['nombre']}' exitosamente.")
                    else:
                        print("Opción no válida.")

            if not productoEncontrado:
                print("¡Ups! No encontramos ningún producto con ese nombre.")
        else:
            print("¡Ups! Aún no hay productos almacenados en la bodega.")

    elif opcion == 5:
        if productos:
            nombreProducto = input("Ingresa el nombre del producto que deseas eliminar: ")
            productoEncontrado = False
            for producto in productos:
                if producto['nombre'].lower() == nombreProducto.lower():
                    productoEncontrado = True
                    print("Información del producto seleccionado:")
                    print(f"ID: {producto['id']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio unitario: {producto['precio']}")
                    print(f"Ubicación: {producto['ubicacion']}")
                    print(f"Cantidad: {producto['cantidad']}")
                    print(f"Descripción: {producto['descripcion']}")
                    print(f"Casa: {producto['casa']}")
                    print(f"Referencia: {producto['referencia']}")
                    print(f"País: {producto['pais']}")
                    print(f"Garantía extendida: {producto['garantia']}")
                    print()

                    confirmacion = input("¿Estás seguro de que deseas eliminar este producto? (Sí/No): ").lower()
                    if confirmacion == "si":
                        productos.remove(producto)
                        print("El producto ha sido eliminado correctamente.")
                    else:
                        print("Operación cancelada.")
                    break

            if not productoEncontrado:
                print("No se encontró ningún producto con ese nombre.")
        else:
            print("No hay productos almacenados en la bodega.")

    elif opcion == 6: 
        print("¡Gracias por usar nuestros servicios! El menú se cerrará.")
