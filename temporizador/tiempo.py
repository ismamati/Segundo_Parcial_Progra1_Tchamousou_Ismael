import pygame as pg
from main import mostrar_texto

class temporizador():
    def __init__(self):
         self.level_timer = 60
         self.first_last_timer = pg.time.get_ticks()
         self.clock = pg.time.Clock()
         self.info_timer = mostrar_texto(f"Tiempo Restante: {self.level_timer}",100, 50,)
        
    def draw(self):
        self.level.draw()
        self.info_timer.draw()

    def actualizar_timer(self):
        if self.level_timer > 0:
            tiempo_actual = pg.time.get_ticks()
            if tiempo_actual - self.first_last_timer > 1000:
                self.level_timer -= 1
                self.first_last_timer = tiempo_actual