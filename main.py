import pygame
from puntajes import GestorPuntajes
from preguntas import GestorPreguntas
from extras.extras import BLANCO,NEGRO, ROJO, AZUL,VIOLETA,VERDE, AMARILLO, fuente
from Boton.boton import Boton
from imagenes.fotos import imagen, fondo, preguntas
from Comodines import Comodines
import random

pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Preguntas")

comodines = Comodines()

def mostrar_menu():
    botones = [
        Boton("Jugar", 300, 200, 200, 50, ROJO, (255, 100, 100), conseguir_nombre),
        Boton("Scores", 290, 300, 220, 50, AZUL, (100, 100, 255), ver_puntuaciones),
        Boton("Salir", 300, 400, 200, 50, ROJO, (255, 100, 100), salir_juego),
    ]

    andando = True
    while andando:

        pantalla.blit(imagen, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                for boton in botones:
                    if boton.ckick():
                        boton.accion()

        for boton in botones:
            boton.dibujar(pantalla)

        pygame.display.flip()

def conseguir_nombre():
    """
    Conseguir nombre:

    Esta funcion se utiliza para que al iniciar el juego la persona escriba su nombre y si no escribe nada 
    se llamara anonimo

    """
    nombre = ""
    entrada_activada = True

    while entrada_activada:

        pantalla.blit(fondo, (0, 0))
        mostrar_texto("Escribe tu nombre:", 50, 200)
        mostrar_texto(nombre, 300, 200, AZUL)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    entrada_activada = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) >= 25:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode
                

    iniciar_juego(nombre)

def iniciar_juego(nombre_jugador):
    """_summary_
        la funcion principal en la que se crean todos los botones, tambien
    Args:
        nombre_jugador (_type_): El nombre del jugador que esta jugando en ese momento

    Returns:
        _type_: _description_
    """
    gestor_preguntas = GestorPreguntas("niveles_preguntas_programacion.json")
    gestor_puntajes = GestorPuntajes()
    puntaje_total = 0
    nivel_actual = 1

    jugando = True
    while jugando:

        pantalla.blit(preguntas,(0,0))
        pregunta, opciones, puntuacion, votos = gestor_preguntas.obtener_pregunta()

        if pregunta == None: 
            nivel_actual += 1
            if nivel_actual > 3:
                felicitacion(nombre_jugador, puntaje_total)
                gestor_puntajes.guardar_puntaje(nombre_jugador, puntaje_total)
                return
            gestor_preguntas.cambiar_nivel(nivel_actual)
            continue

        mostrar_texto(f"Nivel {nivel_actual}", 350, 50)
        mostrar_texto(pregunta, 275, 150)

        def crear_responder(opcion_seleccionada):
            """_summary_
                Funcion para responder la pregunta seleccionada, en esta funcion se compara la respuesta
                con la opcion correcta, dando si es correcta la suma de puntos y retornando True, caso
                contrario si se equivoca entramos en otra funcion y retorno false
            Args:
                opcion_seleccionada (_type_): Opcion seleccionada para responder a la pregunta
            """
            def accion():
                    correcto, puntos = gestor_preguntas.responder(opcion_seleccionada)
                    if correcto:
                        nonlocal puntaje_total
                        puntaje_total += puntos
                        return True
                    else:
                        perdiste(nombre_jugador, puntaje_total)
                        gestor_puntajes.guardar_puntaje(nombre_jugador, puntaje_total)
                        return False
            return accion

        botones = [
                Boton(opciones[0], 200, 300, 150, 50, ROJO, (255, 100, 100), crear_responder(opciones[0])),
                Boton(opciones[1], 450, 300, 150, 50, AZUL, (100, 100, 255), crear_responder(opciones[1])),
            ]


        botones_comodines = [
            Boton("", 210, 450, 50, 50, VIOLETA, (200, 100, 200), next),
            Boton("", 360, 450, 50, 50, VERDE, (100, 255, 100), mitad),
            Boton("", 510, 450, 50, 50, AMARILLO, (255, 255, 150), re_carga),
        ]


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for boton in botones:
                    if boton.ckick():
                        if boton.accion():
                            break
                for boton_comodin in botones_comodines:
                    if boton_comodin.ckick():
                        if boton_comodin.accion():
                            print(botones_comodines)

        for boton in botones:
            boton.dibujar(pantalla)

        for boton_comodin in botones_comodines:
            boton_comodin.dibujar(pantalla)

        pygame.display.flip()

def mostrar_texto(texto, x, y, color=BLANCO):
    """_summary_
        esta funcion solo cumple la funcion de mostrar un texto en pantalla con un determinado contenido, posicion y color
    Args:
        texto (_type_): Texto a mostrar
        x (_type_): Posicion en x de la pantalla
        y (_type_): Posicion en y de la pantalla
        color (_type_, optional): Color a mostrar, si no se selecciona nada sera blanco
    """
    texto_render = fuente.render(texto, True, color)
    pantalla.blit(texto_render, (x, y))

def perdiste(nombre, puntaje):
    """_summary_
        En esta funcion se entra una vez que el jugador responda mal una pregunta, en caso de que eso ocurra, mostrara un boton para salir del juego, su nombre
        y su puntaje, el cual se guardara en el archivo.
    Args:
        nombre (_type_): Nombre del jugador
        puntaje (_type_): Puntaje del jugador
    """
    gestor_puntajes = GestorPuntajes()

    salir = Boton("Salir", 300, 400, 200, 50, ROJO, (255, 100, 100), salir_juego)


    pantalla.fill(NEGRO)

    mostrar_texto(f"Game Over, {nombre}", 250, 250)
    mostrar_texto(f"Tu puntaje es: {puntaje}", 250, 300)
    gestor_puntajes.guardar_puntaje(nombre, puntaje )
    andando = True

    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if salir.ckick():
                    salir_juego()

        salir.dibujar(pantalla)

        pygame.display.flip()
    pygame.display.flip()


def felicitacion(nombre, puntaje):
    """_summary_
        Funcion en la que se entra una vez que se completen todos los niveles en la que se muestra nombre y puntaje del jugador, tambien este se guardara en el archivo
    Args:
        nombre (_type_): Nombree del jugador
        puntaje (_type_): Puntaje del jugador
    """
    salir = Boton("Salir", 300, 400, 200, 50, ROJO, (255, 100, 100), salir_juego)

    gestor_puntajes = GestorPuntajes()

    pantalla.fill(NEGRO)
    mostrar_texto(f"¡Felicidades, {nombre}!", 250, 250)
    mostrar_texto(f"Completaste todos los niveles.", 250, 300)
    mostrar_texto(f"Puntaje final: {puntaje}", 250, 350)

    gestor_puntajes.guardar_puntaje(nombre, puntaje )
    andando = True

    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if salir.ckick():
                    salir_juego()
        pygame.display.flip()

    pygame.display.flip()

def ver_puntuaciones():
    """_summary_
        Funcion para ver el puntaje de los 5 mejores jugadores del juego, se entra unicamente desde un boton del menu. dentro hay un boton para volver al menu

    """
    gestor_puntajes = GestorPuntajes()
    puntajes = gestor_puntajes.leer_puntajes()

    pantalla.fill(NEGRO)
    salir = Boton("Volver", 300, 400, 200, 50, ROJO, (255, 100, 100), salir_juego)

    andando = True

    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir_juego()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if salir.ckick():
                    andando = False 

        pantalla.fill(NEGRO) 
        mostrar_texto("Puntuaciones", 350, 50)
        y_pos = 150
        posicion = 0
        mostrar_texto("MEJORES PUNTAJES",280, 100)
        for nombre, puntaje in puntajes[:5]:
            posicion += 1
            mostrar_texto(f"{posicion}-{nombre}: {puntaje}", 300, y_pos)
            y_pos += 50

        salir.dibujar(pantalla)
        pygame.display.flip()


    mostrar_menu()

def next(gestor_preguntas, comodines):
    if comodines.next_disponible:
        comodines.usar_next(gestor_preguntas)
        return True
    else:
        print("Comodín Next ya usado")
        return False

def mitad(comodines, votos):
    if comodines.half_disponible:
        pistas = comodines.usar_half(votos)
        mostrar_texto(f"Pistas: {pistas}", 50, 500)
    else:
        mostrar_texto("Comodín ya usado", 50, 500)

def re_carga(gestor_preguntas, comodines):
    if comodines.reload_disponible:
        comodines.usar_reload(gestor_preguntas)
    else:
        print("Comodín Reload ya usado")

def salir_juego():
    """_summary_
        Funcion para salir de el juego.
    """
    pygame.quit()
    quit()


mostrar_menu()
