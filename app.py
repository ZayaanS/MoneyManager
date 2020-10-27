import pymongo
from tkinter import *


__author__ = "Zayaan"
mongodb_uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(mongodb_uri)
database = client['MoneyManager']
collection = database['Users']


# set global variables
global username
global password
global username_entry
global email_entry
global password_entry
global main_screen
global email_verify
global password_verify
global email
global login_button
global registration_success
global Registration_fail
global no_user
global register_button
global wrong_password


# create a GUI window 
main_screen = Tk()


# Function to clear the window
def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    return _list


# Main account screen function
def main_account_screen():
    # set the configuration of GUI window 
    main_screen.geometry("400x450")  
    # set the title of GUI window
    main_screen.title("Account Login")
    # create a Form label 
    Label(text="Money Manager", width="300", height="2", font=("Montserrat", 32)).pack() 
    # create Login Button 
    Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = login).pack() 
    # create a register button
    Button(text="Register", height="2", width="30", font=("Montserrat", 10), command=register).pack()
    # start the GUI
    main_screen.mainloop()


# define login function
def login():
    # clear window
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()
    # create login screen
    main_screen.title("Login")
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Email * ").pack()
    email_login_entry = Entry(main_screen, textvariable=email_verify)
    email_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password * ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=login_verification).pack()


def register():
    # clear window
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()
    # set the title of GUI window
    main_screen.title("Account Register")
    # Set label for user's instruction
    Label(main_screen, text="Please enter details below").pack()
    Label(main_screen, text="").pack()   
    # Set email label
    email_lable = Label(main_screen, text="Email * ")
    email_lable.pack()
    # Set email entry
    email_entry.pack()
    # Set username label
    username_lable = Label(main_screen, text="Username * ")
    username_lable.pack()
    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    username_entry.pack() 
    # Set password label
    password_lable = Label(main_screen, text="Password * ")
    password_lable.pack()   
    # Set password entry
    password_entry.pack()   
    Label(main_screen, text="").pack()   
    # Set register button
    Button(main_screen, text="Register", width=10, height=1, command = register_user).pack()


# Set text variables
username = StringVar()
password = StringVar()
email = StringVar()
email_verify = StringVar()
password_verify = StringVar()
password_entry = Entry(main_screen, textvariable=password, show='*')
email_entry = Entry(main_screen, textvariable=email)
username_entry = Entry(main_screen, textvariable=username)
login_button = Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = login)
registration_success = Label(main_screen, text="Registration Success", fg="green", font=("Montserrat", 10))
Registration_fail = Label(main_screen, text="There is already an existing account linked to this email address", fg="red", font=("Montserrat", 10))
no_user = Label(main_screen, text="No user with this email exists", fg="red", font=("Montserrat", 10))
register_button = Button(text="Register", height="2", width="30", font=("Montserrat", 10), command = register)
wrong_password = Label(main_screen, text="Incorrect password", fg="red", font=("Montserrat", 10))


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
def register_user():
    # clear any existing registration info
    registration_success.pack_forget()
    Registration_fail.pack_forget()
    login_button.pack_forget()
    # get username and password
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
        # set a label for showing success information on screen     
        registration_success.pack()
    else:
        print(result)
        # set a label for information on screen     
        Registration_fail.pack()
    clear_register_fields()
    # create Login Button 
    login_button.pack()
    for user in users:
        print(user)


# define log in verfication function
def login_verification():
    # clear any existing extras
    no_user.pack_forget()
    register_button.pack_forget()
    wrong_password.pack_forget()
    # get entries from login screen
    login_email = str(email_verify.get())
    login_password = str(password_verify.get())
    # search database to find if email exists
    user = database["Users"].find_one({"Email" : login_email})
    # if user does not exist add message
    if user is None:
        no_user.pack()
        register_button.pack()
        return
    elif login_password == user["Password"]:
        print("Successfully logged in!")
        return
    else:
        wrong_password.pack()
    # get list of current users
    users = collection.find({})
    for user in users:
        print(user)

collection.delete_many({})
# call the main_account_screen function
main_account_screen()


