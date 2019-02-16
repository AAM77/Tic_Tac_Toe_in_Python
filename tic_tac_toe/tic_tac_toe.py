
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = ["",""]
count = 1

def current_player():
    if count % 2 == 0:
        return players[1]
    else:
        return players[0]


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
def choose_x_or_o():

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
        choose_x_or_o()

    set_players(player_choice)


# SETS THE PLAYERS_1 and PLAYER_2 to
def set_players(player_choice):
    if player_choice.upper() == 'X':
        players[0] = 'X'
        players[1] = 'O'
    else:
        player[0] = 'O'
        player[1] = 'X'


# PRINTS THE BOARD

def print_board():

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# GETS USER INPUT AND DETERMINES IF VALID
def pick_position():
    desired_position = int(input("Choose an open position. (1-9)"))

    if ((1 <= desired_position) and (desired_position <= 9)):
        board_index = desired_position - 1
        update_board(board_index)
    else:
        print("Invalid choice. You must choose a position from 1 - 9")
        pick_position()

# UPDATES THE BOARD ARRAY WITH THE NEW POSITION
def update_board(pos_choice):
    if is_valid(pos_choice):
        board[pos_choice] = current_player() # or 'O' ... the mark belonging to the current player
        print_board()
    else:
        print("Invalid choice. That position is taken.")
        pick_position()

# CHECKS IF THE CHOSEN POSITION IS VALID
def is_valid(pos_choice):
    if board(pos_choice) == 'X' or board(pos_choice) == 'O':
        return True
    else:
        return False

def take_turn(board_index):
    # check for winning combinations
        # if winning combo:
            # declare winner
        # else:
            #if all positions filled with 'X' or 'O'
                # declare a tie
                # end_game()
            # else:
                # pick_position()
                # update_count()

def update_turn():
    count += 1

def winning_combos():
    return []

def end_game():
    # do something at the end
    pass

def check_for_combos():
    # check if the board contains any of the winning combos
    pass

def check_board():
    if all(item == 'X' or item == 'O' for item in board):
        end_game()
    else:
        next_turn()
