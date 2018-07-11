class Contacto(object):
    def __init__(self, telefono = 0, nombre = "", email = ""):
        self.telefono = telefono
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return "Telefono: " + str(self.telefono) + "\nNombre: " + str(self.nombre) + "\nemail: " + str(self.email)
