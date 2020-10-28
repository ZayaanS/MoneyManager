from tkinter import *

# function to create income screen
def create_income_screen(screen):
    # variables
    global new_title
    global new_category
    global new_amount
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
    add_income_button = Button(screen, text="Add", height="2", width="15", font=("Montserrat", 10))
    add_income_button.grid(row=5, column=4)
    # table to display current income values
    Label(text="Existing incomes", font=("Montserrat", 14)).grid(row=6, columnspan=4) 

# function to add new income to database
def add_new_income(user, database, screen):
    # get entry details
    new_title_info = new_title.get()
    new_category_info = new_category.get()
    new_amount_info = new_amount.get()
    collection_name = user + "_Income"
    database[collection_name].insert_one({"Email" : user, "Title" : new_title_info, "Category" : new_category_info, "Amount" : new_amount_info})
    incomes = database[collection_name].find({})
    for income in incomes:
        print(income)


