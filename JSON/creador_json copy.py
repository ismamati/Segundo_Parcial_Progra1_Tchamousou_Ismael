import json
import random

def generar_votos():
    votos_rojo = random.randint(1, 5)  
    votos_azul = 5 - votos_rojo       
    votos = ["Rojo"] * votos_rojo + ["Azul"] * votos_azul
    random.shuffle(votos)
    return votos

def crear_json(ruta_json):
    niveles_programacion = {
    "nivel_1": [
                {"pregunta": "¿Qué es una variable?",
                "opciones": ["Espacio en memoria", "Un programa"],
                "votos": generar_votos(), 
                "puntuacion": 100
                },
                {
                    "pregunta": "¿Cuál es el resultado de 2 + 2?",
                    "opciones": ["4","22"],
                    "votos": generar_votos(), 
                    "puntuacion": 100
                },
                {
                    "pregunta": "¿Qué lenguaje utiliza 'print' para mostrar texto?",
                    "opciones": ["Python","HTML"],
                    "votos": generar_votos(), 
                    "puntuacion": 100
                },
                {
                    "pregunta": "¿Qué es un bucle?",
                    "opciones": ["Repetición de código","Un error"],
                    "votos": generar_votos(), 
                    "puntuacion": 100
                },
                {
                    "pregunta": "¿Cuál es el operador de asignación?",
                    "opciones": ["=","=="],
                    "votos": generar_votos(), 
                    "puntuacion": 100
                }
            ],
            "nivel_2": [
                {
                    "pregunta": "¿Qué estructura se usa para almacenar múltiples valores?",
                    "opciones": ["Lista","Condición"],
                    "votos": generar_votos(), 
                    "puntuacion": 200
                },
                {
                    "pregunta": "¿Qué significa 'if' en programación?",
                    "opciones": ["Condición","Bucle"],
                    "votos": generar_votos(), 
                    "puntuacion": 200
                },
                {
                    "pregunta": "¿Cómo se declara una función en Python?",
                    "opciones": ["def","function"],
                    "votos": generar_votos(), 
                    "puntuacion": 200
                },
                {
                    "pregunta": "¿Cuál es el resultado de '3 * 3'?",
                    "opciones": ["9", "6"],
                    "votos": generar_votos(), 
                    "puntuacion": 200
                },
                {
                    "pregunta": "¿Cual es una forma de ordenamiento?",  
                    "opciones": ["bubble","circle"],
                    "votos": generar_votos(),             
                    "puntuacion": 200
                }
            ],
            "nivel_3": [
                {
                    "pregunta": "¿Qué es una clase en programación?",
                    "opciones": ["Molde para objetos","Una función"],
                    "votos": generar_votos(), 
                    "puntuacion": 300
                },
                {
                    "pregunta": "¿Qué significa 'return' en una función?",
                    "opciones": ["Devuelve un valor","Finaliza el programa"],
                    "votos": generar_votos(), 
                    "puntuacion": 300
                },
                {
                    "pregunta": "¿Cómo se accede a un elemento en una lista?",
                    "opciones": ["Por índice","Con una clave"],
                    "votos": generar_votos(), 
                    "puntuacion": 300
                },
                {
                    "pregunta": "¿Qué es una API?",
                    "opciones": ["Interfaz de programación","Un compilador"],
                    "votos": generar_votos(), 
                    "puntuacion": 300
                },
                {
                    "pregunta": "¿Qué se usa para iterar sobre una lista?",
                    "opciones": ["for","if" ],
                    "votos": generar_votos(), 
                    "puntuacion": 300
                }
        ]
    }
    ruta_archivo_programacion = ruta_json
    with open(ruta_archivo_programacion, "w", encoding="utf-8") as archivo:
        json.dump(niveles_programacion, archivo, indent=4, ensure_ascii=False)

