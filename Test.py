import tkinter as tk
from tkinter import ttk
import RoboCopyCreater

def submit_callback(input_entry):
    #OriginalFilePath = input_entry.get()
    #print(input_entry.get())
    
    return None
  
# Creating tkinter window
window = tk.Tk()
window.title('Robocopy Command Generator')

input_label = tk.Label(
    window, 
    text = "Original filepath:",
    font = ("Times New Roman", 
            10)).grid(
                column = 0,
                row = 1, 
                padx = 10, 
                pady = 25)

input_entry = tk.Entry(
    window, 
    width=50,
    text = "Enter some text",
    font = ("Times New Roman", 10))

input_entry.grid(
    column = 1,
    row = 1, 
    padx = 10, 
    pady = 25)

submit_button = tk.Button(
    window, 
    text = "Submit",
    command = lambda: submit_callback(input_entry))

submit_button.grid(column=1, row=2)

window.mainloop()


