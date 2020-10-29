from tkinter import *
from gen import clear_window
from home import create_home_screen

current_user = ""

# function to create start screen
def create_start_screen(user, database, collection, screen):
    # set the configuration of GUI window 
    screen.geometry("800x700")  
    # set the title of GUI window
    screen.title("Account Login")
    # create a Form label 
    Label(text="Money Manager", width="300", height="2", font=("Montserrat", 32)).pack() 
    # create Login Button 
    Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = lambda: create_login_screen(user, database, collection, screen)).pack() 
    # create a register button
    Button(text="Register", height="2", width="30", font=("Montserrat", 10), command = lambda: create_register_screen(user, database, collection, screen)).pack()
    # start the GUI
    screen.mainloop()

# function to create login screen
def create_login_screen(user, database, collection, screen):
    # variables
    global email_verify
    global password_verify
    email_verify = StringVar()
    password_verify = StringVar()
    # clear window
    clear_window(screen)
    # create login screen
    screen.title("Login")
    Label(screen, text="Please enter details below to login").pack()
    Label(screen, text="").pack()
    Label(screen, text="Email * ").pack()
    email_login_entry = Entry(screen, textvariable = email_verify)
    email_login_entry.pack()
    Label(screen, text="").pack()
    Label(screen, text="Password * ").pack()
    password__login_entry = Entry(screen, textvariable = password_verify, show= '*')
    password__login_entry.pack()
    Label(screen, text="").pack()
    Button(screen, text="Login", width=10, height=1, command = lambda: login_verification(user, database, collection, screen)).pack()

# create register screen
def create_register_screen(user, database, collection, screen):
    # variables
    global username
    global password
    global email
    username = StringVar()
    password = StringVar()
    email = StringVar()
    # clear window
    clear_window(screen)
    # set the title of GUI window
    screen.title("Account Register")
    # Set label for user's instruction
    Label(screen, text="Please enter details below").pack()
    Label(screen, text="").pack()   
    # Set email label
    email_lable = Label(screen, text="Email * ")
    email_lable.pack()
    # Set email entry
    global email_entry
    email_entry = Entry(screen, textvariable = email)
    email_entry.pack()
    # Set username label
    username_lable = Label(screen, text="Username * ")
    username_lable.pack()
    # Set username entry
    global username_entry
    username_entry = Entry(screen, textvariable = username)
    username_entry.pack() 
    # Set password label
    password_lable = Label(screen, text="Password * ")
    password_lable.pack()   
    # Set password entry
    global password_entry
    password_entry = Entry(screen, textvariable = password, show='*')
    password_entry.pack()   
    Label(screen, text="").pack()   
    # Set register button
    Button(screen, text="Register", width=10, height=1, command = lambda: register_user(user, database, collection, screen)).pack()

# function to clear fields after registering a new user
def clear_register_fields():
    email_entry.delete("0","end")
    password_entry.delete("0","end")
    username_entry.delete("0","end")
    username_info = ""
    password_info = ""
    email_info = ""
    result = ""

# function to register user to database
def register_user(user, database, collection, screen):
    #variables 
    global login_button
    global registration_success
    global registration_fail
    login_button = Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = lambda: create_login_screen(user, database, collection, screen))
    registration_success = Label(screen, text="Registration Success", fg="green", font=("Montserrat", 10))
    registration_fail = Label(screen, text="There is already an existing account linked to this email address", fg="red", font=("Montserrat", 10))
    # clear any existing registration info
    registration_success.pack_forget()
    registration_fail.pack_forget()
    login_button.pack_forget()
    # get username and password
    global username_info
    global password_info
    global email_info
    global result
    username_info = str(username.get())
    password_info = str(password.get())
    email_info = str(email.get())
    # get list of current users
    users = collection.find({})
    # search database to check if user with same email exists
    result = database["Users"].find_one({"Email" : email_info})
    # if result is none
    if result is None :
        # add user details to database
        collection.insert_one({"Name" : username_info, "Email" : email_info, "Password" : password_info})
        # create collections for new user
        new_user_dbs(database, email_info)
        # return a list of all collections in database
        print(database.list_collection_names())
        # set a label for showing success information on screen     
        registration_success.pack()
    else:
        print(result)
        # set a label for information on screen     
        registration_fail.pack()
    # clear register fields
    clear_register_fields()
    # create Login Button 
    login_button.pack()
    for user in users:
        print(user)

# function create collections for new user in database
def new_user_dbs(database, email):
    # create user's income collection
    income_table = str(email + "_Income")
    income_coll = database[income_table]
    income_coll.insert_one({"Email" : email, "Title" : "", "Category" : "", "Amount": 0 })
    # create user's budget collection
    budget_table = str(email + "_Budget")
    budget_coll = database[budget_table]
    budget_coll.insert_one({"Email" : email, "Title" : "", "Category" : "", "Amount": 0 })
    # create user's expenses collection
    expenses_table = str(email + "_Expenses")
    expenses_coll = database[expenses_table]
    expenses_coll.insert_one({"Email" : email, "Title" : "", "Category" : "", "Amount": 0 })
    # create user's savings collection
    savings_table = str(email + "_Savings")
    savings_coll = database[savings_table]
    savings_coll.insert_one({"Email" : email, "Title" : "", "Category" : "", "Amount": 0 })
    # create user's balances collection
    balances_table = str(email + "_Balances")
    balances_coll = database[balances_table]
    balances_coll.insert_one({"Email" : email, "Category" : "", "Amount": 0 })

# function to log user in
def login_verification(user, database, collection, screen):
    #variables
    no_user = Label(screen, text="No user with this email exists", fg="red", font=("Montserrat", 10))
    register_button = Button(text="Register", height="2", width="30", font=("Montserrat", 10), command = lambda: create_register_screen(user, database, collection, screen))
    wrong_password = Label(screen, text="Incorrect password", fg="red", font=("Montserrat", 10))
    # clear any existing extras
    no_user.pack_forget()
    register_button.pack_forget()
    wrong_password.pack_forget()
    # get entries from login screen
    login_email = str(email_verify.get())
    login_password = str(password_verify.get())
    global current_user
    current_user = login_email
    # search database to find if email exists
    user = database["Users"].find_one({"Email" : login_email})
    # if user does not exist add message
    if user is None:
        no_user.pack()
        register_button.pack()
        return
    elif login_password == user["Password"]:
        print("Successfully logged in!")
        create_home_screen(user, database, screen)
        print("Current user is : ", current_user)
        return
    else:
        wrong_password.pack()
    # get list of current users
    users = collection.find({})
    for user in users:
        print(user)
