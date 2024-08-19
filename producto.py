# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa un nuevo producto con un ID, nombre, cantidad y precio.
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Método getter para obtener el ID del producto
    @property
    def id_producto(self):
        return self._id_producto

    # Método setter para establecer un nuevo ID para el producto
    @id_producto.setter
    def id_producto(self, value):
        self._id_producto = value

    # Método getter para obtener el nombre del producto
    @property
    def nombre(self):
        return self._nombre

    # Método setter para establecer un nuevo nombre para el producto
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Método getter para obtener la cantidad disponible del producto
    @property
    def cantidad(self):
        return self._cantidad

    # Método setter para actualizar la cantidad del producto
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    # Método getter para obtener el precio del producto
    @property
    def precio(self):
        return self._precio

    # Método setter para establecer un nuevo precio para el producto
    @precio.setter
    def precio(self, value):
        self._precio = value

    def __str__(self):
        # Devuelve una cadena con los detalles del producto: nombre, cantidad y precio.
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase que gestiona el inventario de productos
class Inventario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos del inventario.
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un nuevo producto al inventario si el ID no está duplicado.
        if not any(p.id_producto == producto.id_producto for p in self.productos):
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado correctamente.")
        else:
            print(f"Error: El ID '{producto.id_producto}' ya existe. Por favor, use un ID único.")

    def id_unico(self, id_producto):
        # Verifica si el ID proporcionado es único en el inventario.
        return not any(p.id_producto == id_producto for p in self.productos)

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario usando su ID, si existe.
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
            print(f"Producto con ID '{id_producto}' eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad y/o el precio de un producto existente.
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto con ID '{id_producto}' actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        # Muestra todos los productos actualmente en el inventario.
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

    def listar_ids(self):
        # Lista todos los IDs de productos en el inventario junto con sus nombres.
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("IDs disponibles:")
            for producto in self.productos:
                print(f"- {producto.id_producto}, {producto.nombre}")

    def buscar_producto(self, nombre):
        # Busca productos por nombre, mostrando aquellos que coincidan parcial o totalmente.
        encontrado = False
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

# Función que gestiona el menú interactivo de la aplicación
def menu():
    # Crea una instancia de Inventario para gestionar los productos.
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto ID\n2. Eliminar Producto x ID\n3. Actualizar Producto x ID\n4. Buscar Producto x Nombre\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            # Solicita la entrada del ID del producto y verifica su unicidad antes de agregarlo al inventario.
            while True:
                id_producto = input("Ingrese el ID del producto (ej. EC-001): ")
                if inventario.id_unico(id_producto):
                    break
                else:
                    print(f"Error: El ID '{id_producto}' ya existe. Por favor, use un ID único.")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: ").replace(',', '.'))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Muestra todos los IDs de productos y permite eliminar uno especificando su ID.
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a eliminar (ej. EC-001): ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Permite actualizar la cantidad y/o el precio de un producto existente.
            inventario.listar_ids()
            id_producto = input("Ingrese el ID del producto a actualizar (ej. EEUU-001): ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Permite buscar productos por nombre dentro del inventario.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Muestra todos los productos del inventario.
            inventario.mostrar_inventario()

if __name__ == "__main__":
    # Inicia la ejecución del programa mostrando el menú interactivo.
    menu()
