import tkinter as tk
from tkinter import ttk

# Window Consts
window_title = 'OZ RoboCopy String Creator'
window_geomety = '500x150'

# Window Setup
window = tk.Tk()
window.title(window_title)
window.geometry(window_geomety)
window.iconbitmap('')
window.resizable(False,False)

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

# Widgets
entry_string = tk.StringVar(value='Original Filepath here')
input_string = ttk.Entry(window, textvariable=entry_string) 
#input_string.place(relx=0.2, rely=0.2, anchor='center')

btn_make_string = ttk.Button(window, text='Make String', command=lambda:print('button pressed'))
#btn_make_string.pack(side='bottom', anchor="e", padx=8, pady=8)

# Define the Grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# Place Widgets in Grid
input_string.grid(row=0, column = 0, sticky='nsew')
btn_make_string.grid(row=2,column=1, sticky='se', padx=8, pady=8)

# Run
window.mainloop()