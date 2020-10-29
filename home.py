import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from gen import clear_window
from income import create_income_screen, get_total_income, show_income_table
from expenses import create_expenses_screen, get_total_expenses, show_expense_table
from budget import create_budget_screen
from savings import create_savings_screen, get_total_savings, show_savings_table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function to create navigation buttons
def create_navigation(user, database, collection, screen):
    global home_button
    global budget_button
    global income_button
    global expenses_button
    global savings_button
    global sign_out_button
    home_button = Button(screen, text="home", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : create_home_screen(user, database, collection, screen))
    budget_button = Button(screen, text="budget", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : show_budget_screen(user, database, collection, screen))
    income_button = Button(screen, text="income", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : show_income_screen(user, database, collection, screen))
    expenses_button = Button(screen, text="expenses", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : show_expenses_screen(user, database, collection, screen))
    savings_button = Button(screen, text="savings", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : show_savings_screen(user, database, collection, screen))
    sign_out_button = Button(screen, text="sign out", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : exit(screen))
    home_button.grid(row=1, column=0)
    budget_button.grid(row=1, column=2)
    income_button.grid(row=1, column=1)
    expenses_button.grid(row=1, column=3)
    savings_button.grid(row=1, column=4)
    sign_out_button.grid(row=1, column=5)

# function to create donut chart showing income vs expenses
def create_donut_graph(spent, remaining, screen):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    # labels
    labels = ["spent", "remaining"]
    # amounts to go into graph
    data = [spent, remaining]
    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=90,counterclock=False)
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
    #add donut sections
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
    # set title
    ax.set_title("Balance Available")
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = screen)   
    canvas.draw() 
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row=12, columnspan=5) 

# function to create home screen
def create_home_screen(user, database, collection, screen):
    clear_window(screen)
    create_navigation(user, database, collection, screen)
    Label(text="Money Manager", font=("Montserrat", 32), bg ="white").grid(row=2, columnspan=4) 
    Label(text="Your Balance", font=("Montserrat", 24), bg ="white").grid(row=3, columnspan=4) 
    income = float(get_total_income(user, database))
    expenses = float(get_total_expenses(user, database))
    balance = income - expenses 
    Label(text=balance, font=("Montserrat", 24), bg ="white").grid(row=4, columnspan=4) 
    Label(text="Total Income", font=("Montserrat", 14), bg ="white").grid(row=5, columnspan=4) 
    Label(text=get_total_income(user, database), font=("Montserrat", 14), bg ="white").grid(row=6, columnspan=4) 
    Label(text="Total Expenses", font=("Montserrat", 14), bg ="white").grid(row=7, columnspan=4) 
    Label(text=get_total_expenses(user, database), font=("Montserrat", 14), bg ="white").grid(row=8, columnspan=4) 
    Label(text="Savings", font=("Montserrat", 22), bg ="white").grid(row=9, columnspan=4) 
    Label(text=get_total_savings(user, database), font=("Montserrat", 22), bg ="white").grid(row=10, columnspan=4) 
    create_donut_graph(expenses, balance, screen)


# function to show income screen
def show_income_screen(user, database, collection, screen):
    clear_window(screen)
    create_navigation(user, database, collection, screen)
    create_income_screen(user, database, screen)

# function to show expenses screen
def show_expenses_screen(user, database, collection, screen):
    clear_window(screen)
    create_navigation(user, database, collection, screen)
    create_expenses_screen(user, database, screen)

# function to show budget screen
def show_budget_screen(user, database, collection, screen):
    clear_window(screen)
    create_navigation(user, database, collection, screen)
    create_budget_screen(user, database, screen)

# function to show savings screen
def show_savings_screen(user, database, collection, screen):
    clear_window(screen)
    create_navigation(user, database, collection, screen)
    create_savings_screen(user, database, screen)

def exit(screen):
    screen.quit()


