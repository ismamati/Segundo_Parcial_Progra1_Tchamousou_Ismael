import random

class Comodines:
    def __init__(self):
        self.next_disponible = True
        self.half_disponible = True
        self.reload_disponible = True


    
    def usar_next(self, gestor_preguntas):
        if not self.next_disponible:
            raise Exception("Comodín Next ya fue usado.")
        self.next_disponible = False
        gestor_preguntas.siguiente_pregunta()

    def usar_half(self, votos):
        if not self.half_disponible:
            raise Exception("Comodín Half ya fue usado.")
        self.half_disponible = False
        return random.sample(votos, min(2, len(votos)))

    def usar_reload(self, gestor_preguntas):
        if not self.reload_disponible:
            raise Exception("Comodín Reload ya fue usado.")
        self.reload_disponible = False
        gestor_preguntas.cambiar_pregunta()