import time

def imprimir_linea():
    print("===============================================================")

def imprimir_titulo(titulo):
    imprimir_linea()
    print(titulo)
    imprimir_linea()

def mostrar_pregunta(num_pregunta, pregunta, opciones):
    imprimir_linea()
    print(f"Pregunta {num_pregunta}:")
    print()
    print(pregunta)
    print()
    for i, opcion in opciones.items():
        print(f"{i}. {opcion}")
    print()

def imprimir_resultados(respuestas_correctas_totales, total_preguntas):
    imprimir_linea()
    print("RESULTADOS")
    imprimir_linea()
    print()
    print(f"Preguntas respondidas correctamente: {respuestas_correctas_totales}")
    print(f"Preguntas respondidas incorrectamente: {total_preguntas - respuestas_correctas_totales}")
    print()
    time.sleep(1)  # Pausa de 1 segundo

def imprimir_mensaje_aprobado():
    print("¡Felicidades, has aprobado el examen!")
    print()

def imprimir_mensaje_reprobado():
    print("Lo siento, no has aprobado el examen. Estudia un poco más y vuelve a intentarlo.")
    print()

def mostrar_resultados_finales(respuestas_correctas_totales, total_preguntas, puntuacion):
    imprimir_linea()
    print("RESULTADOS FINALES")
    imprimir_linea()
    print()
    print("Preguntas respondidas correctamente: {}".format(respuestas_correctas_totales))
    print("Preguntas respondidas incorrectamente: {}".format(total_preguntas - respuestas_correctas_totales))
    print("Puntuación obtenida: {}%".format(puntuacion))
    print()
    print("Gracias por realizar el examen de Markdown. ¡Hasta luego!")
    print()
    input("Presiona Enter para salir...")

# Preguntas y respuestas
preguntas = {
    1: {
        'pregunta': "¿Cuál es la extensión de archivo utilizada en Markdown?",
        'opciones': {
            1: ".txt",
            2: ".md",
            3: ".docx",
            4: ".html"
        },
        'respuesta_correcta': 2
    },
    2: {
        'pregunta': "¿Cuál es el símbolo utilizado para los encabezados en Markdown?",
        'opciones': {
            1: "*",
            2: "#",
            3: "%",
            4: "@"
        },
        'respuesta_correcta': 2
    },
    3: {
        'pregunta': "¿Cuál es la sintaxis para crear un enlace en Markdown?",
        'opciones': {
            1: "[enlace](url)",
            2: "{enlace}(url)",
            3: "(url)enlace",
            4: "<enlace>(url)"
        },
        'respuesta_correcta': 1
    },
    4: {
        'pregunta': "¿Cómo se crea una lista numerada en Markdown?",
        'opciones': {
            1: "- Item 1\n   - Item 2",
            2: "* Item 1\n   * Item 2",
            3: "1. Item 1\n   2. Item 2",
            4: "> Item 1\n   > Item 2"
        },
        'respuesta_correcta': 3
    },
    5: {
        'pregunta': "¿Cómo se resalta un código en Markdown?",
        'opciones': {
            1: "`código`",
            2: "```código```",
            3: "[código]",
            4: "(código)"
        },
        'respuesta_correcta': 2
    },
    6: {
        'pregunta': "¿Cuál es la sintaxis para incluir una imagen en Markdown?",
        'opciones': {
            1: "[imagen](ruta)",
            2: "{imagen}(ruta)",
            3: "![imagen](ruta)",
            4: "<imagen>(ruta)"
        },
        'respuesta_correcta': 3
    },
    7: {
        'pregunta': "¿Cuál es la sintaxis para crear una tabla en Markdown?",
        'opciones': {
            1: "| Columna 1 | Columna 2 |\n| --------- | --------- |\n| Valor 1   | Valor 2   |",
            2: "| Columna 1 | Columna 2 |\n| --------- | --------- |\n| Valor 1   | Valor 2   |",
            3: "| Columna 1 | Columna 2 |\n| --------- | --------- |\n| Valor 1   | Valor 2   |",
            4: "| Columna 1 | Columna 2 |\n| --------- | --------- |\n| Valor 1   | Valor 2   |"
        },
        'respuesta_correcta': 1
    },
    8: {
        'pregunta': "¿Cuál es la sintaxis para crear un bloque de cita en Markdown?",
        'opciones': {
            1: "[cita] Texto de la cita [/cita]",
            2: "> Texto de la cita",
            3: "* Texto de la cita *",
            4: "<cita> Texto de la cita </cita>"
        },
        'respuesta_correcta': 2
    },
    9: {
        'pregunta': "¿Cuál es la sintaxis para crear una línea horizontal en Markdown?",
        'opciones': {
            1: "---",
            2: "===",
            3: "+++",
            4: "***"
        },
        'respuesta_correcta': 1
    },
    10: {
        'pregunta': "¿Cuál es la sintaxis para crear texto en negrita en Markdown?",
        'opciones': {
            1: "*texto*",
            2: "_texto_",
            3: "**texto**",
            4: "--texto--"
        },
        'respuesta_correcta': 3
    }
}

total_preguntas = len(preguntas)
respuestas_correctas_totales = 0
num_pregunta = 1

imprimir_titulo("EXAMEN DE MARKDOWN")
print()
print("Bienvenido al examen de Markdown.")
print("A continuación, se presentan 10 preguntas de opción múltiple.")
print("Por favor, seleccione la opción correcta escribiendo el número correspondiente.")
print()
input("Presiona Enter para comenzar el examen...")

while num_pregunta <= total_preguntas:
    pregunta_actual = preguntas[num_pregunta]
    mostrar_pregunta(num_pregunta, pregunta_actual['pregunta'], pregunta_actual['opciones'])

    respuesta = input("Respuesta: ")
    print()

    # Validar la respuesta
    if respuesta.isdigit() and int(respuesta) == pregunta_actual['respuesta_correcta']:
        respuestas_correctas_totales += 1
        print("Respuesta correcta.")
    else:
        print("Respuesta incorrecta.")

    time.sleep(1)  # Pausa de 1 segundo
    num_pregunta += 1
    input("Presiona Enter para continuar...")

imprimir_titulo("RESULTADOS")
imprimir_resultados(respuestas_correctas_totales, total_preguntas)

# Calcular puntuación y mostrar resultado final
puntuacion = (respuestas_correctas_totales * 100) / total_preguntas

if puntuacion >= 70:
    imprimir_mensaje_aprobado()
else:
    imprimir_mensaje_reprobado()

print()
time.sleep(1)  # Pausa de 1 segundo
input("Presiona Enter para ver tus resultados...")
print()
mostrar_resultados_finales(respuestas_correctas_totales, total_preguntas, puntuacion)
