import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fuentes = figlet.getFonts()  # Lista de fuentes disponibles

    # Pedir fuente al usuario
    fuente = input("Ingrese el nombre de la fuente (ENTER para aleatoria): ").strip()

    if fuente == "":
        fuente = random.choice(fuentes)  # Selección aleatoria si no ingresó nada
    elif fuente not in fuentes:
        print("Fuente no encontrada, se usará una fuente aleatoria.")
        fuente = random.choice(fuentes)

    figlet.setFont(font=fuente)

    # Pedir texto al usuario
    texto = input("Ingrese el texto que desea imprimir: ")

    # Mostrar el texto en ASCII Art
    print("\n--- Resultado ---")
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
