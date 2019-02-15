
player_1 = ''
player_2 = ''

# GREETS THE PLAYER
def greet_player():
    print("Welcome to Tic-Tac-Toe")

# PRINTS THE GAME LOGO
def print_game_logo():

    title = """
    #######  #######   ######
       #        #      #
       #        #      #
       #        #      #
       #     #######   ######

    #######   ####     ######
       #     #    #    #
       #     ######    #
       #     #    #    #
       #     #    #    ######

    #######   ####     ######
       #     #    #    #
       #     #    #    ######
       #     #    #    #
       #      ####     ######
    """

    print(title)


    # ASKS THE PLAYER TO CHOOSE X or O
def choose_player():

    player_choice = input("Do you want to be 'X' or 'O'?").upper()

    if player_choice == 'X':
        print("You are now 'X', Player One.")
        print("Player two is 'O'.")
        print("Starting the game.")
    elif player_choice == 'O':
        print("You are now 'O', Player One.")
        print("Player two is 'X'.")
        print("Starting the game.")
    else:
        print("Incorrect choice. Choose 'X' or 'O'")
        choose_player()

    set_players(player_choice)


# SETS THE PLAYERS_1 and PLAYER_2 to
def set_players(player_choice):
    if player_choice.upper() == 'X':
        player_1 = 'X'
        player_2 = 'O'
    else:
        player_1 = 'O'
        player_2 = 'X'


# PRINTS THE BOARD

def print_board(pos):

    pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    print(f" {pos[0]} | {pos[1]} | {pos[2]} ")
    print("-----------")
    print(f" {pos[3]} | {pos[4]} | {pos[5]} ")
    print("-----------")
    print(f" {pos[6]} | {pos[7]} | {pos[8]} ")


def pick_position():
    player_position = input("Where do you want to put your mark? (1-9)")

    if ((0 <= player_position) and (player_position <= 9)):
        #update_board(player_position)
    else:
        print("Invalid choice. You must choose a position from 1 - 9")
        choose_position()
