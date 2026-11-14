import random

# Valores de baraja
valores = ["A", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "J", "Q", "K"]
# Simbolos 
palos = ["♥️", "♦️", "♣️", "♠️"]

# FUNCION QUE GENERA LA LISTA DE LA BARAJA
def creaBaraja (valores, palos):
  b = []
  for palo in palos:
    for valor in valores:
      b.append([valor, palo])
  return b

def esBlackjack(mano):
    return len(mano) == 2 and calcular_puntuacion(mano) == 21
  
# FUNCION QUE REVUELVE LA BARAJA
def revuelveBaraja (b):
  random.shuffle(b) #Toma la lista b (baraja) y usa el metodo shuffle para revolverla
  return b # Regresa la baraja revuelta

#FUNCION QUE IMPRIME LAS MANOS DE LOS JUGADORES
def imprimirCartas(b, j):
  #
  print("Cartas del jugador: ")
  for carta in j:
    print(carta[0], carta[1])
    
  print("Cartas de la banca:")
  print(b[0][0], b[0][1])
  print("Carta oculta")
    
  print("\nCartas restantes:", len(baraja))
    
# Calcular el valor de una mano
def calcular_puntuacion(mano):
    puntos = 0
    ases = 0

    for carta in mano:
        valor = carta[0]

        if valor == "A":
            puntos += 11
            ases += 1

        elif valor in ["J", "Q", "K"]:
            puntos += 10

        else:
            puntos += int(valor)

    # Ajustar el valor de los ases
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos

#Recibe la baraja y el mazo al que entregar
def entregarCarta(b, m): 
  m.append(b.pop())
  return

def turnoJugador(b, j):
  if calcular_puntuacion(j) == 21:
    print(f'Tienes 21 puntos, tu turno termina automaticamente')
    return
  else:
    # Turno del jugador
    print(f'Tienes {calcular_puntuacion(j)} puntos.')
    while True:
      eleccion = input(f'Quieres una carta mas?(s/n)')
      if eleccion != 'n' and eleccion != 's':
        print('Error: Entrada no valida')
        #eleccion = input(f'Quieres una carta mas?(s/n)')
        continue
      elif eleccion == 's':
        entregarCarta(b, j)
        imprimirCartas(b, j)
        print(f'Tienes {calcular_puntuacion(j)} puntos.')
        if calcular_puntuacion(j) == 21:
          print('Ya tienes 21 puntos, tu turno se cierra')
          break
        if calcular_puntuacion(j) > 21:
          print('Te pasaste de 21! Perdiste')
          break
      else:
        break

def turnoBanca(b, m):
  print("Turno de la banca")
  while True:
    if calcular_puntuacion(m) < 17:
      entregarCarta(b, m)
    else:
      break

#=================[INICIA JUEGO]=================
#CREA Y REVUELVE BARAJA
baraja = creaBaraja(valores, palos)
baraja = revuelveBaraja(baraja)
#================================
# Genera las listas para las manos del jugador y banca
jugador = [] 
banca = []

# adjuntamos a las listas las primeras dos cartas
for i in range(2):
    jugador.append(baraja.pop())
    banca.append(baraja.pop())
#================================
imprimirCartas(banca, jugador)
#================================
turnoJugador(baraja, jugador)

if calcular_puntuacion(jugador) <= 21:
    turnoBanca(baraja, banca)

print("MANOS FINALES")
print("Cartas del jugador: ")
for carta in jugador:
  print(carta[0], carta[1])
    
print("Cartas de la banca:")
for carta in banca:
  print(carta[0], carta[1])


puntos_jugador = calcular_puntuacion(jugador)
puntos_banca = calcular_puntuacion(banca)

blackjack_jugador = esBlackjack(jugador)
blackjack_banca = esBlackjack(banca)

# Ambos tienen blackjack
if blackjack_jugador and blackjack_banca:
  print("Push: ambos tienen blackjack")

# Blackjack del jugador
elif blackjack_jugador:
  print("Blackjack: gana el jugador")

# Blackjack de la banca
elif blackjack_banca:
  print("Blackjack: gana la banca")

# El jugador se pasó
elif puntos_jugador > 21:
  print("Gana la banca")

# La banca se pasó
elif puntos_banca > 21:
  print("Gana el jugador")

# Comparación normal de puntuaciones
elif puntos_jugador > puntos_banca:
  print("Gana el jugador")

elif puntos_banca > puntos_jugador:
  print("Gana la banca")

else:
  print("Push: empate")