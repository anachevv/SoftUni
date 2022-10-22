import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()
    # Create widgets

    def create_widgets(self):
        self.label = tk.Label(text="Value Converter")
        self.numberEntry = tk.Entry()
        self.convertButton = tk.Button(text="Convert",
                                       command=self.convert)
        self.output = tk.Label()
        # Place widgets
        self.label.pack(side="left")
        self.numberEntry.pack(side="left")
        self.convertButton.pack(side="left")
        self.output.pack(side="left")

    def convert(self):
        entry = self.numberEntry.get()
        try:
            value = float(entry)
            result = round(value / 1.95583, 2)
            self.output.config(text=str(value) + ' BGN = ' + str(result) + ' EUR', bg="green", fg="white")
        except ValueError:
            self.output.config(text="Please input a number!",
                               bg="red", fg="black")


app = Application()
app.master.title("BGN to EUR Converter")

app.mainloop()
