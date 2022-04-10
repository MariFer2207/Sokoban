"""
Autora:Maria Fernanda Avelar Alvarez
Fecha: 12/04/2022
Descripcion: Sokoban-Juego
    0 - Cajas
    1 - Paredes
    2 - Muñeco
    3 - Camino
    4 - Metas
    5 - Muñeco_meta
    6 - Caja_meta
"""
class sokoban:
    
 print("Hola")

    
mapa = [
    [1,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,1,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,0,3,3,3,1,1,3,1],
    [1,0,3,3,3,2,3,3,0,4,3,1,3,3,1],
    [1,3,3,3,3,3,0,1,1,3,3,3,3,1,1],
    [1,3,3,3,3,3,3,3,0,3,3,1,3,3,1],
    [1,1,3,3,3,3,0,3,3,3,3,1,1,1,1],
    [1,1,3,3,3,3,3,3,0,3,3,3,1,3,1],
    [1,3,3,3,0,3,3,3,3,1,1,1,3,3,1],
    ]

#Posición inicial del muñeco en el mapa
muñeco_fila = 3
muñeco_columna = 5

def imprimirMapa(self):
    for fila in self.mapa:
        print(fila)
"""Imprime el mapa completo"""

def moverDerecha(self):
     """Controla los movimientos a la derecha"""

#00 - Personaje, camino -> [2,3] -> [3,2]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
        self.muneco_columna += 1

#01 - Personaje, meta -> [2,4] -> [3,5]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
        self.muneco_columna += 1

#02 - Personaje, caja, camino -> [2,0,3] -> [3,2,0]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 2
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 0
        self.muneco_columna += 1

#03 - Personaje, caja, meta -> [2,0,4] -> [3,2,6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 2
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
        self.muneco_columna += 1
        
#04 - Personaje, caja_meta, espacio -> [2,6,3] -> [3,5,0]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
        self.muneco_columna += 1

#05 - Personaje, caja_meta, meta -> [2,6,4] -> [3,5,0]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 0
        self.muneco_columna += 1

#06 - Personaje_meta, espacio -> [5,3] -> [4,2]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
        self.muneco_columna += 1

#07 - Personaje_meta, meta -> [5,4] -> [4,5]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
        self.muneco_columna += 1

#08 - Personaje_meta, caja, espacio -> [5,0,3] -> [4,2,0]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 2
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 0
        self.muneco_columna += 1
            
#09 - Personaje_meta, caja, meta -> [5,0,4] -> [4,2,6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 3
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 0
        self.muneco_columna += 1

#10 - Personaje_meta, caja_meta, epacio -> [5,6,3] -> [4,5,0]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 3:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 0
        self.muneco_columna += 1

#11 - Personaje_meta, caja_meta, meta -> [5,6,4] -> [4,5,6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
        self.muneco_columna += 1

def moverIzquierda(self):
"""Controla los movimiento a la izquierda"""

#12 - Personaje, espacio -> [3,2] -> [2,3]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 3 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 2
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 3
        self.muneco_columna -= 1
        
#13 - Personaje, meta -> [4,2] -> [5,3]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 4 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 5
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 3
        self.muneco_columna -= 1

#14 - Personaje, caja, espacio -> [3,0,2] -> [0,3,3]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 3 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 0
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 3
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 3
        self.muneco_columna -= 1

#15 - Personaje, caja, meta -> [4,0,2] -> [6,3,3]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 4 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 6
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 3
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 3
        self.muneco_columna -= 1

#16 - Personaje, caja_meta, espacio -> [3,6,2] -> [0,4,3]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 3 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 0
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 4
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 3
        self.muneco_columna -= 1

#17 - Personaje, caja_meta, meta -> [4,6,2] -> [0,4,3]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 4 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 0
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 4
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 3
        self.muneco_columna -= 1

#18 - Personaje_meta, espacio -> [3,5] -> [2,4]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 3 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 5:
        self.mapa[self.muneco_fila][self.muneco_columna] = 2
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 4
        self.muneco_columna -= 1

#19 - Personaje_meta, meta -> [5,2] -> [4,4]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2:
        self.mapa[self.muneco_fila][self.muneco_columna] = 4
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 4
        self.muneco_columna -= 1

#20 - Personaje_meta, caja, espacio -> [5,0,5] -> [0,2,4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 5:
        self.mapa[self.muneco_fila][self.muneco_columna] = 0
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 2
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 4
        self.muneco_columna -= 1

#21 - Personaje_meta, caja, meta -> [4,0,5] -> [6,2,4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 4 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 5:
        self.mapa[self.muneco_fila][self.muneco_columna] = 6
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 2
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 4
        self.muneco_columna -= 1

#22 - Personaje_meta, caja_meta, espacio -> [3,6,5] -> [0,5,4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 3 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 5:
        self.mapa[self.muneco_fila][self.muneco_columna] = 0
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 4
        self.muneco_columna -= 1

#23 - Personaje_meta, caja_meta, meta -> [4,6,5] -> [6,5,4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 4 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 5:
        self.mapa[self.muneco_fila][self.muneco_columna] = 6
        self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
        self.mapa[self.muneco_fila][self.muneco_columna - 2] = 4
        self.muneco_columna -= 1
        

def jugar(self):
    while True:
        self.imprimirMapa()
        instrucciones = "d-Derecha, b-Abajo, a-Izquierda, q-Arriba, s-Salir"
        print(instrucciones)
        movimiento = input("Mover a: ")
        if movimiento == "d":
            self.moverDerecha()
        elif movimiento == "b":
            self.moverAbajo()
        elif movimiento == "a":
            self.moverIzquierda()
        elif movimiento == "q":
            self.moverArriba()
        elif movimiento == "s":
            break
juego = sokoban()
juego.jugar()
                



