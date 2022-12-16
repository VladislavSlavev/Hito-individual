class Cliente:
    def __init__(self,nif,nombre,email,telefono,direccion,pais):
        self.nif=nif
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        self.direccion=direccion
        self.pais=pais
    def mostrarFichaCliente(self):
        print(f'Ficha del cliente con el NIF {self.nif} \nNombre: {self.nombre} \nEmail: {self.email} \nDireccion: {self.direccion} \nPais: {self.pais}')

#cliente1=Cliente('xrhjrr5', 'Pepe', 'ereff@gmail.es', '667754434', 'los pepes 44', 'Andorra')
#cliente1=Cliente(input('Inserta el NIF: '), input('Inserta el nombre: '), input('Inserta el email: '), input('Inserta el telefono: '), input('Inserta la direccion: '), input('Inserta el pais: '))
# cliente1.mostrarFichaCliente()
