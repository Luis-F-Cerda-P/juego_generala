import os
print("Hola")
input("Presiona Enter y me voy a borrar")

def clear_console():
  os.system('printf "\033c"')
# Call the function to clear the console
clear_console()
input("Debo aparecer después de que todo se borró")
