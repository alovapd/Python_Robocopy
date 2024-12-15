import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

#{DEV} Trying to pass the text in the input field to be transfered to the RoboCopyCreater.py script when the button is pressed

# Changeable constatnts unique to this app
bg_color = 'black' #set to the desired background color (logo's natural background is black)
main_label_text = 'Paste the original filepath in the box below' #set to what you want the label to say
btn_text = 'Get Robocopy cmd' # Set to change the buttons text
window_size = '700x300' #set to change the size of the window

# Functions
def button_func(entry_string):
    print(entry_string.get())

# Initialize Window (App)
window = tk.Tk()
window.title('Robocopy Commad Creater')
window.eval("tk::PlaceWindow . center")
window.resizable(False,False)
window.configure(bg=bg_color)
window.geometry(window_size)

# Widgets
logo_img = ImageTk.PhotoImage(file='starter_files/assets/sohtctflogo.png')
logo_widget = tk.Label(window, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack(pady=20, side=tk.LEFT)

# Creates the label above the input field
tk.Label(window, text=main_label_text, bg=bg_color, fg='white', font=('TKMenuFont', 10)).pack(pady=10)
    
# TextBox Creation 
entry_string = tk.StringVar()
entry = ttk.Entry(window, textvariable = entry_string).pack(pady=10) 
#Debug#'\\10.10.50.221\s$\HTCU MASTER CASE FILES\2024 CASES\HTCU CR#24-017 - ET - OSP - ALLIANCE OP - KELLY'

# Button Creation
#{DEV} Need to get the string from the input field when button is pressed, store in variable, pass to next module
tk.Button(
    window, 
    text=btn_text, 
    font=('TKHeadingFont', 10), 
    bg='#28393a', 
    fg='white', 
    cursor='hand2', 
    activebackground='#badee2', 
    activeforeground='black',
    command=lambda: button_func(entry_string)
    ).pack(pady=5, side=tk.BOTTOM)

# Menu for the features across the top
menu = tk.Menu(window)
window.configure(menu = menu)

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

#run app
window.mainloop()