import tkinter as tk

#to create a window 
root = tk.Tk()
#to set the screen resolution
root.geometry("500x500")
#to set the title
root.title("Hello world")

#this is for plain text
label = tk.Label(root,text="helloworld!", font=('Arial', 18))
label.pack(padx=20,pady=20)

#text box to enter data from the user
textbox = tk.Text(root, font=('Arial', 24), height=2)
textbox.pack()

#entries from the user
myEntry = tk.Entry(root, width=24, font=('Arial', 24))
myEntry.pack()

#This is button
button = tk.Button(root, text='click me')
button.pack()



#fun fact: you do not have to put a program stopper to work
root.mainloop()