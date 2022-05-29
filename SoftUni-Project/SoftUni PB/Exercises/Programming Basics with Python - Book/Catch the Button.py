import tkinter as tk
import random


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

        # Create widgets

    def create_widgets(self):

        self.button = tk.Button(text="Catch me!",
                                command=self.on_click())
        self.label = tk.Label()

        # Place widgets

        self.button.pack(side="top")
        self.label.pack(side="top")

        # bind functions

        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    def on_enter(self):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        self.button.pack(side="right", padx=x, pady=y)

    def on_leave(self):
        self.label.config(text="")

    def on_click(self):
        self.label.config(text="You win!")

# Create the application


app = Application()

app.master.title("Catch the Button")
app.master.minsize(width=400, height=200)

# start the program
app.mainloop()
