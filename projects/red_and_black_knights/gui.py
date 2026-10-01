"""
Uli, jeg har lavet Red and Black Knights.

Jeg har ikke læst opgaven, så det, jeg ved, er ud fra det, Kjartan har fortalt mig.

For at starte programmet skal du ændre `Game` og `Board` nede i `if __name__ == "__main__":`.

"""

import tkinter as tk
from tkinter import ttk, Scrollbar
import math

from red_and_black_knights import Board, Game

squares = {}

def display_the_spiral():
    ring = outer_ring_Len
    steps_taken_on_ring = 0
    side = 0
    row = int(outer_ring_Len)
    col = 0

    for i in range(len(board.board)):
        # Turn logic
        if (steps_taken_on_ring == ring and side == 0):
            side += 1
            steps_taken_on_ring = 0
        elif (steps_taken_on_ring == ring - 1 and side != 0 and side != 3):
            side += 1
            steps_taken_on_ring = 0
        elif (steps_taken_on_ring == ring - 2 and side == 3):
            side += 1
            steps_taken_on_ring = 0
        # Layer shift
        if side == 4:
            side = 0
            ring -= 2

        # row/col logic
        if side == 0:
            row -= 1
        elif side == 1:
            col += 1
        elif side == 2:
            row += 1
        elif side == 3:
            col -= 1

        square = tk.Label(
            board_frame,
            text=len(board.board)-i-1,
            bg="white",
            width=4,
            height=2,
            relief="solid",
            borderwidth=1
        )

        square.grid(row=row,column=col)
        squares[len(board.board)-i-1] = square
        steps_taken_on_ring +=1

def display_the_knights():
    for i in range(len(board.board)):
        if i in board.knights:
            knight_color = board.knights[i].color
            squares[i].config(bg=knight_color)

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title("Knights")
    main_window.geometry("1080x1080")

    canvas = tk.Canvas(main_window)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x = tk.Scrollbar(main_window, orient="horizontal", command=canvas.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    board_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=board_frame, anchor="nw")

    board = Board(91) #Any odd number and it would give you the amount from 0 to the number^2 - 1 - The grid size
    board.board_creation()
    outer_ring_Len = math.sqrt(len(board.board))

    display_the_spiral()

    board_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    game = Game(3, board) #The number represents the number of knights. For now, 5 is the maximum because I haven't decided how I want to implement it yet. This is the engine that runs the program.
    while game.try_place_knight():
     pass

    display_the_knights()
    main_window.mainloop()