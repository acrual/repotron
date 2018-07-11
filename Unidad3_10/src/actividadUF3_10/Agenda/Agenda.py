class Agenda(object):
    def __init__(self):
        self.contactos = []

    def __str__(self):
        cadena = "AGENDA"
        print(self.contactos)
        for i in range(len(self.contactos)):
            cadena = cadena + "\nContacto " + str(i + 1) +  "\n" + str(self.contactos[i].__str__())
        return cadena + "\nNúmero de contactos: " + str(len(self.contactos)) + "\n"

    def comprobarExisteTelefono(self, telefono):
        for i in range(len(self.contactos)):
            if self.contactos[i].telefono == telefono:
                return True
        return False

    def agregarContacto(self, contacto):
        if not self.comprobarExisteTelefono(contacto.telefono):
            self.contactos.append(contacto)
            return True
        else:
            return False

    def buscarPosicionTelefono(self,telefono):
        for i in range(len(self.contactos)):
            if self.contactos[i].telefono == telefono:
                return i
        return -1

    def eliminarContacto(self, telefono):
        pos = self.buscarPosicionTelefono(telefono)
        if pos != -1:
            self.contactos.pop(pos)
            return True
        else:
            return False

    def buscarContacto(self, contacto):
        for i in range(len(self.contactos)):
            if self.contactos[i].telefono == contacto.telefono:
                return contacto
        return None

    def modificarContacto(self, contacto):
        print("El nombre del contacto es ", self.contactos[self.buscarPosicionTelefono(contacto)].nombre)
        nuevoNombre = input("Escribe algo si deseas modificarlo o blanco si no: ")
        if nuevoNombre != "":
            self.contactos[self.buscarPosicionTelefono(contacto)].nombre = nuevoNombre

        print("El email del contacto es ", self.contactos[self.buscarPosicionTelefono(contacto)].email)
        nuevoEmail = input("Escribe algo si deseas modificarlo o blanco si no: ")
        if nuevoEmail != "":
            self.contactos[self.buscarPosicionTelefono(contacto)].email = nuevoEmail
