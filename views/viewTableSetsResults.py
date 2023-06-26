from pandastable import Table
import tkinter as tk
import pandas as pd
from services.setsService import SetsService
from views.viewProbability import ViewProbability
__first_time__ = True
__total_sets_text__ = None
__window__ = None


class ViewTableSetsResults:
    def __init__(self, data_array, window):
        self.__w__ = window
        self.__data__ = data_array
        self.__number__ = []
        self.__total_sets__ = 0
        self.total_sets = ""
        self.__data_table__ = []

    def __table_sets_results__(self):
        try:
            global __first_time__, __total_sets_text__, __window__
            if __first_time__:
                self.__table_data__()
                ViewProbability(self.__w__)
                __first_time__ = False
            else:
                __window__.destroy()
                __total_sets_text__.destroy()
                self.__table_data__()
        except IndexError:
            print("unu")

    def __table_data__(self):
        global __total_sets_text__, __window__
        [self.__number__.append(self.__data__[x][1]) for x in range(len(self.__data__))]
        self.__data_table__ = SetsService(self.__data__).__data_sets__()
        data_sets_table = pd.DataFrame(self.__data_table__, columns=range(1, self.__number__.__getitem__(0) + 1))
        __window__ = tk.Toplevel(self.__w__)
        table = Table(__window__, dataframe=data_sets_table)
        table.show()
        self.__total_sets__ = SetsService(self.__data__).__total_sets_value__()
        self.total_sets = str((" Numero total de combinaciones: ", self.__total_sets__))
        __total_sets_text__ = tk.Label(self.__w__, text=self.total_sets, background="blue", foreground="white", bd=10)
        __total_sets_text__.place(anchor="n", x=300, y=70)
