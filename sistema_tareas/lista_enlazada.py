class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class ListaEnlazada:
    """Lista simplemente enlazada que guarda objetos Tarea."""

    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def insertar_al_final(self, tarea):
        nuevo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano += 1

    def insertar_al_inicio(self, tarea):
        nuevo = Nodo(tarea)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1

    def buscar_por_id(self, id_tarea):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.id == id_tarea:
                return actual.tarea
            actual = actual.siguiente
        return None

    def eliminar_por_id(self, id_tarea) -> bool:
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.tarea.id == id_tarea:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def a_lista(self) -> list:
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.tarea)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return self.tamano

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.tarea
            actual = actual.siguiente
