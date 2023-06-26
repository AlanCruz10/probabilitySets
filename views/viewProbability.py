from pandastable import Table
import tkinter as tk
import pandas as pd


class ViewProbability:
    def __init__(self, window):
        self.__w__ = window
        self.__table_sentence__ = pd.DataFrame(columns=['Sentencia', 'Resultado Fraccion', "Resultado Decimal"])
        self.__table_frame_sentence__ = tk.Frame(self.__w__)
        self.__table_frame_sentence__.place(anchor="center")
        self.__data_table_sentence__ = None
        self.__sentence_text__ = tk.Label(self.__w__, text="Sentencia")
        self.__sentence_text__.pack(anchor="center")
        self.__sentence_entry__ = tk.Entry(self.__w__)
        self.__sentence_entry__.pack(anchor="center")
        self.__sentence_button__ = tk.Button(self.__w__, text="Agregar sentencia",
                                             command=lambda: self.__add_sentence__(), background="green",
                                             foreground="white")
        self.__sentence_button__.pack(anchor="center")
        self.__sentence_array__ = []
        self.__solve_button = tk.Button(self.__w__, text="Resolver", command=lambda: self.__solve_sentence__(),
                                        background="red", foreground="white")
        self.__solve_button.pack(anchor="center", pady=5)

    def __add_sentence__(self):
        __sentence__ = self.__sentence_entry__.get()
        if __sentence__ != "":
            self.__sentence_array__.append(__sentence__)
            data = {'Sentencia': [__sentence__]}
            table_sentence = pd.DataFrame(data)
            self.__table_sentence__ = pd.concat([self.__table_sentence__, table_sentence], ignore_index=True)
            self.__data_table_sentence__ = Table(self.__table_frame_sentence__, dataframe=self.__table_sentence__,
                                                 stretch=True)
            self.__data_table_sentence__.autoResizeColumns()
            self.__data_table_sentence__.show()
            self.__table_frame_sentence__.update_idletasks()
            self.__table_frame_sentence__.pack(ipadx=100, ipady=25)

    def __solve_sentence__(self):
        try:
            solve_array = [1, 2, 3]
            if self.__sentence_array__.__len__() == solve_array.__len__():
                self.__table_sentence__['Resultado Fraccion'] = solve_array
                self.__table_sentence__['Resultado Decimal'] = solve_array
                self.__data_table_sentence__ = Table(self.__table_frame_sentence__, dataframe=self.__table_sentence__,
                                                     stretch=True)
                self.__data_table_sentence__.autoResizeColumns()
                self.__data_table_sentence__.show()
                self.__table_frame_sentence__.update_idletasks()
                self.__table_frame_sentence__.pack(ipadx=100, ipady=25)
        except ValueError:
            print("unu")
