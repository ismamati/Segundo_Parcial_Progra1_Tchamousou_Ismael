import json
import random
from JSON.creador_json import crear_json

class GestorPreguntas:
    def __init__(self, archivo_json):
        crear_json(archivo_json)

        with open(archivo_json, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        self.nivel_actual = 1
        self.preguntas_actuales = self.datos[f"nivel_{self.nivel_actual}"]
        self.indice_actual = 0
        
    def obtener_pregunta(self):

        if self.indice_actual < len(self.preguntas_actuales):
            pregunta = self.preguntas_actuales[self.indice_actual]
            return (
                pregunta["pregunta"],
                pregunta["opciones"],
                pregunta["puntuacion"],
                pregunta["votos"],
            )
        return None, None, None, None

    def responder(self, respuesta):

        if self.indice_actual < len(self.preguntas_actuales):
            pregunta = self.preguntas_actuales[self.indice_actual]
            votos = pregunta["votos"]

            rojos = votos.count("Rojo")
            azules = votos.count("Azul")
            respuesta_correcta = pregunta["opciones"][0] if rojos > azules else pregunta["opciones"][1]

            if respuesta == respuesta_correcta:
                puntuacion = pregunta["puntuacion"]
                self.indice_actual += 1
                return True, puntuacion  
            else:
                return False, 0  

        return False, 0 

    def cambiar_nivel(self, nuevo_nivel):
        if f"nivel_{nuevo_nivel}" in self.datos:
            self.nivel_actual = nuevo_nivel
            self.preguntas_actuales = self.datos[f"nivel_{nuevo_nivel}"]
            self.indice_actual = 0 
            random.shuffle(self.preguntas_actuales) 
            return True
        return False

    def reiniciar(self):
        """
        Reinicia el gestor al nivel 1.
        """
        self.nivel_actual = 1
        self.preguntas_actuales = self.datos["nivel_1"]
        self.indice_actual = 0
        random.shuffle(self.preguntas_actuales)
