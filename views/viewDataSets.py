import tkinter as tk
import pandas as pd


class ViewDataSets:
    def __init__(self, window):
        self.w = window
        self.data_array = []
        self.tabla = pd.DataFrame(columns=['Cantidad', 'Numero'])
        self.amount_text = tk.Label(self.w, text="Ingrese cantidad")
        self.amount_text.pack()
        self.amount_entry = tk.Entry(self.w)
        self.amount_entry.pack()
        self.number_text = tk.Label(self.w, text="Ingrese numero")
        self.number_text.pack()
        self.number_entry = tk.Entry(self.w)
        self.number_entry.pack()
        self.add_button = tk.Button(self.w, text="Agregar datos", command=self.add_data)
        self.add_button.pack()

    def add_data(self):
        number = int(self.number_entry.get())
        amount = int(self.amount_entry.get())
        self.data_array.append((number, amount))
