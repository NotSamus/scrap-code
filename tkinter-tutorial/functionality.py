import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):        
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Test2")
        
        self.label = tk.Label(self.root, text="your message",
                            font=('Arial', 18))
        self.label.pack(padx=10,pady=10)
        self.textbox = tk.Text(self.root,height=5,font=('Arial', 18))
        self.textbox.pack(padx=10,pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="show messagebox", variable=self.check_state)
        self.check.pack(padx=10,pady=10)
    
        self.button = tk.Button(self.root, text='show message', command=self.show_message)
        self.button.pack(padx=10,pady=10)
        #Necessarly to make it work
        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get()==0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0',tk.END))
    
MyGUI()