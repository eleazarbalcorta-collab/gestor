class NodoSimple:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class Cola:
    """Cola FIFO: procesa primero lo mas antiguo (modo 'pendientes')."""

    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def encolar(self, tarea):
        nuevo = NodoSimple(tarea)
        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamano += 1

    def desencolar(self):
        if self.frente is None:
            return None
        tarea = self.frente.tarea
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return tarea

    def esta_vacia(self) -> bool:
        return self.frente is None

    def __len__(self) -> int:
        return self.tamano


class Pila:
    """Pila LIFO: procesa primero lo ultimo recibido (modo 'urgencias')."""

    def __init__(self):
        self.tope = None
        self.tamano = 0

    def apilar(self, tarea):
        nuevo = NodoSimple(tarea)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamano += 1

    def desapilar(self):
        if self.tope is None:
            return None
        tarea = self.tope.tarea
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return tarea

    def esta_vacia(self) -> bool:
        return self.tope is None

    def __len__(self) -> int:
        return self.tamano
