# Tic Tac Toe (Python Terminal Game)

This is a fully interactive, terminal-based Tic Tac Toe game built in Python.  
It includes a user vs. computer mode, score tracking, win detection, board drawing, and an optional "How to Play" tutorial.

The game uses simple logic, random moves for the computer, and clean grid rendering to create a smooth text-based experience.  
Future enhancements include smarter AI blocking and improved difficulty levels.

---

## Features

- Play Tic Tac Toe in the terminal
- User vs Computer gameplay
- Automatically drawn board after every move
- Win, loss, and draw detection
- Live score tracking across multiple games
- Option to choose X or O
- "How to Play" instructions built in
- Clean, modular functions (grid drawing, win checking, game loop)
- Easily extendable logic for AI improvements

---

## Requirements

- Python 3.x  
No additional libraries are required.

---

## Installation

1. Clone or download the repository:

        git clone https://github.com/your-username/your-repo-name.git
        cd your-repo-name

2. Make sure your Python version is 3.x:

        python --version

3. Run the game:

        python tic_tac_toe.py

---

## How to Run

Start the game using:

        python tic_tac_toe.py

Then:

1. View the score  
2. View the numbered board layout  
3. Choose:
   - Press **1** → Play as X  
   - Press **2** → Play as O  
   - Press **3** → Learn how to play  
4. Enter a number (1–9) to place your piece  
5. Computer plays automatically  
6. Play again or exit  

---

## Example Gameplay Output

        Let's play Tic Tac Toe!

        Current Score is 0 - 0

        Here's the board game and spaces:
         7 | 8 | 9
        --- --- ---
         4 | 5 | 6
        --- --- ---
         1 | 2 | 3

        Options:
        Press 1 to be X's
        Press 2 to be O's
        Press 3 to Learn How to Play

        What space do you want to put your symbol? 5

        You played space 5:
         7 | 8 | 9
        --- --- ---
         4 | X | 6
        --- --- ---
         1 | 2 | 3

        The computer played space 2:
         7 | 8 | 9
        --- --- ---
         4 | X | 6
        --- --- ---
         1 | O | 3

…and so on until someone wins or the game draws.

---

## Code Overview

### Grid Drawing

The grid is printed using a formatted 3×3 layout that updates after every move:

        def game_grid(sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9):
            top_vert_line = f" {sp7} | {sp8} | {sp9} "
            top_horz_line = f"--- --- ---"
            middle_vert_line = f" {sp4} | {sp5} | {sp6} "
            bottom_horz_line = f"--- --- ---"
            bottom_vert_line = f" {sp1} | {sp2} | {sp3} "
            print(f"{top_vert_line}\n{top_horz_line}\n{middle_vert_line}\n{bottom_horz_line}\n{bottom_vert_line}")

### Win Checking

All winning combinations are stored and checked automatically:

        winning_plays = [
            (sp1, sp2, sp3), (sp4, sp5, sp6), (sp7, sp8, sp9),
            (sp1, sp4, sp7), (sp2, sp5, sp8), (sp3, sp6, sp9),
            (sp1, sp5, sp9), (sp7, sp5, sp3)
        ]

        if any(play == ("X", "X", "X") for play in winning_plays):
            print("X Wins!")
        elif any(play == ("O", "O", "O") for play in winning_plays):
            print("O Wins!")

### Core Game Loop

The game alternates between:
- User turn
- Computer turn (random selection)
- Grid redraw
- Win/draw checks
- Score updates

Global values track scores and spaces already played.

---

## Potential Future Improvements

- Smarter computer AI (block player wins)
- Multiple difficulty settings
- Highlight winning line
- Replay entire match history
- Option to play user vs user
- Add color to the terminal output
- Use classes instead of globals for cleaner structure

---

## License

This project is open source and available under the MIT License.

