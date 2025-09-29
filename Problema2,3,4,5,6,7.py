# funciones2.py

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


def cargar_alumnos():
    alumnos = []
    try:
        n = int(input("Ingrese la cantidad de alumnos: "))
        if n <= 0:
            raise ValueError("El número debe ser mayor que cero.")
    except ValueError as e:
        print("Error:", e)
        return []

    for i in range(n):
        nombre = input(f"Ingrese el nombre completo del alumno {i+1}: ").strip()
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
        alumnos.append({"nombre": nombre, "notas": notas})
    return alumnos


def evaluar_alumnos(alumnos):
    aprobados = 0
    desaprobados = 0
    for alumno in alumnos:
        promedio = sum(alumno["notas"]) / 3
        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    return aprobados, desaprobados


def promedio_curso(alumnos):
    if not alumnos:
        return 0
    total = sum(sum(alumno["notas"]) / 3 for alumno in alumnos)
    return total / len(alumnos)


def mejores_y_peores(alumnos):
    if not alumnos:
        return None, None
    promedios = [(alumno["nombre"], sum(alumno["notas"]) / 3) for alumno in alumnos]
    mejor = max(promedios, key=lambda x: x[1])
    peor = min(promedios, key=lambda x: x[1])
    return mejor, peor


def buscar_alumno(alumnos, texto):
    if not alumnos:
        return []

    texto = texto.lower()
    resultados = []
    for alumno in alumnos:
        if texto in alumno["nombre"].lower():
            promedio = sum(alumno["notas"]) / 3
            resultados.append({
                "nombre": alumno["nombre"],
                "notas": alumno["notas"],
                "promedio": promedio
            })
    return resultados


def menu():
    alumnos = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar alumnos y notas")
        print("2. Crear rectángulo y cuadrado")
        print("3. Evaluar aprobados y desaprobados")
        print("4. Promedio general del curso")
        print("5. Mejor y peor promedio")
        print("6. Buscar alumno por nombre")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alumnos = cargar_alumnos()
        elif opcion == "2":
            try:
                largo = float(input("Ingrese el largo del rectángulo: "))
                ancho = float(input("Ingrese el ancho del rectángulo: "))
                rect = Rectangulo(largo, ancho)
                print(f"Área del rectángulo: {rect.area()}")

                lado = float(input("Ingrese el lado del cuadrado: "))
                cuad = Cuadrado(lado)
                print(f"Área del cuadrado: {cuad.area()}")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        elif opcion == "3":
            if alumnos:
                aprob, desaprob = evaluar_alumnos(alumnos)
                print(f"Aprobados: {aprob}, Desaprobados: {desaprob}")
            else:
                print("Debe cargar alumnos primero.")
        elif opcion == "4":
            if alumnos:
                print(f"Promedio general del curso: {promedio_curso(alumnos):.2f}")
            else:
                print("Debe cargar alumnos primero.")
        elif opcion == "5":
            if alumnos:
                mejor, peor = mejores_y_peores(alumnos)
                print(f"Mejor promedio: {mejor[0]} con {mejor[1]:.2f}")
                print(f"Peor promedio: {peor[0]} con {peor[1]:.2f}")
            else:
                print("Debe cargar alumnos primero.")
        elif opcion == "6":
            if alumnos:
                texto = input("Ingrese el nombre (completo o parcial) a buscar: ")
                resultados = buscar_alumno(alumnos, texto)
                if resultados:
                    print("\nResultados encontrados:")
                    for r in resultados:
                        print(f"- {r['nombre']} | Notas: {r['notas']} | Promedio: {r['promedio']:.2f}")
                else:
                    print("No se encontraron coincidencias.")
            else:
                print("Debe cargar alumnos primero.")
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
