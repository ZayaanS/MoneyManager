import pymongo
from tkinter import *

# create global variables
global home_button
global budget_button
global income_button
global expenses_button
global savings_button
global main_screen

main_screen = Tk()
home_button = Button(main_screen, text="home", height="2", width="15", font=("Montserrat", 10))
budget_button = Button(main_screen, text="budget", height="2", width="15", font=("Montserrat", 10))
income_button = Button(main_screen, text="income", height="2", width="15", font=("Montserrat", 10))
expenses_button = Button(main_screen, text="expenses", height="2", width="15", font=("Montserrat", 10))
savings_button = Button(main_screen, text="savings", height="2", width="15", font=("Montserrat", 10))


# Function to clear the window
def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
           _list.extend(item.winfo_children())
    return _list

# create navigation buttons
def create_navigation():
    home_button.grid(row=1, column=0)
    budget_button.grid(row=1, column=1)
    income_button.grid(row=1, column=2)
    expenses_button.grid(row=1, column=3)
    savings_button.grid(row=1, column=4)

def home_screen():
    # clear window
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()
    # add navigation
    create_navigation()
