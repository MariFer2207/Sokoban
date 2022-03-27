print("Hola")
class sokoban:
  """
  0 - Cajas
  1 - Paredes
  2 - Muñeco
  3 - Camino
  4 - Metas
  5 - Muñeco_meta
  6 - Caja_meta
  """
  posicion_columna = 4
  mapa = [1,3,3,3,2,3,3,3,1]

  def __init__(self):
    pass

  def imprimirMapa(self):
    for i in self.mapa:
      if i == 3:
        print(" ", end = "")
      elif i == 2:
        print(chr(64), end ="")
      elif i == 1:
        print("|", end ="")
      else:
        print(i, end ="")
    print()

  def moverDerecha(self):
    self.posicion_columna += 1
    self.mapa[self.posicion_columna] = 2
    self.mapa[self.posicion_columna - 1] = 3
    self.imprimirMapa()
  def moverIzquierda(self):
    self.posicion_columna -= 1
    self.mapa[self.posicion_columna] = 2
    self.mapa[self.posicion_columna + 1] = 3

juego = sokoban()
juego.imprimirMapa()

instrucciones = "q-Salir\nd-Derecha\na-Izquierda"

while True:
  print(instrucciones)
  movimiento = input("Mover: ")
  if movimiento == "d":
    juego.moverDerecha()
  elif movimiento == "a":
    juego.moverIzquierda()
  elif movimiento == "q":
    print("Saliste deljuego")
    break
    