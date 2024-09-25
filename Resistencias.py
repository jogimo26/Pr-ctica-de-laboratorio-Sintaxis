print("Por favor seleccione qué tipo de resistencia quiere calcular:\n" "1. Todas en serie\n" "2. Todas en paralelo\n" "3. Mixto (R1, R2 en serie, R3 en paralelo)\n" "4. Mixto (R1, R3 en serie, R2 en paralelo)\n" "5. Mixto (R2, R3 en serie, R1 en paralelo)")
eleccion = int(input("Ingrese su selección: "))
if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4 or eleccion == 5:
    print("Qué valor tienen sus resistencias a calcular?")
    R1 = float(input("Por favor ingrese el valor de R1: "))
    R2 = float(input("Por favor ingrese el valor de R2: "))
    R3 = float(input("Por favor ingrese el valor de R3: "))
    if eleccion == 1:
        Rtotal = R1+R2+R3
        print("El factor de corrección de esta operación es de aumento de 5%.")
        Rtotal += (0.05*Rtotal)
        if Rtotal > 100:
            Rtotal += 20
            print("ADVERTENCIA: La resistencia total se ha tenido que corregir debido a que la resistencia total en serie calculada ha sido de más de 100 ohmios. El nuevo valor de la resistencia total es: ", Rtotal)
        else:
            print("El valor total de su resistencia es: ", Rtotal)
    elif eleccion == 2:
        Rtotal = (1 / ((1/R1) + (1/R2) + (1/R3)))
        print("El factor de corrección de esta operación es de disminución de 10%.")
        Rtotal =- (0.1*Rtotal)
        if Rtotal < 10:
            Rtotal -= 2
            print("ADVERTENCIA: La resistencia total se ha tenido que corregir debido a que la resistencia total en paralelo calculada ha sido de menos de 10 ohmios. El nuevo valor de la resistencia total es: ", Rtotal)
        else:
            print("El valor total de su resistencia es: ",Rtotal)
    elif eleccion == 3:
        Rtotal = (1 / ((1/(R1+R2)) + (1/R3)))
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
    elif eleccion == 4:
        Rtotal = (1 / ((1/(R1+R3)) + (1/R2)))
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
    else:
        Rtotal = 1 / ((1/(R2+R3)) + (1/R1))
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
else:
    print("Elección no válida")
