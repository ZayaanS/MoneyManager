from tkinter import *
from gen import clear_window
from income import create_income_screen, get_total_income, show_income_table
from expenses import create_expenses_screen, get_total_expenses, show_expense_table
from budget import create_budget_screen
from savings import create_savings_screen, get_total_savings, show_savings_table

# function to create navigation buttons
def create_navigation(user, database, screen):
    global home_button
    global budget_button
    global income_button
    global expenses_button
    global savings_button
    home_button = Button(screen, text="home", height="2", width="15", font=("Montserrat", 10), command = lambda : create_home_screen(user, database, screen))
    budget_button = Button(screen, text="budget", height="2", width="15", font=("Montserrat", 10), command = lambda : show_budget_screen(user, database, screen))
    income_button = Button(screen, text="income", height="2", width="15", font=("Montserrat", 10), command = lambda : show_income_screen(user, database, screen))
    expenses_button = Button(screen, text="expenses", height="2", width="15", font=("Montserrat", 10), command = lambda : show_expenses_screen(user, database, screen))
    savings_button = Button(screen, text="savings", height="2", width="15", font=("Montserrat", 10), command = lambda : show_savings_screen(user, database, screen))
    home_button.grid(row=1, column=0)
    budget_button.grid(row=1, column=2)
    income_button.grid(row=1, column=1)
    expenses_button.grid(row=1, column=3)
    savings_button.grid(row=1, column=4)

# function to create home screen
def create_home_screen(user, database, screen):
    show_income_screen(user, database, screen)
    show_expenses_screen(user, database, screen)
    show_savings_screen(user, database, screen)
    clear_window(screen)
    create_navigation(user, database, screen)
    Label(text="Money Manager", font=("Montserrat", 32)).grid(row=2, columnspan=4) 
    Label(text="Your Balance", font=("Montserrat", 24)).grid(row=3, columnspan=4) 
    balance = float(get_total_income()) - float(get_total_expenses())
    Label(text=balance, font=("Montserrat", 24)).grid(row=4, columnspan=4) 
    Label(text="Total Income", font=("Montserrat", 14)).grid(row=5, columnspan=4) 
    Label(text=get_total_income(), font=("Montserrat", 14)).grid(row=6, columnspan=4) 
    Label(text="Total Expenses", font=("Montserrat", 14)).grid(row=7, columnspan=4) 
    Label(text=get_total_expenses(), font=("Montserrat", 14)).grid(row=8, columnspan=4) 
    Label(text="Savings", font=("Montserrat", 22)).grid(row=9, columnspan=4) 
    Label(text=get_total_savings(), font=("Montserrat", 22)).grid(row=10, columnspan=4) 


# function to show income screen
def show_income_screen(user, database, screen):
    clear_window(screen)
    create_navigation(user, database, screen)
    create_income_screen(user, database, screen)

# function to show expenses screen
def show_expenses_screen(user, database, screen):
    clear_window(screen)
    create_navigation(user, database, screen)
    create_expenses_screen(user, database, screen)

# function to show budget screen
def show_budget_screen(user, database, screen):
    clear_window(screen)
    create_navigation(user, database, screen)
    create_budget_screen(user, database, screen)

# function to show savings screen
def show_savings_screen(user, database, screen):
    clear_window(screen)
    create_navigation(user, database, screen)
    create_savings_screen(user, database, screen)


