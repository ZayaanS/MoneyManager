from tkinter import *

# function to define all items in the window
def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
           _list.extend(item.winfo_children())
    return _list

# function to clear all items in window
def clear_window(screen):
    widget_list = all_children(screen)
    for item in widget_list:
        item.pack_forget()
