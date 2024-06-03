import tkinter as tk
from tkinter import ttk

def submit_callback(input_entry):
    print("User entered : " + input_entry.get())
    return None
  
# Creating tkinter window
window = tk.Tk()
window.title('GENERATOR')
window.geometry('500x550')

input_label = tk.Label(window, text="Enter file name" ,font = ("Times New Roman", 10)).grid(column = 0,row = 1, padx = 10, pady = 25)
#input_label.place(column = 1, row = 30)

input_entry = tk.Entry(window, text="Enter some text" ,font = ("Times New Roman", 10))
input_entry.grid(column = 1,row = 1, padx = 10, pady = 25)

submit_button = tk.Button(window, text = "Submit" , command = lambda: submit_callback(input_entry))

submit_button.grid(column=1, row=2)


window.mainloop()