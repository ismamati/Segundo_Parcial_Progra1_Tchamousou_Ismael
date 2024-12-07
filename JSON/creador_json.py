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
            ]
    }
    ruta_archivo_programacion = ruta_json
    with open(ruta_archivo_programacion, "w", encoding="utf-8") as archivo:
        json.dump(niveles_programacion, archivo, indent=4, ensure_ascii=False)

