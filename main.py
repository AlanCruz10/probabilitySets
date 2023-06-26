import tkinter as tk
from views.viewDataSets import ViewDataSets


class Main:
    def __init__(self):
        def rgb2hex():
            return '#%02x%02x%02x' % (120, 200, 225)

        self.window = tk.Tk()
        self.window.geometry("1366x768")
        self.window.title("ProbabilitySets")
        self.window.configure(bg=rgb2hex())

    def view_window(self):
        ViewDataSets(self.window)
        self.window.mainloop()


main = Main()
main.view_window()
