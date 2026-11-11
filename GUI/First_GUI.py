from tkinter import *

def display():
    print("I don’t have bugs… I have unexpected features.")

root=Tk()
# root.geometry("600x400")
root.resizable(True,True)
root.title("My First GUI Application")

Label(root,text="you are not welcome", font=("Callibary",50,"bold")).grid(column=0,row=0)
Label(root,text="Do you wanna listen boaring jokes?", font=("Arial",30,"bold")).grid(column=0,row=2)
b1=Button(root,text="Just Click Here!",font=("Arial",30,"bold"),command=display).grid(column=0,row=3)
root.mainloop()