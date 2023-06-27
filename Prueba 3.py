from operator import truediv
from pickle import APPEND
opc = 0
fila = 10
columnas = 15
peliculas = []
entradas = []
asientos = []



alumno_Duoc = input("Es alumno duoc? ")

def menu():
    print("Peliculas en cartelera")
    peliculas()

while True:
    print("Que pelicula desea? ")
    print("[1]Spiderman-Lejos de casa 🕸")
    print("[2]El Rey Leon🦁")
    print("[3]Toy story 4")
    print("[4]Scream IV🔪")
    print("[5]Super Mario Bros 2D🍝")
    print("[6]Super Mario Bros 3D🍝")
    print("[7]Avatar 3D🟦")
    peliculas = input(int("Seleccione una opcion"))

 


#profe

#while True:
    #imprimir()
    #print("selecciona tu asiento")
    #fila = int(input("Seleccione la fila: "))

#for fila in range(10):
    #for columna in range(15):
        #print(f"[{asientos[fila][columna]} ]",end="")
        #print("")    
