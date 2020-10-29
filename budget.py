from tkinter import *

global total_budget

# function to create budget screen
def create_budget_screen(user, database, screen):
    # variables
    global new_title
    global new_category
    global new_amount
    global collection_name
    global budget
    collection_name = user["Email"] + "_Budget"
    budget = database[collection_name].find({})
    new_title = StringVar()
    new_category = StringVar()
    new_amount = DoubleVar()
    # create heading label
    Label(text="Your Budget", font=("Montserrat", 16), bg ="white").grid(row=2, columnspan=4) 
    # create input field for new budget item
    Label(text="Add new planned expense", font=("Montserrat", 14), bg ="white").grid(row=5, columnspan=4) 
    Label(text="Title", font=("Montserrat", 12), bg ="white").grid(row=6, column=1)
    Label(text="Category", font=("Montserrat", 12), bg ="white").grid(row=6, column=2)
    Label(text="Amount", font=("Montserrat", 12), bg ="white").grid(row=6, column=3) 
    new_title_entry = Entry(screen, textvariable = new_title)
    new_title_entry.grid(row=7, column=1)
    new_category_entry = Entry(screen, textvariable = new_category)
    new_category_entry.grid(row=7, column=2)
    new_amount_entry = Entry(screen, textvariable = new_amount)
    new_amount_entry.grid(row=7, column=3)
    add_budget_button = Button(screen, text="Add", height="2", width="15", font=("Montserrat", 10), bg ="white", command = lambda : add_new_budget(user, database, screen))
    add_budget_button.grid(row=7, column=4)
    # table to display current budget values
    Label(text="Existing planned expenses", font=("Montserrat", 14), bg ="white").grid(row=8, columnspan=4) 
    show_budget_table(screen)

# function to add new budget to database
def add_new_budget(user, database, screen):
    # get entry details
    new_title_info = new_title.get()
    new_category_info = new_category.get()
    new_amount_info = new_amount.get() 
    database[collection_name].insert_one({"Email" : user["Email"], "Title" : new_title_info, "Category" : new_category_info, "Amount" : new_amount_info})
    show_budget_table(screen)

# function to display table 
def show_budget_table(screen):
    print("displaying budget")
    total_budget = 0
    n = 0
    for b in budget:
        n = int(n + 1)
        Label(text = b["Title"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=1) 
        Label(text = b["Category"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=2) 
        Label(text = b["Amount"] , font=("Montserrat", 10), bg ="white").grid(row=int(10+n), column=3) 
        total_budget = float(total_budget) + float(b["Amount"])
    # display total budget
    Label(text="Total Planned Expenses", font=("Montserrat", 14), bg ="white").grid(row=3, columnspan=4) 
    Label(text=total_budget, font=("Montserrat", 14), bg ="white").grid(row=4, columnspan=4) 


