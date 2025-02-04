import tkinter as tk
from tkinter import Menu

def callback():
    print("Menu item clicked")

# Create the main window
root = tk.Tk()
root.title("Underscore Menu Example")

# Create a menu bar
menu_bar = Menu(root)

# Create a "File" menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=callback, underline=0)  # underline=0 means the first character is underscored
file_menu.add_command(label="Save", command=callback, underline=0)
file_menu.add_command(label="Exit", command=root.quit, underline=1)  # underline=1 means the second character is underscored

# Add the "File" menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu, underline=0)

# Attach the menu bar to the window
root.config(menu=menu_bar)
