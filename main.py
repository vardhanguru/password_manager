import tkinter as tk
from tkinter import messagebox
import string
import re
import random
LENGTH=16
window=tk.Tk()
window.config(padx=20,pady=20,width=1000,height=1000)
canvas = tk.Canvas(window, width=200, height=200,highlightthickness=0)
pic=tk.PhotoImage(file='logo.png')
canvas.create_image(100,100,image=pic)
canvas.grid(column=1,row=0)



def generate_password():
    pass_entry.delete(0,tk.END)
    characters = (string.ascii_letters + string.digits + string.ascii_letters+
                  string.punctuation + string.printable)
    # Create an empty password string
    password = ""

    # Loop for the desired length of the password
    for i in range(LENGTH):
        # Choose a random character from the list
        password += random.choice(characters)

    pass_entry.insert(0,password)

def add_all():
    f=open("D:\pass.txt","a")
    content=web_entry.get()+" Password: "+pass_entry.get()+" Email: "+email_entry.get()


    if len(web_entry.get())==0 or len(pass_entry.get())==0:
        messagebox.askokcancel(message="empty field")
    else:
        is_ok = messagebox.askokcancel(message=content)
        if is_ok:
            f.write(f"{content}\n")
            web_entry.delete(0,tk.END)
            pass_entry.delete(0,tk.END)

            f.close()

text1=tk.Label()
text1.config(text='Website name:')
text1.grid(column=0,row=1)

text2=tk.Label()
text2.config(text='Email/Username:')
text2.grid(column=0,row=2)

text3=tk.Label()
text3.config(text='Password:')
text3.grid(column=0,row=3)

#Entries
web_entry=tk.Entry(width=45)
email_entry=tk.Entry(width=45)
pass_entry=tk.Entry(width=45)
web_entry.grid(column=1,row=1,columnspan=2)
email_entry.grid(column=1,row=2,columnspan=2)
pass_entry.grid(column=1,row=3,columnspan=2)

#buttons
button1=tk.Button(text="Generate",command=generate_password)
button1.grid(column=2,row=3,columnspan=2)

button2=tk.Button(text="ADD",width=38,command=add_all)
button2.grid(column=1,row=4,columnspan=2)



window.mainloop()