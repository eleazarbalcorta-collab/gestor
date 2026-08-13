from sistema_tareas.tarea import Tarea, ESTADOS
from sistema_tareas.lista_enlazada import ListaEnlazada
from sistema_tareas.estructuras import Cola, Pila
from sistema_tareas.ordenamientos import bubble_sort, insertion_sort, selection_sort, quicksort
from sistema_tareas.busqueda import busqueda_lineal_por_id, busqueda_binaria_por_id

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
