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
