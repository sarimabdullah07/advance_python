from tkinter import *

def display1():
    print("Process Complete, have a good day!!")
def display2():
    print("Submitted Successfully, NTMU")

r=Tk()
r.title("User Registration form")

l0=Label(r,text="Register Here!",font=("Times New Roman",20,"bold"),fg="grey")
l0.grid(columnspan=3)

l1=Label(r,text="Enter User Name: ",font=("Times New Roman",15,"bold"),pady=10)
l1.grid(row=1,column=0)
li=Entry(r,font=("Times New Roman",15,"bold"),fg="grey")
li.grid(row=1,column=1)

l2=Label(r,text="Enter User Email: ",font=("Times New Roman",15,"bold"),pady=10)
l2.grid(row=2,column=0)
lii=Entry(r,font=("Times New Roman",15,"bold"),fg="grey")
lii.grid(row=2,column=1)

l3=Label(r,text="Enter Mob Number: ",font=("Times New Roman",15,"bold"),pady=10)
l3.grid(row=3,column=0)
lii=Entry(r,font=("Times New Roman",15,"bold"),fg="grey")
lii.grid(row=3,column=1)

l4=Label(r,text="Enter Passward: ",font=("Times New Roman",15,"bold"),pady=10)
l4.grid(row=4,column=0)
lvi=Entry(r,font=("Times New Roman",15,"bold"),show="*")
lvi.grid(row=4,column=1)

l5=Label(r,text="Verify Passward: ",font=("Times New Roman",15,"bold"),pady=10)
l5.grid(row=5,column=0)
lv=Entry(r,font=("Times New Roman",15,"bold"),show="*")
lv.grid(row=5,column=1)

b1=Button(r,text="Submit",font=("Times New Roman",15,"bold"),padx=25,bg="skyblue",fg="black",command=display2)
b1.grid(row=6,column=0)

b2=Button(r,text="Exit",font=("Times New Roman",15,"bold"),padx=27,bg="darkred",fg="white",command=display1)
b2.grid(row=6,column=1)

r.mainloop()