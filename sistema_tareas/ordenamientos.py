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
