from tkinter import *

global total_savings
total_savings = 0

# function to create savings screen
def create_savings_screen(user, database, screen):
    # variables
    global new_title
    global new_category
    global new_amount
    global collection_name
    global savings
    collection_name = user["Email"] + "_Savings"
    savings = database[collection_name].find({})
    new_title = StringVar()
    new_category = StringVar()
    new_amount = DoubleVar()
    # create heading label
    Label(text="Your Savings", font=("Montserrat", 16)).grid(row=2, columnspan=4) 
    # create input field for new savings item
    Label(text="Add new savings item", font=("Montserrat", 14)).grid(row=5, columnspan=4) 
    Label(text="Title", font=("Montserrat", 12)).grid(row=6, column=1)
    Label(text="Category", font=("Montserrat", 12)).grid(row=6, column=2)
    Label(text="Amount", font=("Montserrat", 12)).grid(row=6, column=3) 
    new_title_entry = Entry(screen, textvariable = new_title)
    new_title_entry.grid(row=7, column=1)
    new_category_entry = Entry(screen, textvariable = new_category)
    new_category_entry.grid(row=7, column=2)
    new_amount_entry = Entry(screen, textvariable = new_amount)
    new_amount_entry.grid(row=7, column=3)
    add_savings_button = Button(screen, text="Add", height="2", width="15", font=("Montserrat", 10), command = lambda : add_new_savings(user, database, screen))
    add_savings_button.grid(row=7, column=4)
    # table to display current savings values
    Label(text="Existing savings", font=("Montserrat", 14)).grid(row=8, columnspan=4) 
    show_savings_table(screen)

# function to add new savings to database
def add_new_savings(user, database, screen):
    # get entry details
    new_title_info = new_title.get()
    new_category_info = new_category.get()
    new_amount_info = new_amount.get() 
    database[collection_name].insert_one({"Email" : user["Email"], "Title" : new_title_info, "Category" : new_category_info, "Amount" : new_amount_info})
    show_savings_table(screen)

# function to display table 
def show_savings_table(screen):
    print("displaying savings")
    total_savings = 0
    n = 0
    for b in savings:
        n = int(n + 1)
        Label(text = b["Title"] , font=("Montserrat", 10)).grid(row=int(10+n), column=1) 
        Label(text = b["Category"] , font=("Montserrat", 10)).grid(row=int(10+n), column=2) 
        Label(text = b["Amount"] , font=("Montserrat", 10)).grid(row=int(10+n), column=3) 
        total_savings = float(total_savings) + float(b["Amount"])
    # display total savings
    Label(text="Total Savings", font=("Montserrat", 14)).grid(row=3, columnspan=4) 
    Label(text=total_savings, font=("Montserrat", 14)).grid(row=4, columnspan=4) 
    get_total_savings()

# function to get total savings
def get_total_savings():
    print(total_savings)
    return total_savings
