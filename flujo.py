# Escribir un script en Python que permita calcular
# la superficie de figuras geométricas. Debe mostrar
# un menú para elegir entre las figuras: cuadrado, 
# rectángulo, triángulo y círculo. Dependiendo de la 
# figura elegida, solicitará los datos para el cálculo
# y mostrará por pantalla el resultado. Los valores 
# ingresados deben estar expresados en cm.
import math 

print(math.pi)
def calcularCuadrado():
  lado1 = int(input("Ingresa en cm el lado: \n"))
  print(f"El área es de {lado1*lado1}cm²\n")

def calcularRectángulo():
  lado1 = int(input("Ingresa en cm el largo: \n"))
  lado2 = int(input("Ingresa en cm el ancho: \n"))
  print(f"El área es de {lado1*lado2}cm²")

def calcularTriángulo():
  lado1 = int(input("Ingresa en cm la base: \n"))
  lado2 = int(input("Ingresa en cm la altura: \n"))
  print(f"El área es de {(lado1*lado2)/2}cm²")

def calcularCírculo():
   lado1 = float(input("Ingresa en cm el radio: \n"))
   print(f"El área es de {round(math.pi*(lado1**2), 2)}cm²")
  

while True:
  
  print("Escoge una opción:")
  print("1) Cuadrado")
  print("2) Rectángulo")
  print("3) Triángulo")
  print("4) Círculo")
  eleccionUsuario = int(input(""))

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
