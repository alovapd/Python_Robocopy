import tkinter as tk
from PIL import ImageTk

# Changeable constatnts unique to this app
bg_color = 'black' #set to the desired background color (logo's natural background is black)
main_label_text = 'Paste the Original filepath in the box below' #set to what you want the label to say
btn_text = 'Get Robocopy cmd' # Set to change the buttons text

def load_frame1():
    frame1.pack_propagate(False)
    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file='starter_files/assets/sohtctflogo.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20, side=tk.LEFT)

    # Creates the label above the input field
    tk.Label(frame1, text=main_label_text, bg=bg_color, fg="white", font=('TKMenuFont', 10)).pack(pady=10)
    
    # TextBox Creation 
    inputtxt = tk.Text(frame1, height = 1, width = 60).pack(pady=10) 

    # Button Creation
    #{DEV} Need to solve this lambda function throws error
    tk.Button(frame1, text=btn_text, font=('TKHeadingFont', 10), 
    bg='#28393a', fg='white', cursor='hand2', activebackground='#badee2', activeforeground='black', command=lambda:load_frame1(inputtxt)
    ).pack(pady=5, side=tk.BOTTOM)

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
    
    #def GetUserTxt():
        #print(inputtxt.get())

#initialize app
window = tk.Tk()
window.title('Robocopy Commad Creater')
window.eval("tk::PlaceWindow . center")
window.resizable(False,False)

#create frame widget
frame1 = tk.Frame(window, width=750, height=150, bg=bg_color)
frame2 = tk.Frame(window, bg=bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

#run app
window.mainloop()