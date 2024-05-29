##########################################################################################
#   Author:        Adam Osborne
#   Organization:  SOHTCTFDFL
#   Contact Info:  adam.osborne@hightechcrimestaskforce.com
#                  541-613-4031
#   Purpose:       This script takes asks the user for a network filepath 
#                  and creates a command line command to be placed in the command
#                  window to execute robocopy 
#                  This is for moving the entire case file from the working server (221)
#                  to the archive server (222)
#
#                  -V1.0
#                  Simply the code written which the user can access using VS Code
#                  Pending Dev
#                       - Make GUI for easy use
#                       - Add functionality to interact directly with the command line
#                         so the script will aumatically execute the script when the user
#                         gives it an proper input
#                       - make .exe which is portable
##########################################################################################

#DEV# Make GUI
import tkinter as tk
from PIL import ImageTk

#initialize app
root = tk.Tk()
root.title('Robocopy Commad Creater')
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg='#3d6466')
frame1.grid(row=0, column=0)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file='starter_files/assets/sohtctflogo.png')
logo_widget = tk.Label(frame1,image=logo_img)
logo_widget.image = logo_img
logo_widget.pack()

#run app
root.mainloop()

OriginalFilePath = input(r'What is the Original filepath?') 

# Defined variables that are not expected to change
Server222 = r'\\10.10.50.222\3\HTCU Master Case Files'

#Debug#'\\10.10.50.221\s$\HTCU MASTER CASE FILES\2024 CASES\HTCU CR#24-017 - ET - OSP - ALLIANCE OP - KELLY'

# Creates a list of the items delimited using the backslash charecter in the OriginalFilePath string
CaseString = OriginalFilePath.split('\\')
#Debug#[print(x) for x in CaseYear]

# Loops through the list snd pulls out year of the case (CaseYear) also pulls out the last list item 
# which is the final file path location. 
i = 0 
while i < len(CaseString):
    if 'CASES' in CaseString[i]:
        CaseYear = CaseString[5]
        #Debug#print(CaseYear)
    else:
        if '-' in CaseString[i]:
            CasePath = CaseString[-1]
            #Debug#print(CasePath)
    i = i + 1

# Produces the RoboCoy string to be used in the command line
RoboCopyString = 'robocopy ' + '"' + OriginalFilePath + '" ' + '"' + Server222 + "\\" + CaseYear + "\\" + CasePath + '"' + " \\E \\copyall"
print(RoboCopyString)









