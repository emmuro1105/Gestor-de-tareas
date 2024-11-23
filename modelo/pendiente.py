from modelo.tarea import Tarea  #importar la clase "Tarea" del modelo

class Pendiente:
    def __init__(self):
        self.tareas = []  #inicializa una lista vacía para almacenar tareas

    def agregar_tarea(self, nombre, descripcion, fecha_vencimiento, estado):
        nueva_tarea = Tarea(nombre, descripcion, fecha_vencimiento, estado)  #crea una nueva tarea
        self.tareas.append(nueva_tarea)  #añade la nueva tarea a la lista

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            del self.tareas[index]  #elimina la tarea en el índice especificado

    def cambiar_estado_tarea(self, index):
        if 0 <= index < len(self.tareas):
            tarea = self.tareas[index]
            if tarea.estado == "pendiente":
                tarea.estado = "completada"  #cambia el estado de la tarea a "completada"
            else:
                tarea.estado = "pendiente"  #cambia el estado de la tarea a "pendiente"

    def listar_tareas(self):
        return self.tareas  #retorna la lista creada
