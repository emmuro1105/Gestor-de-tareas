class Categoria: #clase para clasificar las tareas creadas (funcionalidad sin añadir)
    def __init__(self, nombre, descripcion):
        self.nombre = nombre #inicia el nombre de la categoria
        self.descripcion = descripcion #inicia la descripcion de la categoria

    def agregar_categoria(self, nombre, descripcion):
        return Categoria(nombre, descripcion) #crea y retorna la instacia nueva de categoria
