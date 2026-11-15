from tkinter import *
from tkinter import messagebox
from tkinter import ttk

r=Tk()
# r.geometry("500x400")
r.title("User Registration form")

def submit():
    if un.get()=="" or ue.get()=="" or um.get()=="" or up.get()=="" or uv.get()=="":
        messagebox.showerror("Mat kar lala mat kar","All fields should be filled")
    else:
        if up.get()!=uv.get():
            messagebox.showerror("Error","Passward unmatched")
        elif not ue.get().endswith("@gmail.com"):
                messagebox.showerror("Invalid","email should be ends with @gmail.com")
        elif len(um.get())!=10:
            messagebox.showerror("Mobile Number","Mobile Number should contains 10 digits")
        else:
            if g.get()=="male":
                messagebox.showinfo("Gender","Male gender selected")
            if g.get()=="female":
                messagebox.showinfo("Gender","Female gender selected")

            skill=[]
            if p.get()==1:
                skill.append("Python")
            if c.get()==1:
                skill.append("Rust")
            if j.get()==1:
                skill.append("Java")
                 
            print("User Name:", un.get())
            print("User Email:", ue.get())
            print("Mobile Number:", um.get())
            print("Gender: ",g.get())
            print("Skill: ",skill)
            print("Password:", up.get())
            print("Verify Passward", uv.get())
            print("Division: ",dist.get())
            print("Age: ",age.get())
            print("Process Complete, Have a Good Day!!")

un=StringVar()
ue=StringVar()
um=StringVar()
up=StringVar()
uv=StringVar()
g=StringVar(value="male")
p=IntVar(value=0)
c=IntVar(value=0)
j=IntVar(value=0)
dist=StringVar(value="Nashik")
age=IntVar(value=18)

l0=Label(r,text="Register Here!",font=("Times New Roman",20,"bold"),fg="dark blue")
l0.grid(columnspan=3)

l1=Label(r,text="Enter User Name:",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l1.grid(row=1,column=0,sticky=W)
li=Entry(r,font=("Times New Roman",15),fg="grey",textvariable=un)
li.grid(row=1,column=1,sticky=W)

l2=Label(r,text="Enter User Email: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l2.grid(row=2,column=0,sticky=W)
lii=Entry(r,font=("Times New Roman",15),fg="grey",textvariable=ue)
lii.grid(row=2,column=1,sticky=W)

l3=Label(r,text="Enter Mob Number: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l3.grid(row=3,column=0,sticky=W)
lii=Entry(r,font=("Times New Roman",15),fg="grey",textvariable=um)
lii.grid(row=3,column=1,sticky=W)

l3a=Label(r,text="Select Gender: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l3a.grid(row=4,column=0,sticky=W)
circle1=Radiobutton(r,text="Male",font=("Times New Roman",15),pady=10,padx=10,value="male",variable=g)
circle1.grid(row=4,column=1,sticky=W)
circle2=Radiobutton(r,text="Female",font=("Times New Roman",15),pady=10,padx=10,value="female",variable=g)
circle2.grid(row=5,column=1,sticky=W)

l3b=Label(r,text="Select Skills: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l3b.grid(row=6,column=0,sticky=W)
square1=Checkbutton(r,text="Python",font=("Times New Roman",15),pady=10,padx=10,variable=p)
square1.grid(row=6,column=1,sticky=W)
square2=Checkbutton(r,text="Rust",font=("Times New Roman",15),pady=10,padx=10,variable=c)
square2.grid(row=7,column=1,sticky=W)
square3=Checkbutton(r,text="Java",font=("Times New Roman",15),pady=10,padx=10,variable=j)
square3.grid(row=8,column=1,sticky=W)

l4=Label(r,text="Enter Passward: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l4.grid(row=9,column=0,sticky=W)
lvi=Entry(r,font=("Times New Roman",15),show="*",textvariable=up)
lvi.grid(row=9,column=1,sticky=W)

l5=Label(r,text="Verify Passward: ",font=("Times New Roman",15,"bold"),pady=10,padx=10)
l5.grid(row=10,column=0,sticky=W)
lv=Entry(r,font=("Times New Roman",15),show="*",textvariable=uv)
lv.grid(row=10,column=1,sticky=W)

lz=Label(r,text="Select District: ",font=("Times New Roman",15,"bold"),padx=10,pady=10)
lz.grid(row=11,column=0,sticky=W)
c=ttk.Combobox(r,values=["Amravati","Aurangabaad","Konkan","Nagpur","Nashik","Pune"],font=("Times New Roman",15),textvariable=dist)
c.grid(row=11,column=1,sticky=W)

ly=Label(r,text="Select Age: ",font=("Times New Roman",15,"bold"),padx=10,pady=10)
ly.grid(row=12,column=0,sticky=W)
s=ttk.Spinbox(r,from_=18,to=59,font=("Times New Roman",15),textvariable=age)
s.grid(row=12,column=1,sticky=W)

b1=Button(r,text="Submit",font=("Times New Roman",15,"bold"),padx=25,bg="skyblue",fg="black",command=submit)
b1.grid(row=14,column=0,padx=10,pady=10)

b2=Button(r,text="Exit",font=("Times New Roman",15,"bold"),padx=27,bg="darkred",fg="white")
b2.grid(row=14,column=1,padx=10,pady=10)

r.mainloop()