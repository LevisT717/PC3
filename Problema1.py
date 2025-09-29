while True:
    try:
        fraccion = input("Ingrese la fracción en formato X/Y: ")
        x, y = fraccion.split("/")  
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError  
        if x > y:
            raise ValueError  

        porcentaje = round((x / y) * 100)

        if porcentaje <= 1:
            print("E")   
        elif porcentaje >= 99:
            print("F")   
        else:
            print(f"{porcentaje}%")
        break  

    except ValueError:
        print("❌ Error: Ingrese números enteros válidos en el formato X/Y, con X ≤ Y.")
    except ZeroDivisionError:
        print("❌ Error: El denominador (Y) no puede ser cero.")
