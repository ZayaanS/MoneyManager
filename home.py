from tkinter import *
from gen import clear_window
from income import create_income_screen

# function to create navigation buttons
def create_navigation(screen):
    global home_button
    global budget_button
    global income_button
    global expenses_button
    global savings_button
    home_button = Button(screen, text="home", height="2", width="15", font=("Montserrat", 10), command = lambda : create_home_screen(screen))
    budget_button = Button(screen, text="budget", height="2", width="15", font=("Montserrat", 10))
    income_button = Button(screen, text="income", height="2", width="15", font=("Montserrat", 10), command = lambda : show_income_screen(screen))
    expenses_button = Button(screen, text="expenses", height="2", width="15", font=("Montserrat", 10))
    savings_button = Button(screen, text="savings", height="2", width="15", font=("Montserrat", 10))
    home_button.grid(row=1, column=0)
    budget_button.grid(row=1, column=1)
    income_button.grid(row=1, column=2)
    expenses_button.grid(row=1, column=3)
    savings_button.grid(row=1, column=4)

# function to create home screen
def create_home_screen(screen):
    clear_window(screen)
    create_navigation(screen)

# function to show income screen
def show_income_screen(screen):
    clear_window(screen)
    create_navigation(screen)
    create_income_screen(screen)


