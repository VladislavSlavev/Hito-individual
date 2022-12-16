from clientes import Cliente
from productos import Productos

class Pedidos:
    def __init__(self, id_pedido, fecha_pedido, nombre, nombre_producto, cantidad, total):
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
        self.nombre = nombre
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.total = total

    def comprar1(self):
        if cliente1.pais.lower()!='españa':
            total=self.total+20
            print(f'No eres de España, los gastos de envio son 20 Euros, el total es: {total}')
        else:
            total=self.total
            print(f'Eres de España, asi que no tienes gastos de envios, tu pedido es de {total} Euros')
    def comprar2(self):
        if cliente2.pais.lower()!='españa':
            total=self.total+20
            print(f'No eres de España, los gastos de envio son 20 Euros, el total es: {total}')
        else:
            total=self.total
            print(f'Eres de España, asi que no tienes gastos de envios, tu pedido es de {total} Euros')
    def comprar3(self):
        if cliente3.pais.lower()!='españa':
            total=self.total+20
            print(f'No eres de España, los gastos de envio son 20 Euros, el total es: {total}')
        else:
            total=self.total
            print(f'Eres de España, asi que no tienes gastos de envios, tu pedido es de {total} Euros')
    def comprar4(self):
        if cliente4.pais.lower()!='españa':
            total=self.total+20
            print(f'No eres de España, los gastos de envio son 20 Euros, el total es: {total}')
        else:
            total=self.total
            print(f'Eres de España, asi que no tienes gastos de envios, tu pedido es de {total} Euros')

    def sms(self):
        print('SMS enviado')
    def pdf(self):
        print(f'PDF enviado')
    def mostrarFichaPedido(self):
        print(f'Pedido: {self.id_pedido} \nFecha: {self.fecha_pedido} \nCliente: {self.nombre} \nProducto: {self.nombre_producto} \nCantidad: {self.cantidad} \nTotal: {self.total}')

cliente1=Cliente('abcdd45', 'Pepe', 'pepe@gmail.es', '667754434', 'los robles 44', 'Andorra')
cliente2=Cliente('eertr54', 'Juan', 'juan@gmail.es', '622234453', 'peras 14', 'España')
cliente3=Cliente('e2e1eas', 'Maria', 'maria@gmail.es', '66445733', 'saucos 2', 'españa')
cliente4=Cliente('j5h12t2', 'Hulk Hogan', 'hulk@gmail.es', '64544321', 'hollywood avenue 134', 'Estados Unidos')

producto1=Productos(1, 'Silla', 20, True)
producto2=Productos(2, 'Mesa', 50, True)
producto3=Productos(3, 'Lampara', 10, False)
producto4=Productos(4, 'Cama', 300, True)
producto5=Productos(5, 'Alfombra', 5, False)
producto6=Productos(6, 'Puerta', 45, True)

pedido1=Pedidos(1, '05/12/2022', cliente1.nombre, producto3.nombre_producto, 3, (producto3.precio*3))
pedido2=Pedidos(2, '01/01/2022', cliente4.nombre, producto1.nombre_producto, 1, (producto1.precio*1))
pedido3=Pedidos(3, '11/05/2022', cliente3.nombre, producto6.nombre_producto, 5, (producto6.precio*5))
pedido4=Pedidos(4, '20/03/2022', cliente2.nombre, producto2.nombre_producto, 2, (producto2.precio*2))

print('1,2,3,4')
elegir=int(input('¿Que pedido quieres elegir?:'))

if elegir==1:
    pedido1.mostrarFichaPedido()
    pedido1.comprar1()
    sms_si=input('¿Quieres enviar un SMS del pedido?: ')
    if sms_si.lower()=='si':
        pedido1.sms()
    pdf_si=input('¿Quieres enviar un PDF del pedido?')

    if pdf_si.lower()=='si':
        pedido1.pdf()
    elif pdf_si.lower()=='no':
        print('Hasta pronto')
elif elegir==2:
    pedido2.mostrarFichaPedido()
    pedido2.comprar4()
    sms_si=input('¿Quieres enviar un SMS del pedido?: ')
    if sms_si.lower()=='si':
        pedido1.sms()
    pdf_si=input('¿Quieres enviar un PDF del pedido?')

    if pdf_si.lower()=='si':
        pedido1.pdf()
    elif pdf_si.lower()=='no':
        print('Hasta pronto')
elif elegir==3:
    pedido3.mostrarFichaPedido()
    pedido3.comprar3()
    sms_si=input('¿Quieres enviar un SMS del pedido?: ')
    if sms_si.lower()=='si':
        pedido1.sms()
    pdf_si=input('¿Quieres enviar un PDF del pedido?')

    if pdf_si.lower()=='si':
        pedido1.pdf()
    elif pdf_si.lower()=='no':
        print('Hasta pronto')
elif elegir==4:
    pedido4.mostrarFichaPedido()
    pedido4.comprar2()
    sms_si=input('¿Quieres enviar un SMS del pedido?: ')
    if sms_si.lower()=='si':
        pedido1.sms()
    pdf_si=input('¿Quieres enviar un PDF del pedido?')

    if pdf_si.lower()=='si':
        pedido1.pdf()
    elif pdf_si.lower()=='no':
        print('Hasta pronto')