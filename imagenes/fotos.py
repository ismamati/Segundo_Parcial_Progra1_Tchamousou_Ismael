import pygame as pg

pg.init()

imagen = pg.image.load("./fotos/FONDO.png")
imagen = pg.transform.scale(imagen, (800, 600))

fondo = pg.image.load("./fotos/Nombre.jpg")
fondo = pg.transform.scale(fondo, (800, 600))

preguntas = pg.image.load("./fotos/preguntas.jpg")
preguntas = pg.transform.scale(preguntas, (800, 600))
