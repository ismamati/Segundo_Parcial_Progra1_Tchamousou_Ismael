import csv

class GestorPuntajes:
    def __init__(self, archivo_csv="./puntuaciones.csv"):
        self.archivo_csv = archivo_csv

    def guardar_puntaje(self, nombre, puntaje):
        """_summary_
            Guarda los puntajes en el archivo csv
        Args:
            nombre (_type_): Nombre del jugador
            puntaje (_type_): Puntaje
        """

        with open(self.archivo_csv, mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, puntaje])

    def leer_puntajes(self):

        puntajes = []
        try:
            with open(self.archivo_csv, mode="r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    if len(fila) == 2:  
                        puntajes.append((fila[0], int(fila[1])))
            self.ordenamiento(puntajes)
        except FileNotFoundError:
            pass  
        return puntajes
    
    def ordenamiento(self, matriz):
        for filas in range(len(matriz)-1):
            for  filas_2 in range(filas+1,len(matriz)):
                if matriz[filas_2][1] > matriz[filas][1]:
                    matriz[filas_2], matriz[filas] = matriz[filas],matriz[filas_2]

        

