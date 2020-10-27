import pymongo
from tkinter import *

# create global variables
global home_button
global budget_button
global income_button
global expenses_button
global savings_button

home_button = Button(text="home", height="2", width="15", font=("Montserrat", 10))
budget_button = Button(text="budget", height="2", width="15", font=("Montserrat", 10))
income_button = Button(text="income", height="2", width="15", font=("Montserrat", 10))
expenses_button = Button(text="expenses", height="2", width="15", font=("Montserrat", 10))
savings_button = Button(text="savings", height="2", width="15", font=("Montserrat", 10))

# create navigation buttons
def create_navigation():
    home_button.grid(row=1, column=0)
    budget_button.grid(row=1, column=1)
    income_button.grid(row=1, column=2)
    expenses_button.grid(row=1, column=3)
    savings_button.grid(row=1, column=4)