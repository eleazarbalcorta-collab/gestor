import random
import time


def generar_datos(n):
    return [random.randint(1, n * 10) for _ in range(n)]


# --- Ordenamiento ---

COMPLEJIDAD = {
    "Bubble Sort":    {"promedio": "O(n²)", "peor": "O(n²)  — arreglo en orden inverso"},
    "Insertion Sort": {"promedio": "O(n²)", "peor": "O(n²)  — arreglo en orden inverso"},
    "Selection Sort": {"promedio": "O(n²)", "peor": "O(n²)  — siempre recorre todo"},
    "Merge Sort":     {"promedio": "O(n log n)", "peor": "O(n log n) — siempre igual"},
}


def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    pasadas = 0
    for i in range(n):
        pasadas += 1
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, pasadas


def insertion_sort(arr):
    a = arr[:]
    pasadas = 0
    for i in range(1, len(a)):
        pasadas += 1
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a, pasadas


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    pasadas = 0
    for i in range(n):
        pasadas += 1
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, pasadas


def merge_sort(arr, _pasadas=None):
    if _pasadas is None:
        _pasadas = [0]
    if len(arr) <= 1:
        return arr[:], _pasadas
    _pasadas[0] += 1
    mid = len(arr) // 2
    left, _ = merge_sort(arr[:mid], _pasadas)
    right, _ = merge_sort(arr[mid:], _pasadas)
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, _pasadas


# --- Búsqueda ---

def busqueda_lineal(arr, objetivo):
    for i, val in enumerate(arr):
        if val == objetivo:
            return i
    return -1


def busqueda_binaria(arr, objetivo):
    izq, der = 0, len(arr) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1


# --- Cronometraje ---

def medir_tiempo(func, *args):
    inicio = time.perf_counter()
    resultado = func(*args)
    fin = time.perf_counter()
    return resultado, fin - inicio


# --- Menú ---

def menu_ordenamiento(datos):
    opciones = {
        "1": ("Bubble Sort",     bubble_sort),
        "2": ("Insertion Sort",  insertion_sort),
        "3": ("Selection Sort",  selection_sort),
        "4": ("Merge Sort",      merge_sort),
    }
    print("\n  1. Bubble Sort")
    print("  2. Insertion Sort")
    print("  3. Selection Sort")
    print("  4. Merge Sort")
    op1 = input("Elige primer algoritmo: ").strip()
    op2 = input("Elige segundo algoritmo: ").strip()
    if op1 not in opciones or op2 not in opciones:
        print("Opción inválida.")
        return

    for op in (op1, op2):
        nombre, func = opciones[op]
        (_, pasadas_raw), t = medir_tiempo(func, datos)
        pasadas = pasadas_raw[0] if isinstance(pasadas_raw, list) else pasadas_raw
        info = COMPLEJIDAD[nombre]
        print(f"\n--- Resultados: {nombre} ---")
        print(f"  Tiempo de ejecución : {t:.6f} segundos")
        print(f"  Complejidad promedio: {info['promedio']}")
        print(f"  Peor caso           : {info['peor']}")
        print(f"  Pasadas realizadas  : {pasadas}")


def menu_busqueda(datos):
    ordenado = sorted(datos)
    objetivo = random.choice(datos)
    print(f"\nBuscando el valor: {objetivo}")

    _, t1 = medir_tiempo(busqueda_lineal, datos, objetivo)
    print(f"  Búsqueda Lineal  -> {t1:.6f} s")

    _, t2 = medir_tiempo(busqueda_binaria, ordenado, objetivo)
    print(f"  Búsqueda Binaria -> {t2:.6f} s  (sobre arreglo ordenado)")


def menu_principal():
    datos = []
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Generar datos aleatorios")
        print("2. Ejecutar algoritmo de ordenamiento")
        print("3. Ejecutar algoritmo de búsqueda")
        print("4. Salir")
        op = input("Elige opción: ").strip()

        if op == "1":
            n = input("Tamaño N (ej. 100, 1000, 10000): ").strip()
            if not n.isdigit():
                print("Ingresa un número válido.")
                continue
            datos = generar_datos(int(n))
            print(f"\nSe generaron {len(datos)} números aleatorios:")
            print(datos)

        elif op == "2":
            if not datos:
                print("Primero genera datos (opción 1).")
                continue
            menu_ordenamiento(datos)

        elif op == "3":
            if not datos:
                print("Primero genera datos (opción 1).")
                continue
            menu_busqueda(datos)

        elif op == "4":
            print("Saliendo.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()
