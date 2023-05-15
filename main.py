#=========Import Modules=========================================---.
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
import customtkinter
from customtkinter import *
import sys
#============================Theme================================
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
#=================================================================
def open_file():
    #Open a file for editing.
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete('1.0', END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(customtkinter.END, text)
    window.title(f"Example notebook - {filepath}")
#=================================================================---.
def save_file(event):
    #Save a file.
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Example notebook - {filepath}")
#=================================================================|
def s_file():#							  |
	save_file("e")#						  |
#=================================================================|
def onKeyPress(event):#						  |
    print("ctrl+a")#						  |
#=================================================================|
window = customtkinter.CTk()#					  |
#=====================Window======================================|
window.title("Example notebook ")#                                       |
window.rowconfigure(0, minsize=800, weight=1)#                    |
window.columnconfigure(1, minsize=800, weight=1)#                 |
#=======================Elements==================================|


txt_edit = tk.Text(window)#                                     =============================|
fr_buttons = customtkinter.CTkFrame(window, relief=tk.RAISED, bd=2)#                            |
btn_open = customtkinter.CTkButton(fr_buttons, text="Open", command=open_file) # Open Button    |
thisMenuBar = Menu(window)

btn_save = customtkinter.CTkButton(fr_buttons, text="Save As...", command=s_file) # Save Button |
#===============================================================================================|
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5) #     |
btn_save.grid(row=1, column=0, sticky="ew", padx=5) #             |
#=================================================================|
fr_buttons.grid(row=0, column=0, sticky="ns")#                    |
txt_edit.grid(row=0, column=1, sticky="nsew")#                    |
window.bind('<Control-a>', onKeyPress)#                           |
window.bind('<Control-s>', save_file)#                            |
scrollb = tk.Scrollbar(window, command=txt_edit.yview)#           |
#scrollb.grid(row=0, column=0)#, sticky='nsew')                   |
#============View Window==========================================|
window.mainloop()#                                                |
#=================================================================|
