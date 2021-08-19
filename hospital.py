from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.geometry("1540x800+0+0")

        lbltitle = Label(self.root, 50, bd=20, relief=RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font="times new roman", style="bold")
        lbltitle.pack(side=TOP, fill=x)



root = Tk()
ob = Hospital(root)
root.mainloop()