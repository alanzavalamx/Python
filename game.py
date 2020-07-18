import random

winPos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
table_board = set([1,2,3,4,5,6,7,8,9])
ai_start = True #TRUE SI LA PC INICIA, FALSE SI LA PERSONA INICIA
ai_pass = set()
person_pass = set()


def winnerWays(pass_movements):
    #REVISA SI ALGUIEN GANO
    for subset in winPos:
        count = 0
        for movements in pass_movements:
            if movements in subset:
                count += 1
        if count == 3:
            return True
    return False

def winner(winPos, ai_pass,person_pass):
    #RETORNA EL GANADOR
    if winnerWays(ai_pass):
        print('LA PC GANO')
        return True
    if winnerWays(person_pass):
        print('TU GANASTE')
        return True
    
    return False

def isInWinWays(table_board,an_pass,winPos):
    #REVISA SI EL AI O LA PERSONA TIENE POSIBILIDADES DE GANAR EN EL SIGUIENTE MOVIMIENTO
    maybe_win = []

    for subset in winPos:
        count = 0
        sub_maybe = set()
        for movement in an_pass:
            if movement in subset:
                sub_maybe.add(movement)
                count += 1
        if count == 2:
            value = next(iter(set(subset) - sub_maybe) )
            if value in table_board:
                maybe_win.append(value)

    return maybe_win

def theyNeverWins(table_board,ai_pass,person_pass, winPos):
    #RETORNA LOS MOVIMIENTOS QUE HACEN GANAR A LA PC O A LA PERSONA EN EL SIGUIENTE MOVIMIENTO
    maybe_win_ai = isInWinWays(table_board,ai_pass,winPos)
    maybe_win_person = isInWinWays(table_board,person_pass,winPos)

    return maybe_win_ai, maybe_win_person

def AiSelection(table_board, winPos, ai_pass, person_pass):

    mov_list = []
    ai_win, blok_person = theyNeverWins(table_board,ai_pass,person_pass, winPos)

    if len(ai_win) > 0:
        n = next(iter(ai_win))
        print(f'COMPUTADORA SELECCIONO EL {n}')
        return n

    if len(blok_person) > 0:
        n = next(iter(blok_person))
        print(f'COMPUTADORA SELECCIONO EL {n}')
        return n
    

    #SELECCION DEL CENTRO
    if 5 in table_board:
        print('COMPUTADORA SELECCIONO EL 5')
        return 5
    
    count = 0
    for i in person_pass:
        if i in [1,3,7,9]:
            count += 1
        if count > 1:
            for x in table_board:
                if x in [2,4,6,8]:
                    print(f'COMPUTADORA SELECCIONO EL {x}')
                    return x

    #SELECCION DE ESQUINAS 
    for i in table_board:
        if i in [1,3,7,9]:
            mov_list.append(i)
        if len(mov_list) > 0:
            n = random.choice(mov_list)
            print(f'COMPUTADORA SELECCIONO EL {n}')
            return n

    #SELECCION DE CENTROS LATERALES 
    for i in table_board:
        if i in [2,4,6,8]:
            mov_list.append(i)
        if len(mov_list) > 0:
            n = random.choice(mov_list)
            print(f'COMPUTADORA SELECCIONO EL {n}')
            return n

def game(table_board,winPos, pos_selected):
    error = False
    if (pos_selected >= 1) and (pos_selected <= 9):
        if pos_selected in table_board:
           table_board.remove(pos_selected)
        else:
            print('Esa casilla ya esta ocupada.')
            error = True
    else:
        print('Seleeciona un valor entre 0 y 9')
        error = True
    return error

while len(table_board) > 0:
    print(table_board)
    if ai_start:
        print('JUGADOR ACTUAL: COMPUTADORA')
        pos_selected = AiSelection(table_board,winPos, ai_pass, person_pass)
        error = game(table_board, winPos, pos_selected)
        if not error:
            ai_pass.add(pos_selected)
            print('PC PASS', ai_pass)
            ai_start = False
        else:
            break
    else:
        print('JUGADOR ACTUAL: DORYAN')
        pos_selected = int(input('Selecciona una casilla: '))
        error = game(table_board, winPos, pos_selected)

        if not error:
            person_pass.add(pos_selected)
            print('PERSON PASS', person_pass)
            ai_start = True

    if winner(winPos, ai_pass,person_pass):
        break
    if len(table_board) == 0:
        print('EL JUEGO ES UN EMPATE.')
