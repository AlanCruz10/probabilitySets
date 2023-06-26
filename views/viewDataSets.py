import tkinter as tk
import pandas as pd
from pandastable import Table
from views.viewTableSetsResults import ViewTableSetsResults


class ViewDataSets:
    def __init__(self, window):
        self.__w__ = window
        self.__data_array__ = []
        self.__table__ = pd.DataFrame(columns=['Cantidad', 'Numero'])
        self.__amount_text__ = tk.Label(self.__w__, text="Ingrese cantidad")
        self.__amount_text__.pack()
        self.__amount_entry__ = tk.Entry(self.__w__)
        self.__amount_entry__.pack()
        self.__number_text__ = tk.Label(self.__w__, text="Ingrese numero")
        self.__number_text__.pack()
        self.__number_entry__ = tk.Entry(self.__w__)
        self.__number_entry__.pack()
        self.__add_button__ = tk.Button(self.__w__, text="Agregar datos", command=lambda: self.__add_data__())
        self.__add_button__.pack()
        self.__table_frame__ = tk.Frame(self.__w__)
        self.__table_frame__.place()
        self.__data_table__ = None
        self.__results_button__ = tk.Button(self.__w__, text="Ver Resultados", command=lambda: self.__results_data__())
        self.__results_button__.pack()

    def __add_data__(self):
        try:
            number = int(self.__number_entry__.get())
            amount = int(self.__amount_entry__.get())
            self.__data_array__.append((amount, number))
            data = {'Cantidad': [amount], 'Numero': [number]}
            data_sentence = pd.DataFrame(data)
            self.__table__ = pd.concat([self.__table__, data_sentence], ignore_index=True)
            if self.__data_table__ is not None:
                self.__data_table__.destroy()
            self.__data_table__ = Table(self.__table_frame__, dataframe=self.__table__, stretch=True)
            self.__data_table__.autoResizeColumns()
            self.__data_table__.show()
            self.__table_frame__.update_idletasks()
            self.__table_frame__.place_configure(anchor="w", y=300, width=230)
        except ValueError:
            print("unu")

    def __results_data__(self):
        try:
            ViewTableSetsResults(self.__data_array__, self.__w__).__table_sets_results__()
        except Exception:
            print("unu")
