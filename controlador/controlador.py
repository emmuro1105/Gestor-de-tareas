from modelo.pendiente import Pendiente  #importar la clase "Pendiente" del modelo
class Controlador:
    def __init__(self):
        self.pendiente = Pendiente()  #instancia de la clase "Pendiente"

    #añade una tarea a la lista
    def agregar_tarea(self, nombre, descripcion, fecha_vencimiento, estado):
        #llama al método agregar_tarea de la clase "Pendiente"
        self.pendiente.agregar_tarea(nombre, descripcion, fecha_vencimiento, estado)
    #elimina una tarea de la lista
    def eliminar_tarea(self, index):
        #llama al método eliminar_tarea de la clase "Pendiente"
        self.pendiente.eliminar_tarea(index)

    #cambia el estado de una tarea de la lista
    def cambiar_estado_tarea(self, index):
        #llama al método cambiar_estado_tarea de la clase "Pendiente"
        self.pendiente.cambiar_estado_tarea(index)

    #lista todas las tareas
    def listar_tareas(self):
        return self.pendiente.listar_tareas()

