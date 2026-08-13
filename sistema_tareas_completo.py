from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Bloque 1: modelo de datos
# ---------------------------------------------------------------------------

PRIORIDADES = {1: "alta", 2: "media", 3: "baja"}
ESTADOS = ("pendiente", "en_progreso", "completada")


@dataclass
class Tarea:
    id: int
    descripcion: str
    prioridad: int  # 1 = alta, 2 = media, 3 = baja
    tiempo: float  # valor numerico para desempatar/ordenar (p.ej. dias restantes)
    estado: str = "pendiente"

    def __str__(self) -> str:
        nombre_prioridad = PRIORIDADES.get(self.prioridad, "?")
        return (
            f"[{self.id}] {self.descripcion} "
            f"(prioridad={self.prioridad}/{nombre_prioridad}, "
            f"tiempo={self.tiempo}, estado={self.estado})"
        )


# ---------------------------------------------------------------------------
# Bloque 2: lista enlazada
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Bloque 3: cola FIFO y pila LIFO
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Bloque 4: algoritmos de ordenamiento
# ---------------------------------------------------------------------------

def _clave(tarea):
    """Orden: primero prioridad (1=alta primero), y en empate, por tiempo."""
    return (tarea.prioridad, tarea.tiempo)


def bubble_sort(tareas):
    """Burbuja. Complejidad: O(n^2) peor/promedio, O(n) mejor caso (ya ordenada)."""
    lista = list(tareas)
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if _clave(lista[j]) > _clave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return lista


def insertion_sort(tareas):
    """Insercion. Complejidad: O(n^2) peor caso, O(n) mejor caso (casi ordenada)."""
    lista = list(tareas)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and _clave(lista[j]) > _clave(actual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


def selection_sort(tareas):
    """Seleccion. Complejidad: O(n^2) en todos los casos."""
    lista = list(tareas)
    n = len(lista)
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if _clave(lista[j]) < _clave(lista[indice_menor]):
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista


def quicksort(tareas):
    """Quicksort (opcional). Complejidad: O(n log n) promedio, O(n^2) peor caso."""
    lista = list(tareas)
    _quicksort(lista, 0, len(lista) - 1)
    return lista


def _quicksort(lista, inicio, fin):
    if inicio < fin:
        indice_pivote = _particionar(lista, inicio, fin)
        _quicksort(lista, inicio, indice_pivote - 1)
        _quicksort(lista, indice_pivote + 1, fin)


def _particionar(lista, inicio, fin):
    pivote = _clave(lista[fin])
    i = inicio - 1
    for j in range(inicio, fin):
        if _clave(lista[j]) <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1


# ---------------------------------------------------------------------------
# Bloque 5: algoritmos de busqueda
# ---------------------------------------------------------------------------

def busqueda_lineal_por_id(tareas, id_tarea):
    """Busqueda lineal. Complejidad: O(n). No requiere que la lista este ordenada."""
    for tarea in tareas:
        if tarea.id == id_tarea:
            return tarea
    return None


def busqueda_binaria_por_id(tareas_ordenadas_por_id, id_tarea):
    """Busqueda binaria. Complejidad: O(log n). Requiere lista ordenada por id."""
    inicio, fin = 0, len(tareas_ordenadas_por_id) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        id_actual = tareas_ordenadas_por_id[medio].id
        if id_actual == id_tarea:
            return tareas_ordenadas_por_id[medio]
        if id_actual < id_tarea:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


# ---------------------------------------------------------------------------
# Bloque 6: programa principal
# ---------------------------------------------------------------------------

ALGORITMOS = {
    "1": ("Bubble sort", bubble_sort),
    "2": ("Insertion sort", insertion_sort),
    "3": ("Selection sort", selection_sort),
    "4": ("Quicksort", quicksort),
}


class GestorTareas:
    def __init__(self):
        self.tareas = ListaEnlazada()
        self.siguiente_id = 1

    def agregar_tarea(self, descripcion, prioridad, tiempo):
        tarea = Tarea(self.siguiente_id, descripcion, prioridad, tiempo)
        self.tareas.insertar_al_final(tarea)
        self.siguiente_id += 1
        return tarea

    def procesar_fifo(self):
        cola = Cola()
        for tarea in self.tareas:
            cola.encolar(tarea)
        orden = []
        while not cola.esta_vacia():
            orden.append(cola.desencolar())
        return orden

    def procesar_lifo(self):
        pila = Pila()
        for tarea in self.tareas:
            pila.apilar(tarea)
        orden = []
        while not pila.esta_vacia():
            orden.append(pila.desapilar())
        return orden

    def planificar_por_prioridad(self, algoritmo):
        return algoritmo(self.tareas.a_lista())

    def buscar(self, id_tarea, metodo="lineal"):
        if metodo == "lineal":
            return busqueda_lineal_por_id(self.tareas.a_lista(), id_tarea)
        ordenadas_por_id = sorted(self.tareas.a_lista(), key=lambda t: t.id)
        return busqueda_binaria_por_id(ordenadas_por_id, id_tarea)


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un numero valido.")


def menu():
    gestor = GestorTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1) Agregar tarea")
        print("2) Ver tareas (orden de ingreso)")
        print("3) Procesar modo FIFO (pendientes)")
        print("4) Procesar modo LIFO (urgencias)")
        print("5) Planificar por prioridad (ordenar)")
        print("6) Buscar tarea por id")
        print("7) Cambiar estado de una tarea")
        print("0) Salir")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            descripcion = input("Descripcion: ").strip()
            prioridad = pedir_entero("Prioridad (1=alta, 2=media, 3=baja): ")
            tiempo = pedir_entero("Tiempo estimado (numero, para desempate): ")
            tarea = gestor.agregar_tarea(descripcion, prioridad, tiempo)
            print(f"Tarea agregada: {tarea}")

        elif opcion == "2":
            if len(gestor.tareas) == 0:
                print("No hay tareas.")
            for tarea in gestor.tareas:
                print(tarea)

        elif opcion == "3":
            for tarea in gestor.procesar_fifo():
                print(tarea)

        elif opcion == "4":
            for tarea in gestor.procesar_lifo():
                print(tarea)

        elif opcion == "5":
            print("Algoritmos disponibles:")
            for clave, (nombre, _) in ALGORITMOS.items():
                print(f"{clave}) {nombre}")
            eleccion = input("Elige un algoritmo: ").strip()
            if eleccion not in ALGORITMOS:
                print("Opcion invalida.")
                continue
            nombre, algoritmo = ALGORITMOS[eleccion]
            ordenadas = gestor.planificar_por_prioridad(algoritmo)
            print(f"Tareas ordenadas con {nombre}:")
            for tarea in ordenadas:
                print(tarea)

        elif opcion == "6":
            id_tarea = pedir_entero("Id a buscar: ")
            metodo = input("Metodo (lineal/binaria): ").strip().lower()
            if metodo not in ("lineal", "binaria"):
                metodo = "lineal"
            resultado = gestor.buscar(id_tarea, metodo)
            print(resultado if resultado else "Tarea no encontrada.")

        elif opcion == "7":
            id_tarea = pedir_entero("Id de la tarea: ")
            tarea = gestor.tareas.buscar_por_id(id_tarea)
            if tarea is None:
                print("Tarea no encontrada.")
                continue
            print(f"Estados posibles: {', '.join(ESTADOS)}")
            nuevo_estado = input("Nuevo estado: ").strip()
            if nuevo_estado in ESTADOS:
                tarea.estado = nuevo_estado
                print(f"Actualizado: {tarea}")
            else:
                print("Estado invalido.")

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu()
