import json
from JSON.creador_json import crear_json
import random


ruta_archivo_programacion = "niveles_preguntas_programacion.json"

crear_json(ruta_archivo_programacion)

with open(ruta_archivo_programacion, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

nivel_1 = datos["nivel_1"]
nivel_2 = datos["nivel_2"]
nivel_3 = datos["nivel_3"]


class GestorPreguntas:
    def __init__(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        self.nivel_actual = 1
        self.preguntas_actuales = self.datos[f"nivel_{self.nivel_actual}"]
        self.indice_actual = 0

    def obtener_pregunta(self):

        pregunta = self.preguntas_actuales[self.indice_actual]
        print(pregunta)
        if self.indice_actual < len(self.preguntas_actuales):
            pregunta = self.preguntas_actuales[self.indice_actual]
            return pregunta["pregunta"], pregunta["opciones"]
        
        return None, None

    def responder(self, respuesta):
        rojos = 0
        azules = 0
        if self.indice_actual < len(self.preguntas_actuales):
            pregunta = self.preguntas_actuales[self.indice_actual]
            votos = pregunta["votos"]

            for opciones in votos:
                if opciones == "Rojo":
                    rojos += 1
                else:
                    azules += 1
            if azules > rojos:
                respuesta_correcta = pregunta["opciones"][1]
                print(respuesta_correcta)
            else:
                respuesta_correcta = pregunta["opciones"][0]
                print(respuesta_correcta)

            if respuesta == respuesta_correcta:
                self.indice_actual += 1
                return True, f"¡Correcto! Ganaste {pregunta['puntuacion']} puntos."
            else:
                return False, 

        return False, 

    def cambiar_nivel(self, nuevo_nivel):
        if f"nivel_{nuevo_nivel}" in self.datos:
            self.nivel_actual = nuevo_nivel
            self.preguntas_actuales = self.datos[f"nivel_{nuevo_nivel}"]
            self.indice_actual = 0
            return True
        return False


    def reiniciar(self):
        self.nivel_actual = 1
        self.preguntas_actuales = self.datos["nivel_1"]
        self.indice_actual = 0
        random.shuffle(self.preguntas_actuales)
