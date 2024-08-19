# Clase Producto .
class Producto:
    def _init_(self, id_producto, nombre, cantidad, precio):

        #Constructor de la clase Producto.

        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getter para id_producto
    @property
    def id_producto(self):
        return self._id_producto

    # Setter para id_producto
    @id_producto.setter
    def id_producto(self, value):
        self._id_producto = value

    # Getter para nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Getter para cantidad
    @property
    def cantidad(self):
        return self._cantidad

    # Setter para cantidad
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    # Getter para precio
    @property
    def precio(self):
        return self._precio

    # Setter para precio
    @precio.setter
    def precio(self, value):
        self._precio = value

    def _str_(self):

        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"
