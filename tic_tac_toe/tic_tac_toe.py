
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

def print_board():

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# GETS USER INPUT AND DETERMINES IF VALID
def pick_position():
    desired_position = input("Choose a position to place your mark. (1-9)")

    if ((0 <= player_position) and (player_position <= 9)):
        update_board(desired_position)
    else:
        print("Invalid choice. You must choose a position from 1 - 9")
        choose_position()

# UPDATES THE BOARD ARRAY WITH THE NEW POSITION
def update_board(pos_choice):
    board[pos_choice] = 'X' # or 'O' ... the mark belonging to the current player
    print_board()
