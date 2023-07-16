import os
from colorama import Fore, Style


def inicializar_juego():
    tablero = [[" " for i in range(3)] for j in range(3)]
    return tablero


def mostrar_tablero(tablero):
    os.system("cls")
    for i in range(3):
        if i > 0:
            print("-" * 11)

        for j in range(3):
            if j > 0:
                print("|", end="")
            if tablero[i][j] == "X":
                print(Fore.LIGHTRED_EX + " " + tablero[i][j] + " " + Style.RESET_ALL, end="")
            elif tablero[i][j] == "O":
                print(Fore.LIGHTGREEN_EX + " " + tablero[i][j] + " " + Style.RESET_ALL, end="")
            else:
                print(Fore.LIGHTBLACK_EX + " " + str(i * 3 + j + 1) + " " + Style.RESET_ALL, end="")

        print()


def verificar_ganador(tablero):
    ganador = None
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            ganador = tablero[i][0]
            return ganador

    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] != " ":
            ganador = tablero[0][j]
            return ganador

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        ganador = tablero[0][0]
        return ganador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        ganador = tablero[0][2]
        return ganador


def pedir_posicion_usuario(tabla):
    while True:
        try:
            posicion_usuario = int(input("Ingrese una posición entre 1 y 9: "))
            posicion_usuario -= 1
            if posicion_usuario < 0 or posicion_usuario > 8:
                raise ValueError
            fila = posicion_usuario // 3
            columna = posicion_usuario % 3
            if tabla[fila][columna] != ' ':
                raise ValueError
            break

        except ValueError:
            print("Posición inválida. Intente nuevamente.")

    return (fila, columna)


def minimax(tabla, turno, contador): 
    ganador = verificar_ganador(tabla)
    if ganador == 'X':
        return (-10, None, None) 
    elif ganador == 'O':
        return (10, None, None) 
    elif contador == 9:
        return (0, None, None)
    
    mejor_valor = None 
    mejor_fila = None 
    mejor_columna = None 
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == ' ':
                tabla[i][j] = turno 
                contador += 1  
                if turno == 'O':  
                    valor = minimax(tabla, 'X', contador)[0]

                    if mejor_valor == None or valor > mejor_valor:
                        mejor_valor = valor
                        mejor_fila = i
                        mejor_columna = j

                else:
                    valor = minimax(tabla, 'O', contador)[0]

                    if mejor_valor == None or valor < mejor_valor:
                        mejor_valor = valor
                        mejor_fila = i
                        mejor_columna = j

                tabla[i][j] = ' ' 
                contador -= 1 

    return (mejor_valor, mejor_fila, mejor_columna)

def juego():
    tabla = inicializar_juego()
    turno = 'X'
    contador = 0

    while True:
        mostrar_tablero(tabla)

        if contador == 9:
            print("\nEmpate!")
            input("Press any key to continue...")
            break

        if turno == 'X':
            print("Turno del usuario")
            (fila, columna) = pedir_posicion_usuario(tabla)
            tabla[fila][columna] = 'X'
            turno = 'O'

        else:
            print("Turno del ordenador")
            (valor, fila, columna) = minimax(tabla, 'O', contador=contador)

            tabla[fila][columna] = 'O'

            turno = 'X'

        contador += 1
        ganador = verificar_ganador(tabla)

        if ganador != None:
            mostrar_tablero(tabla)
            print("\n", ganador, "ha ganado")
            input("Press any key to continue...")
            break

juego()     