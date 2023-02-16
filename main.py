from Sudoku import *
import tkinter as tk
from functools import partial


def color_config(widget, color, event):
    widget.configure(bg=color)


def change_number(widget, event):
    if event.char in numbers:
        widget.delete(1.0, tk.END)
        widget.insert(1.0, event.char, "center")
    return "break"


def check_board():
    return True


if __name__ == '__main__':
    board = Sudoku(9, 40)
    board.generate_board()

    win = tk.Tk()
    win.title('Sudoku')
    win.configure(bg="#595958")
    win.resizable(width=False, height=False)

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    colors = [['#999997', '#595958', '#999997'],
              ['#595958', '#999997', '#595958'],
              ['#999997', '#595958', '#999997']]
    rows = []

    # create grid of text widgets to display and accept user input of sudoku board

    for i in range(9):
        cols = []
        for j in range(9):
            # configure text field parameters
            e = tk.Text(win, height=3, width=6, relief='ridge', cursor="arrow",
                        bg=colors[i // 3][j // 3], font=("Roboto", 15, "bold"), fg="CYAN")
            e.tag_configure("center", justify="center")
            e.insert(tk.END, board.get_value(i, j), "center")

            # if the cell contains a number that is not 0, remove user ability to change it
            if board.get_value(i, j) != 0:
                e.configure(state=tk.DISABLED, fg="BLACK")

            # assign different actions to the text field
            e.bind("<KeyPress>", partial(change_number, e))
            e.bind("<Enter>", partial(color_config, e, '#7D7E8C'))
            e.bind("<Leave>", partial(color_config, e, colors[i // 3][j // 3]))

            # add text field to the grid
            e.grid(row=i, column=j, sticky=tk.NSEW)
            cols.append(e)
        rows.append(cols)

    check_board = tk.Button(win, height=3, width=10, text="Check", font=("Roboto", 13, "bold"), bg="#999997",
                            command=check_board)
    check_board.grid(row=0, column=9, sticky=tk.NSEW)

    clear_board = tk.Button(win, height=3, width=10, text="Clear", font=("Roboto", 13, "bold"), bg="#595958")
    clear_board.grid(row=1, column=9, sticky=tk.NSEW)

    quit_btn = tk.Button(win, height=3, width=10, text="Quit", font=("Roboto", 13, "bold"), command=win.destroy,
                         bg="#999997")
    quit_btn.grid(row=2, column=9, sticky=tk.NSEW)

    win.mainloop()
