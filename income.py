from tkinter import *

# function to create income screen
def create_income_screen(user, database, screen):
    # variables
    global new_title
    global new_category
    global new_amount
    global collection_name
    global incomes
    collection_name = user["Email"] + "_Income"
    incomes = database[collection_name].find({})
    new_title = StringVar()
    new_category = StringVar()
    new_amount = DoubleVar()
    # create heading label
    Label(text="Your Incomes", font=("Montserrat", 16)).grid(row=2, columnspan=4) 
    # create input field for new income
    Label(text="Add new income", font=("Montserrat", 14)).grid(row=3, columnspan=4) 
    Label(text="Title", font=("Montserrat", 12)).grid(row=4, column=1)
    Label(text="Category", font=("Montserrat", 12)).grid(row=4, column=2)
    Label(text="Amount", font=("Montserrat", 12)).grid(row=4, column=3) 
    new_title_entry = Entry(screen, textvariable = new_title)
    new_title_entry.grid(row=5, column=1)
    new_category_entry = Entry(screen, textvariable = new_category)
    new_category_entry.grid(row=5, column=2)
    new_amount_entry = Entry(screen, textvariable = new_amount)
    new_amount_entry.grid(row=5, column=3)
    add_income_button = Button(screen, text="Add", height="2", width="15", font=("Montserrat", 10), command = lambda : add_new_income(user, database, screen))
    add_income_button.grid(row=5, column=4)
    # table to display current income values
    Label(text="Existing incomes", font=("Montserrat", 14)).grid(row=6, columnspan=4) 

# function to add new income to database
def add_new_income(user, database, screen):
    # get entry details
    new_title_info = new_title.get()
    new_category_info = new_category.get()
    new_amount_info = new_amount.get() 
    database[collection_name].insert_one({"Email" : user["Email"], "Title" : new_title_info, "Category" : new_category_info, "Amount" : new_amount_info})
    show_income_table()

# function to display table 
def show_income_table():
    n = 0
    for income in incomes:
        n = n + 1
        Label(text = income["Title"] , font=("Montserrat", 10)).pack()
        Label(text = income["Category"] , font=("Montserrat", 10)).pack()
        Label(text = income["Amount"] , font=("Montserrat", 10)).pack()


