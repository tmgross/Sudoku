from Sudoku import *
import tkinter as tk
from functools import partial

if __name__ == '__main__':
    board = Sudoku(9, 40)
    board.generate_board()
    board.print()

    win = tk.Tk()
    win.title('Sudoku')
    win.resizable(width=False, height=False)


    def color_config(widget, color, event):
        widget.configure(background=color)


    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    def change_number(widget, event):
        if event.char in numbers:
            widget.delete(1.0, tk.END)
            widget.insert(1.0, event.char, "center")
        return "break"


    colors = [['#999997', '#595958', '#999997'],
              ['#595958', '#999997', '#595958'],
              ['#999997', '#595958', '#999997']]
    rows = []
    for i in range(9):
        cols = []
        for j in range(9):
            e = tk.Text(win, height=3, width=6, relief='groove', cursor="arrow",
                        background=colors[i // 3][j // 3], font=('Roboto', 15, "bold"))
            e.tag_configure("center", justify="center")
            e.insert(tk.END, board.get_value(i, j), "center")

            if board.get_value(i, j) != 0:
                e.configure(state=tk.DISABLED, foreground="CYAN")

            e.bind("<KeyPress>", partial(change_number, e))
            e.bind("<Enter>", partial(color_config, e, '#7D7E8C'))
            e.bind("<Leave>", partial(color_config, e, colors[i // 3][j // 3]))
            e.grid(row=i, column=j, sticky=tk.NSEW)
            cols.append(e)
        rows.append(cols)

    win.mainloop()
