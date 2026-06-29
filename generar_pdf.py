from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


def generar():
    doc = SimpleDocTemplate(
        "reporte_algoritmos.pdf",
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    titulo = ParagraphStyle("titulo", fontSize=18, alignment=TA_CENTER, spaceAfter=6,
                             textColor=colors.HexColor("#1a1a2e"), fontName="Helvetica-Bold")
    subtitulo = ParagraphStyle("subtitulo", fontSize=11, alignment=TA_CENTER, spaceAfter=20,
                                textColor=colors.HexColor("#555555"), fontName="Helvetica")
    h1 = ParagraphStyle("h1", fontSize=13, spaceBefore=16, spaceAfter=6,
                         textColor=colors.HexColor("#1a1a2e"), fontName="Helvetica-Bold")
    h2 = ParagraphStyle("h2", fontSize=11, spaceBefore=10, spaceAfter=4,
                         textColor=colors.HexColor("#2e4057"), fontName="Helvetica-Bold")
    cuerpo = ParagraphStyle("cuerpo", fontSize=10, spaceAfter=6, leading=14,
                             alignment=TA_JUSTIFY, fontName="Helvetica")
    codigo = ParagraphStyle("codigo", fontSize=8.5, spaceAfter=4, leading=13,
                             fontName="Courier", backColor=colors.HexColor("#f4f4f4"),
                             leftIndent=12, rightIndent=12, spaceBefore=4)

    story = []

    # Portada
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Métodos de Ordenamiento y Búsqueda", titulo))
    story.append(Paragraph("Documentación del código — Python", subtitulo))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc")))
    story.append(Spacer(1, 0.2 * inch))

    # 1. Descripción general
    story.append(Paragraph("1. Descripción General", h1))
    story.append(Paragraph(
        "El programa implementa cuatro algoritmos de ordenamiento y dos de búsqueda. "
        "Está organizado en funciones independientes, una por algoritmo, y cuenta con un menú "
        "interactivo que permite al usuario generar datos aleatorios, comparar dos algoritmos "
        "de ordenamiento y ejecutar búsquedas cronometradas.", cuerpo))

    # 2. Estructura del programa
    story.append(Paragraph("2. Estructura del Programa", h1))
    modulos = [
        ["Sección", "Qué hace"],
        ["generar_datos(n)", "Genera N números enteros aleatorios"],
        ["COMPLEJIDAD", "Diccionario con Big O de cada algoritmo"],
        ["bubble_sort / insertion_sort\nselection_sort / merge_sort", "Algoritmos de ordenamiento"],
        ["busqueda_lineal / busqueda_binaria", "Algoritmos de búsqueda"],
        ["medir_tiempo(func, *args)", "Cronometra cualquier función"],
        ["menu_ordenamiento(datos)", "Menú para elegir y comparar dos algoritmos"],
        ["menu_busqueda(datos)", "Ejecuta ambas búsquedas automáticamente"],
        ["menu_principal()", "Menú principal que controla el flujo"],
    ]
    t = Table(modulos, colWidths=[2.8 * inch, 3.8 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Courier"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)

    # 3. Generación de datos
    story.append(Paragraph("3. Generación de Datos", h1))
    story.append(Paragraph(
        "La función <b>generar_datos(n)</b> recibe el tamaño N y devuelve una lista de N "
        "enteros aleatorios. El rango de valores es de 1 a N×10, de modo que escala con el "
        "tamaño del arreglo.", cuerpo))
    story.append(Paragraph("def generar_datos(n):", codigo))
    story.append(Paragraph("    return [random.randint(1, n * 10) for _ in range(n)]", codigo))
    story.append(Paragraph(
        "El usuario puede ingresar cualquier N (100, 1000, 10000). Los números se muestran "
        "en pantalla tal como se generaron, sin ningún orden.", cuerpo))

    # 4. Algoritmos de ordenamiento
    story.append(Paragraph("4. Algoritmos de Ordenamiento", h1))
    story.append(Paragraph(
        "Todos los algoritmos reciben el arreglo original, hacen una copia interna "
        "(<b>a = arr[:]</b>) para no modificarlo, cuentan sus pasadas y devuelven "
        "el arreglo ordenado junto con el conteo de pasadas.", cuerpo))

    story.append(Paragraph("4.1 Bubble Sort", h2))
    story.append(Paragraph(
        "Compara pares de elementos vecinos e intercambia los que estén en orden incorrecto. "
        "Repite el proceso N veces. En cada pasada el elemento más grande 'burbujea' "
        "hacia el final.", cuerpo))
    story.append(Paragraph("for i in range(n):         # pasada exterior", codigo))
    story.append(Paragraph("    for j in range(0, n-i-1):", codigo))
    story.append(Paragraph("        if a[j] > a[j+1]:", codigo))
    story.append(Paragraph("            a[j], a[j+1] = a[j+1], a[j]", codigo))

    story.append(Paragraph("4.2 Insertion Sort", h2))
    story.append(Paragraph(
        "Toma cada elemento desde la posición 1 y lo inserta en la posición correcta "
        "dentro de la parte izquierda ya ordenada, desplazando elementos hacia la derecha "
        "mientras sean mayores.", cuerpo))
    story.append(Paragraph("for i in range(1, len(a)):", codigo))
    story.append(Paragraph("    key = a[i]", codigo))
    story.append(Paragraph("    while j >= 0 and a[j] > key:", codigo))
    story.append(Paragraph("        a[j+1] = a[j]   # desplaza hacia la derecha", codigo))

    story.append(Paragraph("4.3 Selection Sort", h2))
    story.append(Paragraph(
        "En cada pasada recorre todo el subarreglo no ordenado para encontrar el elemento "
        "mínimo y lo coloca en su posición definitiva al inicio. Siempre realiza N pasadas "
        "sin importar el estado del arreglo.", cuerpo))
    story.append(Paragraph("for i in range(n):", codigo))
    story.append(Paragraph("    min_idx = i", codigo))
    story.append(Paragraph("    for j in range(i+1, n):", codigo))
    story.append(Paragraph("        if a[j] < a[min_idx]: min_idx = j", codigo))
    story.append(Paragraph("    a[i], a[min_idx] = a[min_idx], a[i]", codigo))

    story.append(Paragraph("4.4 Merge Sort", h2))
    story.append(Paragraph(
        "Algoritmo recursivo. Divide el arreglo en dos mitades, ordena cada mitad "
        "recursivamente y luego las fusiona en orden. Es el más eficiente de los cuatro. "
        "Las pasadas se cuentan en cada llamada recursiva con un acumulador compartido "
        "(<b>_pasadas</b>).", cuerpo))
    story.append(Paragraph("mid = len(arr) // 2", codigo))
    story.append(Paragraph("left  = merge_sort(arr[:mid], _pasadas)", codigo))
    story.append(Paragraph("right = merge_sort(arr[mid:], _pasadas)", codigo))
    story.append(Paragraph("# luego fusiona left y right en orden", codigo))

    # 5. Tabla de complejidades
    story.append(Paragraph("5. Tabla de Complejidades (Big O)", h1))
    tabla_comp = [
        ["Algoritmo", "Mejor caso", "Caso promedio", "Peor caso"],
        ["Bubble Sort",    "O(n)",      "O(n²)",        "O(n²) — orden inverso"],
        ["Insertion Sort", "O(n)",      "O(n²)",        "O(n²) — orden inverso"],
        ["Selection Sort", "O(n²)",     "O(n²)",        "O(n²) — siempre igual"],
        ["Merge Sort",     "O(n log n)","O(n log n)",   "O(n log n) — siempre igual"],
    ]
    tc = Table(tabla_comp, colWidths=[1.6 * inch, 1.2 * inch, 1.4 * inch, 2.4 * inch])
    tc.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2e4057")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(tc)

    # 6. Algoritmos de búsqueda
    story.append(Paragraph("6. Algoritmos de Búsqueda", h1))
    story.append(Paragraph(
        "Ambas búsquedas se ejecutan automáticamente al elegir la opción 3 del menú. "
        "Se elige un valor aleatorio del arreglo como objetivo y se mide el tiempo de cada método.", cuerpo))

    story.append(Paragraph("6.1 Búsqueda Lineal", h2))
    story.append(Paragraph(
        "Recorre el arreglo elemento por elemento desde el inicio hasta encontrar el objetivo. "
        "Opera sobre el arreglo sin ordenar. En el peor caso recorre todos los elementos: <b>O(n)</b>.", cuerpo))
    story.append(Paragraph("for i, val in enumerate(arr):", codigo))
    story.append(Paragraph("    if val == objetivo: return i", codigo))

    story.append(Paragraph("6.2 Búsqueda Binaria", h2))
    story.append(Paragraph(
        "Requiere que el arreglo esté ordenado. Divide el rango de búsqueda a la mitad en "
        "cada paso comparando el elemento central con el objetivo. Mucho más rápida: <b>O(log n)</b>.", cuerpo))
    story.append(Paragraph("while izq <= der:", codigo))
    story.append(Paragraph("    mid = (izq + der) // 2", codigo))
    story.append(Paragraph("    if arr[mid] == objetivo: return mid", codigo))
    story.append(Paragraph("    elif arr[mid] < objetivo: izq = mid + 1", codigo))
    story.append(Paragraph("    else: der = mid - 1", codigo))

    # 7. Cronometraje
    story.append(Paragraph("7. Cronometraje", h1))
    story.append(Paragraph(
        "La función <b>medir_tiempo</b> es genérica: recibe cualquier función y sus argumentos, "
        "registra el tiempo antes y después de ejecutarla usando <b>time.perf_counter()</b> "
        "(el reloj de mayor precisión disponible en Python, con resolución de nanosegundos) "
        "y devuelve el resultado junto con el tiempo transcurrido en segundos.", cuerpo))
    story.append(Paragraph("def medir_tiempo(func, *args):", codigo))
    story.append(Paragraph("    inicio = time.perf_counter()", codigo))
    story.append(Paragraph("    resultado = func(*args)", codigo))
    story.append(Paragraph("    fin = time.perf_counter()", codigo))
    story.append(Paragraph("    return resultado, fin - inicio", codigo))

    # 8. Menú
    story.append(Paragraph("8. Menú Principal", h1))
    story.append(Paragraph(
        "El menú principal tiene 4 opciones. El programa no permite ordenar ni buscar "
        "sin haber generado datos primero.", cuerpo))
    opciones_menu = [
        ["Opción", "Acción"],
        ["1", "Genera N números aleatorios y los muestra en pantalla"],
        ["2", "Pide elegir dos algoritmos de ordenamiento y muestra resultados de cada uno"],
        ["3", "Ejecuta Búsqueda Lineal y Binaria automáticamente y muestra tiempos"],
        ["4", "Termina el programa"],
    ]
    tm = Table(opciones_menu, colWidths=[0.8 * inch, 5.8 * inch])
    tm.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(tm)

    story.append(Spacer(1, 0.3 * inch))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc")))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("Documentación generada automáticamente — algoritmos.py", subtitulo))

    doc.build(story)
    print("PDF generado: reporte_algoritmos.pdf")


if __name__ == "__main__":
    generar()
