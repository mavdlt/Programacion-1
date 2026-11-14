#Maria de los Angeles Valenzuela De la trinidad
print("Este programa indica los primeros 16 caracteres de la curp")

apellido1 = input("Escribe tu Primer Apellido (*) ").upper()
apellido2 = input("Escribe tu Segundo Apellido ").upper()
nombre1 = input("Escribe tu Primer Nombre (*) ").upper()
nombre2 = input("Escribe tu Segundo Nombre ").upper()

#============================================================
#Comienza ciclo para evitar vacíos en Primer Apellido y Primer Nombre
while apellido1 == "" or nombre1 == "" :
    if apellido1 == "" :
        print("*Primer apellido no debe quedar vacío")
        apellido1 = input("Escribe tu Primer Apellido: ").upper()

    if nombre1 == "" :
        print("*Primer Nombre no debe quedar vacío")
        nombre1 = input("Escribe tu Primer Nombre (*) ").upper()
    
print(f"Tu nombre completo es {nombre1} {nombre2} {apellido1} {apellido2}")

#============================================================
#Primer letra de la curp
curp = apellido1[0]

#Si apellido comienza con Ñ, reemplazar por X
if apellido1[0] == "Ñ" :
    curp = "X"

#============================================================
#Inicio contador para segunda letra de curp
    
c = 1 #Se requiere la primera vocal interna, no la del inicio del apellido

#Comparar cada letra hasta encontrar la primera vocal interna
while c < len(apellido1) :
    if apellido1[c] == "A" or apellido1[c] == "Á" :
        curp = curp + "A"
        break
    elif apellido1[c] == "E" or apellido1[c] == "É" :
        curp = curp + "E"
        break
    elif apellido1[c] == "I" or apellido1[c] == "Í" :
        curp = curp + "I"
        break
    elif apellido1[c] == "O" or apellido1[c] == "Ó" :
        curp = curp + "O"
        break
    elif apellido1[c] == "U" or apellido1[c] == "Ú" :
        curp = curp + "U"
        break
    #Si el apellido no tiene vocal interna
    elif apellido1[c] != "A" and apellido1[c] != "Á" and apellido1[c] != "E" and apellido1[c] != "É" and apellido1[c] != "I" and apellido1[c] != "Í" and apellido1[c] != "O" and apellido1[c] != "Ó" and apellido1[c] != "U" and apellido1[c] != "Ú" :
        curp = curp + "X"
        break
    c = c + 1
    
#============================================================
#Tercera letra de curp. Primera letra del apellido 2

#si el apellido comienza con Ñ o no hay se pondra X en la tercera posicion
if apellido2[0] == "Ñ" or apellido2 == "":
    curp = curp + "X"
else :
    curp = curp + apellido2[0]

#============================================================
#cuarta letra. Primera letra de nombre2
nombresMasUsados = ["MARIA", "MA", "MA.", "JOSE", "J", "J."]
if nombre2 == "":
    curp += nombre1[0]
elif nombre2[0] == "Ñ" :
    curp += "X"
elif nombre1 in nombresMasUsados:
    curp += nombre2[0]
else: 
    #Nombre compuesto
    if (" " in nombre1):
        
        c=0
        while c < len(nombre1):
            if nombre1[c] != " " :
                primerPalabra += nombre1[c]
                c += 1
            else:
                break
        
        nombresMasUsados = ["MARIA", "MA", "MA.", "JOSE", "J", "J."]
        
        if primerPalabra in nombresMasUsados:
            ultimoEspacio = c
            while c < len(nombre1):
                if nombre1[c] != " " :
                    ultimoEspacio = c
                c += 1
            curp += nombre1[ultimoEspacio + 1]
                

    #Nombre no compuesto
    else:
        curp += nombre1[0]
        
if curp == "BACA" or curp == "BAKA" or curp == "BUEI" or curp == "BUEY" or curp == "CACA" or curp == "CACA" or curp == "CACO" or curp == "CAGA" or curp == "CAGO" or curp == "CAKA" or curp == "CAKO" or curp == "COGE" or curp == "COGI" or curp == "COJO" or curp == "COJA" or curp == "COJE" or curp == "FETO" or curp == "LOCA" or curp == "LOCO" or curp == "MAMO" or curp == "MAME" or curp == "MAMI" or curp == "MOCO" or curp == "MEAR" or curp == "MEAS" or curp == "MEON" or curp == "PADA" or curp == "PEDI" or curp == "PENE" or curp == "PIPI" or curp == "PITO" or curp == "POPO" or curp == "PUTA" or curp == "PUTO" or curp == "QULO" or curp == "RATA" or curp == "ROBA" or curp == "RUIN" or curp == "SENO" or curp == "TETA" or curp == "VACA" or curp == "VAGA" or curp == "VAGO" or curp == "VAKA" or curp == "VUEI" or curp == "VUEY" :
    curp = curp.replace(curp[1],"X")

print(f"Primeros 4 dígitos de la curp {curp}")

#============================================================
#fecha de nacimiento. Dígitos del 5 - 10
year = int(input("Escribe el año [1900,2026]: "))

while year < 1900 or year >= 2026 :
    print("Escribe el año entre estos rangos [1900,2026]")
    year = int(input("Escribe el año [1900,2026]: "))

mes = int(input("Escribe el mes en el rango [1,12]"))

while mes <1 or mes > 12 :
    print("Escribe el mes en el rango [1,12]")
    mes = int(input("Escribe el mes en el rango [1,12]"))
    
match mes :
    #meses con 31 días
    case 1|3|5|7|8|10|12 :
        diaNacimiento = int(input("Escribe tu día de nacimiento"))
        if diaNacimiento > 31 or diaNacimiento < 1:
            print("ERROR")
        else:
            print("Tu fecha de nacimiento es ", diaNacimiento, ",",mes,",",year)
    case 2 :
        #Bisiesto
        if year %4 == 0 and year %100 != 0 or year %400 == 0:
            diaNacimiento = int(input("Escribe tu día de nacimiento"))
            
            if diaNacimiento <1 or diaNacimiento >29 :
               print("ERROR")
            else :
                print("Tu fecha de nacimiento es ", diaNacimiento, ",",mes,",",year)
        else :
            diaNacimiento = int(input("Escribe tu día de nacimiento"))
            
            if diaNacimiento < 1 or diaNacimiento > 28 :
               print("ERROR")
            else :
                print("Tu fecha de nacimiento es ", diaNacimiento, ",",mes,",",year)
    #meses con 30 días
    case 4|6|9|11 :
        diaNacimiento = int(input("Escribe tu día de nacimiento"))
        if diaNacimiento > 30 or diaNacimiento < 1:
            print("ERROR")
        else:
            print("Tu fecha de nacimiento es ", diaNacimiento, ",",mes,",",year)

#str convirte valores numéricos a caracteres
#.zfill agrega ceros hasta completar la longitud establecida 
caracter_year = str(year) [2:]
caracter_mes = str(mes).zfill(2)
caracter_dia = str(diaNacimiento).zfill(2)

fecha = caracter_year + caracter_mes + caracter_dia
curp = curp + fecha
print(f"Curp con fecha {curp}")

#============================================================
#Posición 11. Sexo M o H
sexo = input("Escribe tu sexo biológico: Mujer [M] o Hombre [H]").upper()

while sexo != "H" and sexo != "M":
    sexo = input("ERROR. Escribe tu sexo biológico: Mujer [M] o Hombre [H]").upper()

if sexo == "H" :
    curp = curp + "H"
else :
    curp = curp + "M"
    
print(f"Curp con genero {curp}")

#============================================================
# Posición 12 y 13. La letra inicial y última consonante del estado de nacimiento
estados = ["AGUASCALIENTES","BAJA CALIFORNIA", "BAJA CALIFORNIA SUR", "CAMPECHE", "COAHUILA", "COLIMA", "CHIAPAS","CHIHUAHUA","DISTRITO FEDERAL","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","MEXICO", "MICHOACAN","MORELOS","NAYARIT","NUEVO LEON","OAXACA","PUEBLA","QUERETARO","QUINTANA ROO","SAN LUIS POTOSI", "SINALOA", "SONORA", "TABASCO", "TAMAULIPAS","TLAXCALA", "VERACRUZ", "YUCATAN","ZACATECAS"]

claveEstado = ["AS","BC","BS","CC","CL","CH","CM","CH","DF","DG","GT","GR","HG","JC","MC","MN","MS","NT","NL","OC","PL","QT","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]

#numeración por estado
i = 0
while i < 32 :
    print(i+1,".",estados[i])
    i += 1

seleccion = int(input("Estado de nacimiento "))
print(f"El estado que seleccionaste es {seleccion}")

while seleccion < 1 or seleccion > 32 :
    print("Debe escribir en el rango [1,32]")
    seleccion = int(input("Estado de nacimiento "))


seleccion = claveEstado[seleccion-1]
print(f"La clave del estado es {seleccion}")

curp = curp + seleccion
print(f"La curp con clave de estado es {curp}")

#============================================================
# Dígitos de 14-16.

# 14.primera consonante interna del primer apellido

c = 1
while c < len(apellido1) :
        
    #Si la primera consonante interna es Ñ se sustituye por 'X'
    if apellido1[c] == "Ñ" :
            curp = curp + "X"
            break
    
    if apellido1[c] != "A" and apellido1[c] != "Á" and apellido1[c] != "E" and apellido1[c] != "É" and apellido1[c] != "I" and apellido1[c] != "Í" and apellido1[c] != "O" and apellido1[c] != "Ó" and apellido1[c] != "U" and apellido1[c] != "Ú" :
        curp = curp + apellido1[c]
        break
    c = c + 1
        
    if c == len(apellido1) and len(curp) != 14:
        curp = curp + "X"

# 15.primera consonante interna del segundo apellido

#Si apellido 2 es vacío se sustituye por 'X'
if apellido2 == "":
    curp = curp + "X"
#De otra forma se comienza el ciclo
else:
    c = 1
    while c < len(apellido2) :
    
        #Si la primera consonante interna es Ñ se sustituye por 'X'
        if apellido2[c] == "Ñ":
            curp = curp + "X"
            break
        
        elif apellido2[c] != "A" and apellido2[c] != "Á" and apellido2[c] != "E" and apellido2[c] != "É" and apellido2[c] != "I" and apellido2[c] != "Í" and apellido2[c] != "O" and apellido2[c] != "Ó" and apellido2[c] != "U" and apellido2[c] != "Ú" :
            curp = curp + apellido2[c]
            break
        c = c + 1
        
        if c == len(apellido2) and len(curp) != 15:
            curp = curp +"X"

# 16.primera consonante interna del nombre

#Si la primera consonante interna es Ñ se sustituye por 'X'

c = 1
while c < len(nombre1) :
    #Si es nombre compuesto o nombre común se utiliza la primera letra del segundo nombre
    if nombre1 in nombresMasUsados:
        nombre2[c] != "A" and nombre2[c] != "Á" and nombre2[c] != "E" and nombre2[c] != "É" and nombre2[c] != "I" and nombre2[c] != "Í" and nombre2[c] != "O" and nombre2[c] != "Ó" and nombre2[c] != "U" and nombre2[c] != "Ú"
        curp = curp + nombre2[c]
        break
    c = c + 1
    
    #Si la primera consonante interna es Ñ se sustituye por 'X'
    if nombre1[c] == "Ñ":
        curp = curp + "X"
        break        
    
    #Se busca la primera consonante interna del nombre 1
    if nombre1[c] != "A" and nombre1[c] != "Á" and nombre1[c] != "E" and nombre1[c] != "É" and nombre1[c] != "I" and nombre1[c] != "Í" and nombre1[c] != "O" and nombre1[c] != "Ó" and nombre1[c] != "U" and nombre1[c] != "Ú" :
        curp = curp + nombre1[c]
        break
    c = c + 1
    
    #Se termian el ciclo y no hay cosonante
    if c==len(nombre1) and len(curp) != 16:
        curp = curp + "X"

print(f"La curp final es {curp}")