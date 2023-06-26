from pandastable import Table
import tkinter as tk
import pandas as pd
from services.setsService import SetsService


class ViewTableSetsResults:
    def __init__(self, data_array, window):
        self.__w__ = window
        self.__data__ = data_array
        self.__number__ = []

    def __table_sets_results__(self):
        try:
            [self.__number__.append(self.__data__[x][1]) for x in range(len(self.__data__))]
            __data_table__ = SetsService(self.__data__).__data_sets__()
            data_sets_table = pd.DataFrame(__data_table__, columns=range(1, self.__number__.__getitem__(0) + 1))
            __window__ = tk.Toplevel(self.__w__)
            table = Table(__window__, dataframe=data_sets_table)
            table.show()
        except IndexError:
            print("unu")
