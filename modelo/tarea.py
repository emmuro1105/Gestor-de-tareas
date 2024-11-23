class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento, estado=False):
        #inicializacion de los atributos de la tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado #estado "False" por defecto

    def completar(self): #cambia el atributo "estado" a "completado" 
        self.estado = True

    def editar(self, nombre, descripcion, fecha_vencimiento):
        #edicion de los atributos de la tarea
        self.nombre = nombre 
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento

    def eliminar(self):
        del self #elimina la instancia de tarea