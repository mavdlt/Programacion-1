#CIFRADO CESAR. Se encripta de acuerdo al abecedario y un desplazamiento dado


alfabeto = "ABCDEFJHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñoprstuvwxyz"

print("Este programa encripta mensajes de acuerdo al abecedario y un desplazamiento dado. Además es capaz de desencriptar mensajes.")
codigo = input("Escribe tu mensaje a codificar: ")

while codigo == "":
    codigo = input("ERROR. Este campo no puede quedar vacío. Escribe tu mensaje a codificar ")


desplazamiento = int(input("Desplazamiento = "))

while desplazamiento < 0: 
    desplazamiento = int(input("ERROR. Debe ser un valor positivo. Desplazamiento = "))

mensajeCifrado = ""
# Para cada letra del codigo a cifrar
for letra in codigo:
  #La letra debe estar en el alfabeto
  if letra in alfabeto:
    posicion = alfabeto.index(letra)

    # Si la suma de posicion y desplazamiento es mayor a la longitud del alfabeto, volvemos al inicio del alfabeto
    if (posicion + desplazamiento) > (len(alfabeto)-1):
      mensajeCifrado += alfabeto[(posicion + desplazamiento) - len(alfabeto)]
    else:
      mensajeCifrado += alfabeto [posicion + desplazamiento]

print(f"Tu mensaje codificado es {mensajeCifrado}")

mensajeDecifrado = ""
for letra in mensajeCifrado:
    if letra in alfabeto:
            posicion = alfabeto.index(letra)
            nuevaPosicion = (posicion - desplazamiento) % len(alfabeto)
            mensajeDecifrado += alfabeto[nuevaPosicion]
    else:
            mensajeDecifrado += letra

print(f"Tu mensaje decodificado es {mensajeDecifrado}")