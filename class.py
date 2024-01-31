import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pyodbc
from tkinter import *
from PIL import Image
import os 

class AkyeritApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Add any initialization code here
        self.colour1= '#222448'
        self.colour1= '#54527E'
        self.colour3= 'white'