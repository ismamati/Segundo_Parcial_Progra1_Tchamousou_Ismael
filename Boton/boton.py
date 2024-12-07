import pygame as pg
from extras.extras import BLANCO, fuente


class Boton:
    def __init__(self, texto, x, y, ancho, alto, color, color_hover, accion):
        self.texto = texto
        self.rect = pg.Rect(x, y, ancho, alto)
        self.color = color
        self.color_hover = color_hover
        self. accion = accion

    def dibujar(self, pantalla):
        color_actual = self.color_hover if self.rect.collidepoint(pg.mouse.get_pos()) else self.color
        pg.draw.rect(pantalla, color_actual, self.rect)
        texto_render = fuente.render(self.texto, True, BLANCO)
        pantalla.blit(texto_render, (self.rect.x + 70, self.rect.y + 10))

    def ckick(self):
        return self.rect.collidepoint(pg.mouse.get_pos())
