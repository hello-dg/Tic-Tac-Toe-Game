import random

pc_selection = random.randint(1,9)

spaces_played = []


def game_grid(sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9):
    top_vert_line = f" {sp7} | {sp8} | {sp9} "
    top_horz_line = f"--- --- ---"
    middle_vert_line = f" {sp4} | {sp5} | {sp6} "
    bottom_horz_line = f"--- --- ---"
    bottom_vert_line = f" {sp1} | {sp2} | {sp3} "

    print(f"{top_vert_line}\n{top_horz_line}\n{middle_vert_line}\n{bottom_horz_line}\n{bottom_vert_line}")


def game_play(user_symbol, pc_symbol):
    game_grid(" "," "," "," "," "," "," "," "," ")


game_play(1,2)

game_over = False
while not game_over:
    print("Let's play Tic Tac Toe!")
    correct_option = False
    while not correct_option:
        option_selected = int(input("\nOptions:\nPress 1 to be X's\nPress 2 to be O's\nPress 3 to Learn How to Play\n"))
        if option_selected == 1:
            pass
        elif option_selected == 2:
            pass
        elif option_selected == 3:
            print("\nTic Tac Toe is a simple two-player game played on a 3x3 grid.\n"
                  "The players take turns marking a space on the grid with their symbol—either 'X' or 'O'.\n"
                  "The objective is to be the first player to get three of their symbols in a row, either\n"
                  "horizontally, vertically, or diagonally. If all nine spaces are filled without any player\n"
                  "achieving this, the game ends in a draw.\n")
            print("To choose which space to put your symbol, use your keypad (1 through 9).\n"
                  "The grid is laid out to match the keypad. See below for the numeric values\n"
                  "of each space then look at your keypad.\n")
            print("Layout:")
            game_grid(1, 2, 3, 4, 5, 6, 7, 8, 9)
        else:
            print("\nIncorrect Selection... Try Again.\n")

    game_over = True