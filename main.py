from Sudoku import *
import tkinter as tk
from functools import partial

if __name__ == '__main__':
    board = Sudoku(9, 20)
    board.generate_board()
    board.print()

    win = tk.Tk()
    win.title('Sudoku')

    def color_config(widget, color, event):
        widget.configure(background=color)

    colors = [['#999997', '#595958', '#999997'],
              ['#595958', '#999997', '#595958'],
              ['#999997', '#595958', '#999997']]
    rows = []
    for i in range(9):
        cols = []
        for j in range(9):
            e = tk.Label(win, text=board.get_value(i, j), height=3, width=6, relief='groove',
                         background=colors[i // 3][j // 3], font=('Roboto', 15, "bold"))
            e.bind("<Enter>", partial(color_config, e, '#7D7E8C'))
            e.bind("<Leave>", partial(color_config, e, colors[i // 3][j // 3]))
            e.grid(row=i, column=j, sticky=tk.NSEW)
            cols.append(e)
        rows.append(cols)

    win.mainloop()