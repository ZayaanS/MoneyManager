from tkinter import *

global total_expenses
total_expenses = 0

# function to create expenses screen
def create_expenses_screen(user, database, screen):
    # variables
    global new_title
    global new_category
    global new_amount
    global collection_name
    global expenses
    collection_name = user["Email"] + "_Expenses"
    expenses = database[collection_name].find({})
    new_title = StringVar()
    new_category = StringVar()
    new_amount = DoubleVar()
    # create heading label
    Label(text="Your Expenses", font=("Montserrat", 16), bg ="white").grid(row=2, columnspan=4) 
    # create input field for new expenses
    Label(text="Add new expense", font=("Montserrat", 14), bg ="white").grid(row=5, columnspan=4) 
    Label(text="Title", font=("Montserrat", 12), bg ="white").grid(row=6, column=1)
    Label(text="Category", font=("Montserrat", 12), bg ="white").grid(row=6, column=2)
    Label(text="Amount", font=("Montserrat", 12), bg ="white").grid(row=6, column=3) 
    new_title_entry = Entry(screen, textvariable = new_title)
    new_title_entry.grid(row=7, column=1)
    new_category_entry = Entry(screen, textvariable = new_category)
    new_category_entry.grid(row=7, column=2)
    new_amount_entry = Entry(screen, textvariable = new_amount)
    new_amount_entry.grid(row=7, column=3)
    add_expense_button = Button(screen, text="Add", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : add_new_expense(user, database, screen))
    add_expense_button.grid(row=7, column=4)
    # table to display current expense values
    Label(text="Existing expenses", font=("Montserrat", 14), bg ="white").grid(row=8, columnspan=4) 
    show_expense_table(screen)

# function to add new expense to database
def add_new_expense(user, database, screen):
    # get entry details
    new_title_info = new_title.get()
    new_category_info = new_category.get()
    new_amount_info = new_amount.get() 
    database[collection_name].insert_one({"Email" : user["Email"], "Title" : new_title_info, "Category" : new_category_info, "Amount" : new_amount_info})
    show_expense_table(screen)

# function to display table 
def show_expense_table(screen):
    print("displaying expenses")
    total_expenses = 0
    n = 0
    for expense in expenses:
        n = int(n + 1)
        Label(text = expense["Title"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=1) 
        Label(text = expense["Category"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=2) 
        Label(text = expense["Amount"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=3) 
        total_expenses = float(total_expenses) + float (expense["Amount"])
    # display total expenses
    Label(text="Total Expenses", font=("Montserrat", 14), bg ="white").grid(row=3, columnspan=4) 
    Label(text=total_expenses, font=("Montserrat", 14), bg ="white").grid(row=4, columnspan=4) 

# function to get total expenses
def get_total_expenses(user, database):
    collection_name = user["Email"] + "_Expenses"
    expenses = database[collection_name].find({})
    total = 0
    for i in expenses:
        total = float(total) + float (i["Amount"])
    return total