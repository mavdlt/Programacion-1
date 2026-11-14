def nombre_mes(m):
  if m== 1:
    return "Enero"
  elif m==2:
    return "Febrero"
  elif m== 3:
    return "Marzo"
  elif m== 4:
    return "Abril"
  elif m== 5:
    return "Mayo"
  elif m== 6:
    return "Junio"
  elif m==7:
    return "Julio"
  elif m==8:
    return "Agosto"
  elif m==9:
    return "Septiembre"
  elif m==10:
    return "Octubre"
  elif m==11:
    return "Noviembre"
  elif m==12:
    return "Diciembre"
#-----------------------------------------------------------------------
def año_bisiesto(año):
  if año % 4==0 and año %100!=0 or año%400==0: # año bisiesto
    return True
  else:
    return False
#-----------------------------------------------------------------------
def dias_mes(mes, año):
  match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        return 31
    case 4 | 6 | 9 | 11:
        return 30
    case 2:
        if año_bisiesto(año):
            return 29
        else:
            return 28
#-----------------------------------------------------------------------

def dia_semana(d):
    nombre_dia = None
    if d == 1:
        nombre_dia ="Lunes"
    elif d == 2:
        nombre_dia ="Martes"
    elif d == 3:
        nombre_dia ="Miercoles"
    elif d == 4:
        nombre_dia ="Jueves"
    elif d == 5:
        nombre_dia ="Viernes"
    elif d == 6:
        nombre_dia ="Sabado"
    elif d == 0:
        nombre_dia ="Domingo"
    return nombre_dia

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
while True:
  try:
    año = int(input("Escribe un año en [1900,2026]: "))
    if año>=1900 and año<=2026:
      break
    else:
      print("Se espera un número entero en [1900,2026]")
  except ValueError:
    print("Debes escribir un número entero")


while True:
  try:
    mes = int(input("Escribe un mes: "))
    if mes>=1 and mes<=12:
      break
    else:
      print("Debes escribir un número entero en [1,12]")
  except ValueError:
    print("Debes escribir un número entero")

numDias = dias_mes(mes, año)
nombreMes = nombre_mes(mes)

while True:
    try:
        dia = int(input("Escribe un dia: "))
        if dia>=1 and dia<=numDias:
            break
        else:
            print(f"Debes escribir un numero en [1,{numDias}]")
    except ValueError:
        print("Debes escribir un número entero")

a = (14 - mes ) // 12
b = año - a
c = mes + 12*a - 2

indicador = dia + b + b // 4 - b // 100 + b // 400 + (31*c) // 12
d = indicador % 7

nombre_dia_semana = dia_semana(d)
print(f"La fecha dada es {nombre_dia_semana} {dia} de {nombreMes} del {año}")