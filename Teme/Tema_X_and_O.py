# User X and Computer O
counter = 9
game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = ''


def print_game_board():
    print(' {0}|{1}|{2}\n {3}|{4}|{5}\n {6}|{7}|{8}'
          .format(str(game_board[0]), str(game_board[1]), str(game_board[2]),
                  str(game_board[3]), str(game_board[4]), str(game_board[5]),
                  str(game_board[6]), str(game_board[7]), str(game_board[8])))


print(' 1|2|3\n 4|5|6\n 7|8|9')

while counter:
    #  Alege jucatorul
    user_x = int(input("  Alege o pozitie: "))
    if user_x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(" Introdu o pozitie corecta!")
        continue
    if game_board[user_x - 1] == ' ':
        game_board[user_x - 1] = 'X'
    else:
        print(" Pozitie ocupata! Reintrodu pozitia!")
        continue
    counter -= 1
    print_game_board()
    #  Verificam daca exista un castigator
    if counter < 6:
        for i in [0, 3, 6]:
            if game_board[i] == game_board[i + 1] == game_board[i + 2] and game_board[i] != ' ':
                winner = game_board[i]
                break
        for i in [0, 1, 2]:
            if game_board[i] == game_board[i + 3] == game_board[i + 6] and game_board[i] != ' ':
                winner = game_board[i]
                break
        if (game_board[0] == game_board[4] == game_board[8]) or \
                (game_board[2] == game_board[4] == game_board[6]) and game_board[4] != ' ':
            winner = game_board[4]
    if winner == 'X':
        print("   Ai castigat! :)")
        break
    elif winner == 'O':
        print("   Ai pierdut! :(")
        break
    #   Alege calculatorul
    priority_position = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for p in priority_position:
        if game_board[p - 1] == ' ':
            game_board[p - 1] = 'O'
            print("  Computerul a ales: {0}".format(p))
            counter -= 1
            break
    print_game_board()
