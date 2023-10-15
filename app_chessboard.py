# from tkinter import *
#
#
# letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
# button_colors = ["yellow", "brown"]
#
# root = Tk()
# root.title("Chess board")
#
# i = 0
# while i < len(letters):
#     Button(root, text=letters[i], bg=button_colors[0]).grid(column=i, row=0, sticky=NSEW, ipadx=15)
#     Button(root, text=letters[i], bg=button_colors[0]).grid(column=i, row=9, sticky=NSEW, ipadx=15)
#     if i < 8:
#         Button(root, text=8-i, bg=button_colors[0]).grid(column=0, row=i+1, sticky=NSEW, ipadx=15)
#         Button(root, text=8-i, bg=button_colors[0]).grid(column=9, row=i+1, sticky=NSEW, ipadx=15)
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=1, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=1, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=2, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=2, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=3, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=3, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=4, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=4, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=5, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=5, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=6, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=6, sticky=NSEW, ipadx=15)\
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=7, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=7, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=8, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=8, sticky=NSEW, ipadx=15)
#     i += 1
#
# root.mainloop()
#
# # 8-0 =8
# # 8-1 =7
# # 8-2 =6
# # 8-3 =5
# # 8-4 =4
# # 8-5 =3
# # 8-6 =2
# # 8-7 =1
#
#
# from tkinter import *
#
#
# letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
# button_colors = ["yellow", "brown"]
#
# root = Tk()
# root.title("Chess board")
#
# i = 0
# while i < len(letters):
#     Button(root, text=letters[i], bg=button_colors[0]).grid(column=i, row=0, sticky=NSEW, ipadx=15)
#     Button(root, text=letters[i], bg=button_colors[0]).grid(column=i, row=9, sticky=NSEW, ipadx=15)
#     if i < 8:
#         Button(root, text=8-i, bg=button_colors[0]).grid(column=0, row=i+1, sticky=NSEW, ipadx=15)
#         Button(root, text=8-i, bg=button_colors[0]).grid(column=9, row=i+1, sticky=NSEW, ipadx=15)
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=1, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=1, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=2, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=2, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=3, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=3, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=4, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=4, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=5, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=5, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=6, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=6, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=7, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=7, sticky=NSEW, ipadx=15)
#
#         if i % 2:
#             Button(root, bg=button_colors[0]).grid(column=i+1, row=8, sticky=NSEW, ipadx=15)
#         else:
#             Button(root, bg=button_colors[1]).grid(column=i+1, row=8, sticky=NSEW, ipadx=15)
#     i += 1
#
# root.mainloop()


import tkinter as tk
import tkinter.ttk as ttk

letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
button_colors = ["yellow", "brown", "white", "black", "blue", "#5555ff", "#55ff55", "red", "green"]
buttons = []


def clear_chessboard():
    y = 0
    # print(y < len(buttons))
    # print(y, len(buttons))
    while y < len(buttons):
        # buttons[y].config(text=y)
        # print(y, y%18)
        if y % 2 and y%16 < 8 or not y % 2 and 8 <= y % 16 <= 15:
            buttons[y].config(highlightbackground=button_colors[1])
    #     if x * a + x * b + x * c + x * d:
    #     if x * (a + b + c + d):
        if y % 2 and (y < 8 or 16 <= y < 24 or 32 <= y < 40 or 48 <= y < 56) \
                or not y % 2 and (8 <= y < 16 or 24 <= y < 31 or 40 <= y < 47 or 56 <= y < 63):
            buttons[y].config(highlightbackground=button_colors[1], bg=button_colors[1])
        else:
            buttons[y].config(highlightbackground=button_colors[0], bg=button_colors[0])
        if y % 2 and 8 <= y % 16 <= 15 or not y % 2 and y % 16 < 8:
            buttons[y].config(highlightbackground=button_colors[0], bg=button_colors[0])
        else:
            buttons[y].config(highlightbackground=button_colors[1], bg=button_colors[1])

        y += 1


def paint_horizontal():
    clear_chessboard()
    x = 0
    while x < len(buttons):
        # print((9-(x%8+1))*8)
        # print(8-x//8 == 7)
        # print(list(entry_field.get()))
        # print(str(8-x//8))
        # print(button_colors)
        # print(button_colors[4])
        # print(type(list(entry_field.get())[1]))
        # print(type(str(8-x//8)))
        # print(type(button))
        # print(button_colors)
        # print(button_colors[4])
        if str(8-x//8) == list(entry_field.get())[1]:
            buttons[x].config(highlightbackground=button_colors[4], bg=button_colors[4])
        x += 1


def paint_vertical():
    clear_chessboard()
    y = 0
    # print(y%8+1)
    # print(entry_field.get()[0])
    print(letters.index(entry_field.get()[0]))
    # print(letters.index("A"))
    while y < len(buttons):
        if y%8+1 == letters.index(entry_field.get()[0]):
            buttons[y].config(highlightbackground=button_colors[4], bg=button_colors[4])
        y += 1


def paint_cell():
    clear_chessboard()
    x = 0
    # print(str(8-x//8))
    while x < len(buttons):
        if str(8-x//8) == list(entry_field.get())[1] and x%8+1 == letters.index(entry_field.get()[0]):
            buttons[x].config(highlightbackground=button_colors[4], bg=button_colors[4])
        x += 1


def paint_castle():
    clear_chessboard()
    x = 0
    while x < len(buttons):
        horizontal_line = str(8 - x // 8) == list(entry_field.get())[1]
        vertical_line = x % 8 + 1 == letters.index(entry_field.get()[0])
        paint_odd_cell = x % 2 and 8 <= x % 16 <= 15 or not x % 2 and x % 16 < 8
        paint_even_cell = not paint_odd_cell

        if horizontal_line and vertical_line:
            buttons[x].config(bg=button_colors[6])
        # h * o + v * o = o*(h+v)
        elif paint_odd_cell and (horizontal_line or vertical_line):
            buttons[x].config(bg=button_colors[5])
        elif paint_even_cell and (horizontal_line or vertical_line):
            buttons[x].config(bg=button_colors[4])

        x += 1


def paint_main_diagonal():
    clear_chessboard()
    cell = entry_field.get()
    i = 0
    while i < len(buttons):
        paint_odd_cell = i % 2 and 8 <= i % 16 <= 15 or not i % 2 and i % 16 < 8
        paint_even_cell = not paint_odd_cell
        # print(i, i//8, i%8, i//8 == i%8)
        # print(i, i//8, i%8, i//8+letters.index(cell[0])-1 == i%8)
        # print(9-int(list(cell)[1]))
        num_button_horizontal = i//8
        num_button_vertical = i%8
        num_letter_horizontal = letters.index(cell[0])
        num_letter_vertical = 9-int(list(cell)[1])
        main_diagonal = num_button_horizontal+num_letter_horizontal == num_button_vertical+num_letter_vertical
        if paint_even_cell and main_diagonal:
            buttons[i].config(bg=button_colors[8])
        elif paint_odd_cell and main_diagonal:
            buttons[i].config(bg=button_colors[6])

        i += 1


def paint_second_diagonal():
    clear_chessboard()
    cell = entry_field.get()
    i = 0
    while i < len(buttons):
        paint_odd_cell = i % 2 and 8 <= i % 16 <= 15 or not i % 2 and i % 16 < 8
        paint_even_cell = not paint_odd_cell
        num_button_horizontal = 7 - i // 8
        num_button_vertical = i % 8
        num_letter_horizontal = letters.index(cell[0])
        num_letter_vertical = int(list(cell)[1])
        second_diagonal = num_button_horizontal+num_letter_horizontal == num_letter_vertical+num_button_vertical
        if paint_even_cell and second_diagonal:
            buttons[i].config(bg=button_colors[8])
        elif paint_odd_cell and second_diagonal:
            buttons[i].config(bg=button_colors[6])
        i += 1


def paint_elephant():
    clear_chessboard()
    cell = entry_field.get()
    i = 0
    while i < len(buttons):
        main_diagonal = i//8 + letters.index(cell[0]) == i%8 + (9-int(list(cell)[1]))
        second_diagonal = (7 - i//8) + letters.index(cell[0]) == i%8 + int(list(cell)[1])
        odd_cell = i % 2 and 8 <= i % 16 <= 15 or not i % 2 and i % 16 < 8
        even_cell = not odd_cell
        if main_diagonal and second_diagonal:
            buttons[i].config(bg=button_colors[3])
        elif odd_cell and (main_diagonal or second_diagonal):
            buttons[i].config(bg=button_colors[6])
        elif even_cell and (main_diagonal or second_diagonal):
            buttons[i].config(bg=button_colors[8])

        i += 1


def paint_queen():
    clear_chessboard()
    cell = entry_field.get()
    x = 0
    # print(str(8-x//8))
    while x < len(buttons):
        horizontal_line = str(8 - x // 8) == list(entry_field.get())[1]
        vertical_line = x % 8 + 1 == letters.index(entry_field.get()[0])
        main_diagonal = x // 8 + letters.index(cell[0]) == x % 8 + (9 - int(list(cell)[1]))
        second_diagonal = (7 - x // 8) + letters.index(cell[0]) == x % 8 + int(list(cell)[1])
        paint_odd_cell = x % 2 and 8 <= x % 16 <= 15 or not x % 2 and x % 16 < 8
        paint_even_cell = not paint_odd_cell
        if horizontal_line and vertical_line:
            buttons[x].config(bg=button_colors[6])
        elif paint_odd_cell and (horizontal_line or vertical_line):
            buttons[x].config(bg=button_colors[5])
        elif paint_even_cell and (horizontal_line or vertical_line):
            buttons[x].config(bg=button_colors[4])
        elif main_diagonal and second_diagonal:
            buttons[x].config(bg=button_colors[3])
        elif paint_odd_cell and (main_diagonal or second_diagonal):
            buttons[x].config(bg=button_colors[6])
        elif paint_even_cell and (main_diagonal or second_diagonal):
            buttons[x].config(bg=button_colors[8])
        x += 1


def paint_king():
    clear_chessboard()
    cell = entry_field.get()
    i = 0
    while i < len(buttons):
        # print(i, 8-i//8, 8-i//8-1<=int(list(cell)[1])<=8-i//8+1)
        # print(i, i%8+1, i%8<=letters.index(cell[0])<= i%8+2)
        odd_cell = i % 2 and 8 <= i % 16 <= 15 or not i % 2 and i % 16 < 8
        even_cell = not odd_cell
        vertical_cells = i%8<=letters.index(cell[0])<= i%8+2
        horizontal_cells = 8-i//8-1<=int(list(cell)[1])<=8-i//8+1
        if odd_cell and (horizontal_cells and vertical_cells):
            buttons[i].config(bg=button_colors[2])
        elif even_cell and (horizontal_cells and vertical_cells):
            buttons[i].config(bg=button_colors[3])
        elif str(8-i//8) == list(entry_field.get())[1] and i%8+1 == letters.index(entry_field.get()[0]):
            buttons[i].config(bg=button_colors[7])
        i += 1


def paint_horse():
    clear_chessboard()
    cell = entry_field.get()
    i = 0
    while i < len(buttons):
        center_vertical = letters.index(cell[0])
        center_horizontal = int(list(cell)[1])
        vertical_line = i % 8 + 1
        horizontal_line = 8 - i // 8
        vertical_shift_right2 = center_vertical + 2 == i % 8 + 1
        vertical_shift_left2 = center_vertical - 2 == i % 8 + 1
        vertical_shift_right1 = center_vertical + 1 == i % 8 + 1
        vertical_shift_left1 = center_vertical - 1 == i % 8 + 1
        horizontal_shift_up1 = center_horizontal + 1 == horizontal_line
        horizontal_shift_down1 = center_horizontal - 1 == horizontal_line
        horizontal_shift_up2 = center_horizontal + 2 == horizontal_line
        horizontal_shift_down2 = center_horizontal - 2 == horizontal_line
        horizontal_shift_up = horizontal_shift_up2 and (vertical_shift_right1 or vertical_shift_left1)
        horizontal_shift_down = horizontal_shift_down2 and (vertical_shift_right1 or vertical_shift_left1)
        vertical_shift_right = vertical_shift_right2 and (horizontal_shift_up1 or horizontal_shift_down1)
        vertical_shift_left = vertical_shift_left2 and (horizontal_shift_up1 or horizontal_shift_down1)
        horse_all_steps = horizontal_shift_up or horizontal_shift_down or vertical_shift_right or vertical_shift_left
        cell_dark = i % 2 and 8 <= i % 16 <= 15 or not i % 2 and i % 16 < 8
        cell_light = not cell_dark

        if center_vertical == vertical_line and center_horizontal == horizontal_line:
            buttons[i].config(bg=button_colors[3])

        elif cell_dark and horse_all_steps:
            buttons[i].config(bg=button_colors[6])

        elif cell_light and horse_all_steps:
            buttons[i].config(bg=button_colors[8])

        i += 1


root = tk.Tk()
root.title("Chess board")


i = 0
while i < len(letters):
    label = tk.Label(root, text=letters[i], bg=button_colors[0], fg="black")
    label.grid(column=i, row=0, sticky="NSEW", ipadx=15)
    label = tk.Label(root, text=letters[i], bg=button_colors[0], fg="black")
    label.grid(column=i, row=9, sticky="NSEW", ipadx=15)
    if i < 8:
        label = tk.Label(root, text=8 - i, bg=button_colors[0], fg="black")
        label.grid(column=0, row=i + 1, sticky="NSEW", ipadx=15)
        label = tk.Label(root, text=8 - i, bg=button_colors[0], fg="black")
        label.grid(column=9, row=i + 1, sticky="NSEW", ipadx=15)
    i += 1


y = 0
while y < 8:
    x = 0
    while x < 8:
        if not x % 2 and not y % 2 or x % 2 and y % 2:
            button = tk.Button(root, text=f" ", highlightbackground=button_colors[0], bg=button_colors[0])
            button.grid(row=y+1, column=x+1, sticky="NSEW")
        else:
            button = tk.Button(root, text=f" ", highlightbackground=button_colors[1], bg=button_colors[1])
            button.grid(row=y+1, column=x+1, sticky="NSEW")

        buttons.append(button)
        x += 1
    y += 1


entry_field = tk.Entry()
entry_field.grid(column=11, row=0)
ttk.Button(text="repaint chessboard", command=clear_chessboard).grid(column=11, row=1, sticky="NSEW")
ttk.Button(text="paint cell", command=paint_cell).grid(column=11, row=2, sticky="NSEW")
ttk.Button(text="paint horizont", command=paint_horizontal).grid(column=11, row=3, sticky="NSEW")
ttk.Button(text="paint vertical", command=paint_vertical).grid(column=11, row=4, sticky="NSEW")
ttk.Button(text="paint castle", command=paint_castle).grid(column=11, row=5, sticky="NSEW")
ttk.Button(text="paint main diagonal", command=paint_main_diagonal).grid(column=11, row=6, sticky="NSEW")
ttk.Button(text="paint second diagonal", command=paint_second_diagonal).grid(column=11, row=7, sticky="NSEW")
ttk.Button(text="paint elephant", command=paint_elephant).grid(column=11, row=8, sticky="NSEW")
ttk.Button(text="paint queen", command=paint_queen).grid(column=11, row=9, sticky="NSEW")
ttk.Button(text="paint king", command=paint_king).grid(column=11, row=10, sticky="NSEW")
ttk.Button(text="paint horse", command=paint_horse).grid(column=11, row=11, sticky="NSEW")
root.mainloop()

