# import math
import random
import os

def clear_console():
  os.system('printf "\033c"')
# Call the function to clear the console
clear_console()

def lanzar_dados(jugador):
  lanzamiento = [
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
  ]
  jugador["dados"] = lanzamiento
  print(f"Lanzaste: {lanzamiento}")

def obtener_y_presentar_categorias_posibles(jugador):
  def no_tiene_puntaje(categoria):
    key, value = categoria
    return value == None
  
  def categorias_numericas(categoria):
    if categoria in ultimo_lanzamiento_strings:
      return True
  
  
  ultimo_lanzamiento = [1,1,1,1,2]
  # ultimo_lanzamiento = jugador["dados"]
  ultimo_lanzamiento_strings = list(map(lambda x: str(x), ultimo_lanzamiento))


  distribucion = {
    "1": ultimo_lanzamiento_strings.count("1"),
    "2": ultimo_lanzamiento_strings.count("2"),
    "3": ultimo_lanzamiento_strings.count("3"),
    "4": ultimo_lanzamiento_strings.count("4"),
    "5": ultimo_lanzamiento_strings.count("5"),
    "6": ultimo_lanzamiento_strings.count("6"),
  }

  # print("La distribución es:", distribucion)

  ocurrencias = distribucion.values()
  lanzamiento_ordenado = ultimo_lanzamiento.sort()

  categorias_sin_puntaje = list(dict(filter(no_tiene_puntaje, jugador["categorias"].items())))

  numericas = list(set(ultimo_lanzamiento_strings))
  generala = any(value == 5 for value in ocurrencias)
  generala_doble = generala and jugador["categorias"]["Generala"] != None
  poker = any(value >= 4 for value in ocurrencias)
  full = any(value == 3 for value in ocurrencias) and any(value == 2 for value in ocurrencias)
  escalera = lanzamiento_ordenado == [1,2,3,4,5] or lanzamiento_ordenado == [2,3,4,5,6] or lanzamiento_ordenado == [1,3,4,5,6]
    
  categorias_posibles = []
  categorias_posibles += numericas  # Concatenate numericas list to categorias_posibles
  if generala_doble:
      categorias_posibles.append("Generala Doble")  # Append "Generala" to categorias_posibles
  if generala:
      categorias_posibles.append("Generala")  # Append "Generala" to categorias_posibles
  if poker:
      categorias_posibles.append("Póker")  # Append "Poker" to categorias_posibles
  if full:
      categorias_posibles.append("Full")  # Append "Full" to categorias_posibles
  if escalera:
      categorias_posibles.append("Escalera")  # Append "Escalera" to categorias_posibles


  # print(categorias_posibles)
  # print(categorias_sin_puntaje)

  categorias_aplicables = list(set(categorias_posibles) & set(categorias_sin_puntaje))
  categorias_aplicables.sort()
  
  
  print("Puedes puntuar en las siguientes categorías:")
  for index, element in enumerate(categorias_aplicables):
    print(f"{index + 1}) {element}")
  

categorias = {
  "1": None,
  "2": None,
  "3": None,
  "4": None,
  "5": None,
  "6": None,
  "Escalera":None,
  "Full":None,
  "Póker":None,
  "Generala":None,
  "Generala Doble":None,
}
jugador1 = {"categorias": dict(categorias)}
jugador2 = {"categorias": dict(categorias)}

print("Bienvenido al juego La Generala! 😁🎲")
jugador1["nombre"] = input("Ingresa el nombre del jugador 1:\n")
jugador2["nombre"] = input("Ingresa el nombre del jugador 2:\n")

input(f"{jugador1["nombre"]}, presiona 'Enter' para lanzar tus dados 🎲")
lanzar_dados(jugador1)
obtener_y_presentar_categorias_posibles(jugador1)




  
""" 
print("1) Cuadrado")
print("2) Rectángulo")
print("3) Triángulo")
print("4) Círculo")
eleccionUsuario = int(input(""))

while True:
  match eleccionUsuario:
    case 1:
         calcularCuadrado()
    case 2:
         calcularRectángulo()
    case 3:
         calcularTriángulo()
    case 4:
         calcularCírculo()
    case _:
        print("No ingresaste una opción válida! Este programa solo recibe número como instrucciones")
        continue
     
  continuar = input("Deseas calcular el área de otra figura? Y/N: \n")
  if continuar.lower() == "n":
     print("Hasta luego! Gracias por calcular con nosotros!")
     break
  else: 
     continue
 """