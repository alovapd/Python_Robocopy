import tkinter as tk
from tkinter import ttk

# Window Consts
window_title = 'RoboCopy String Creator'
window_geomety = '500x200'

# Window Setup
window = tk.Tk()
window.title(window_title)
window.geometry(window_geomety)

# Menu for the features across the top
menu = tk.Menu(window)

# File Menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = lambda: print('New File'))
file_menu.add_command(label = 'Open', command = lambda: print('Open File'))
#file_menu.add_separator() ##This can add a seperator in the menu if desired.
menu.add_cascade(label = 'File', menu = file_menu)


#  Help Menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Get Help', command = lambda: print('Get Help'))
menu.add_cascade(label = 'Help', menu = help_menu)

window.configure(menu = menu)



# Run
window.mainloop()