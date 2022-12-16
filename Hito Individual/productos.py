class Productos:
    def __init__(self,id_producto,nombre_producto, precio, stock):
        self.id_producto=id_producto
        self.nombre_producto=nombre_producto
        self.precio=precio
        self.stock=stock

    def mostrarFichaProductos(self):
        print(f'Ficha del producto {self.id_producto} \nNombre del producto: {self.nombre_producto} \nPrecio: {self.precio} \nStock: {self.stock}')

# producto1=Productos(1,'Silla', 20, True)
# producto2=Productos(2,'Mesa', 50, True)
# producto3=Productos(3, 'Lampara', 10, False)
# producto4=(4, 'Cama', 300, True)
# producto5=(5, 'Alfombra', 5, False)
# producto6=(6, 'Puerta', 45, True)


