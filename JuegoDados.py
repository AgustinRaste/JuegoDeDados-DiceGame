import random

__author__ = 'Agustin Rastellini'


def ingresar_nombre(n):
    print("Ingrese un nombre para el jugador", n+1, ": ")
    nombre = input()
    return nombre


def ingresar_objetivo():
    n = int(input("Ingrese el valor del objetivo para ganar: "))
    while n =< 10:
        print("El valor debe ser mayor que 10")
        n = int(input("Ingrese nuevamente el valor del objetivo para ganar: "))
    return n


def turno_jugador(n):
    print("*******Juega ", n, "*******")
    puntos = 0
    prd = int(input("Ingrese 1 si apuesta por IMPAR o 0 si apuesta por PAR: "))
    while not(prd in (0, 1)):
        prd = int(input("ERROR, DEBE SER 1 PARA IMPAR o 0 PARA PAR: "))
    print("-"*20)
    # Ingresando 0 y 1 aprovecho estos valores para hacer el condicional
    if prd == 1:
        print("El jugador ", n, " apostó por IMPAR")
    else:
        print("El jugador ", n, " apostó por PAR")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    print("Obtuvo: ", dado1, ",", dado2, " y", dado3)

    suma = dado1 + dado2 + dado3
    print("Y la suma es: ", suma)
    print("-"*20)
    if (suma % 2) == prd:
        print("El jugador acertó la paridad!!")
        if (dado1 % 2) == prd and (dado2 % 2) == prd and (dado3 % 2) == prd:
            print("Además, todos los dados del tiro son de la paridad elegida, dobla su puntaje!!")
            dado_max = max(dado1, dado2, dado3)
            puntos = dado_max
            puntos = dado_max * 2
        else:
            puntos_parcial = max(dado1, dado2, dado3)
            puntos = puntos + puntos_parcial
    else:
        print("El jugador no acertó la paridad")
        dado_min = min(dado1, dado2, dado3)
        puntos -= dado_min
    print("Puntaje en esta jugada: ", puntos)
    if i == 0:
        print("*"*15, "FIN DEL TURNO", "*"*15)
    else:
        print("*"*15, "FIN DE LA JUGADA", "*"*15)
    return puntos


def determinar_ganador():
    ganador_tiene_mayoria = False
    if total[0] > total[1]:
        print("-----JUEGO TERMINADO, GANA ", nom[0], "-----")
        if cant_aciertos[0] > cant_aciertos[1]:
            ganador_tiene_mayoria = True

    elif total[1] > total[0]:
        print("-----JUEGO TERMINADO, GANA ", nom[1], "-----")
        if cant_aciertos[1] > cant_aciertos[0]:
            ganador_tiene_mayoria = True
    else:
        print("-----JUEGO TERMINADO, EMPATAN EN PUNTOS-----")
        if cant_aciertos[0] > cant_aciertos[1]:
            print("--GANA ", nom[0], " POR MAYORIA DE ACIERTOS")
            ganador_tiene_mayoria = True
        elif cant_aciertos[1] > cant_aciertos[0]:
            print("--GANA ", nom[1], " POR MAYORIA DE ACIERTOS")
            ganador_tiene_mayoria = True
        else:
            print("--Termina en empate por igualdad de aciertos--")
    return ganador_tiene_mayoria


def porcentaje_aciertos(n):
    porcentaje = float((n*100)/total_jugadas)
    return porcentaje


def puntaje_promedio(n):
    promedio = total[n]/total_jugadas
    return promedio


def menu_opciones():
    print("****************************************")
    print("* BIENVENIDOS AL JUEGO DE DADOS        *")
    print("* OPCIONES:                            *")
    print("* (1) - JUGAR                          *")
    print("* (2) - MOSTRAR ESTADISTICAS           *")
    print("* (3) - MOSTRAR REGLAS DEL JUEGO       *")
    print("* (4) - SALIR DEL PROGRAMA             *")
    print("****************************************")
    op = str(input("Ingrese una opcion: "))
    while not(op in ('1', '2', '3', '4')):
        op = str(input("Debe ser 1, 2, 3 o 4"))
    return op


def mostrar_reglas():
    print("********************************************************************")
    print("*                        REGLAS DEL JUEGO                          *")
    print("*                                                                  *")
    print("* 1- En su turno, cada jugador debe apostar por la                 *")
    print("*    paridad de la suma de los 3 dados                             *")
    print("* 2- Si acierta la paridad, el jugador suma el valor               *")
    print("*    mas alto de los 3 dados                                       *")
    print("* 3- Si NO acierta la paridad, se le restará el valor              *")
    print("*    mas bajo de los 3 dados (puede tener puntaje negativo)        *")
    print("* 4- En el caso de que el jugador acierte la paridad y             *")
    print("*    ademas, todos los dados son de la pàridad elegida             *")
    print("*    el jugador dobla su puntaje obtenido en esa jugada            *")
    print("* 5- Gana el jugador que alcance primero el objetivo,              *")
    print("*    el cual se ingresa manualmente antes de comenzar a jugar      *")
    print("* 6- En caso de empate en puntos, se acude a la cantidad de        *")
    print("*    jugadas acertadas por cada jugador. El que mas haya acertado  *")
    print("*    es el ganador del juego                                       *")
    print("* 7- En caso de igualar tambien en aciertos, entonces es un EMPATE *")
    print("*                                                                  *")
    print("********************************************************************")

    return


# EMPIEZA EL PROGRAMA

def principal():
    nom = ["Jugador 1", "Jugador 2"]
    puntos = [0, 0]
    total_jugadas = 0
    tres_aciertos = [False, False]
    # Arranca con un menu de opciones

    op = '-1'

    while op != '4':
        op = menu_opciones()
        if op == '1':
            # Reinicio todos los datos que son propios de cada partida
            hay_ganador = False
            total = [0, 0]
            cant_aciertos = [0, 0]
            aciertos_consec = [0, 0]
            tres_aciertos = [False, False]
            jugada_empatada = False
            ganador_tiene_mayoria = False
            continuar = 'n'
            if total_jugadas != 0:
                continuar = input("Desea usar los nombres de la jugada anterior? (s/n): ")
            if continuar == 'n':
                for i in range(2):
                    nom[i] = ingresar_nombre(i)
            obj = ingresar_objetivo()
            print("-"*20)
            print("El objetivo es: ", obj)
            print("-"*20)
            total_jugadas = 0   # Reinicio el contador de jugadas para cuando empiece una nueva
            print("-"*15, "INICIO DEL JUEGO", "-"*15)
            while not hay_ganador:
                for i in range(2):
                    puntos[i] = turno_jugador(nom[i])
                    total[i] += puntos[i]
                    # Si los puntos son positivos quiere decir que acertó, indistintamente de si fue doble puntaje o no
                    if puntos[i] > 0:
                        cant_aciertos[i] += 1
                        aciertos_consec[i] += 1
                    else:
                        aciertos_consec[i] = 0

                    if aciertos_consec[i] >= 3:
                        tres_aciertos[i] = True
                        nombre_tres_aciertos = nom[i]

                if puntos[0] == puntos[1]:
                    jugada_empatada = True
                print("-"*20)
                for i in range(2):
                    print("Puntaje parcial de ", nom[i], ": ", total[i])
                print("-"*20)
                total_jugadas += 1

                if total[0] >= obj or total[1] >= obj:
                    hay_ganador = True
                # Determinacion del ganador, ademas pongo una bandera para saber si el jugador que ganó
                # Fue tambien quien mas aciertos tuvo
                    ganador_tiene_mayoria = determinar_ganador()
        elif op == '2':
            if total_jugadas != 0:
                print("------------------ESTADISTICAS DEL JUEGO-----------------")
                print("- Se hicieron ", total_jugadas, "jugadas en total")

                if jugada_empatada:
                    print("- Hubo al menos una jugada con empate en puntajes!!")

                for i in range(2):
                    print("- Promedio por jugada de ", nom[i], ": ", round(puntaje_promedio(i), 2))
                for i in range(2):
                    print("-", nom[i], "acertó el ", round(porcentaje_aciertos(cant_aciertos[i]), 2), "% de las jugadas totales")
                if ganador_tiene_mayoria:
                    print("- El ganardor del juego acerto la mayoria de las jugadas")
                else:
                    print("- El ganador NO fue quien acertó la mayoria de jugadas")
                if cant_aciertos[1] == cant_aciertos[0]:
                    print("- AMBOS TUVIERON LA MISMA CANTIDAD DE ACIERTOS!")
            else:
                print("Aun no se jugó ninguna partida!")

            if tres_aciertos[0] and tres_aciertos[1]:
                print("- AMBOS JUGADORES TUVIERON 3 ACIERTOS CONSECUTIVOS")
            elif tres_aciertos[0] or tres_aciertos[1]:
                print("- EL JUGADOR ", nombre_tres_aciertos, "HIZO 3 ACIERTOS CONSECUTIVOS")

            print("Aciertos de ", nom[0], ": ", cant_aciertos[0])
            print("Aciertos de ", nom[1], ": ", cant_aciertos[1])
            print("----------------------------------------------------------")
        elif op == '3':
            mostrar_reglas()
        else:
            print("------GRACIAS POR USAR MI PROGRAMA-------")



if __name__ == '__main__':
    principal()
