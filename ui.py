#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from uilayout import *


class Main(CreatureWindow):
    def __init__(self, master=None):
        super().__init__(master)
        # self.style = ttk.Style()
        # self.style.theme_use("winnative")


if __name__ == "__main__":
    app = Main()
    app.run()
