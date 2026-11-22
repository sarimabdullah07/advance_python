from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

# with open("All_STU_Marks.csv","w") as A:
#     A.write("1,2,3")
#     A.close()

r=Tk()
r.title("MARKS ENTRY FROM")
style = ttk.Style()

style.configure(
    "Custom.TCombobox",
    font=("Bahnschrift SemiLight", 15),
    foreground="#800000"
)
style.configure(
    "Custom.TSpinbox",
    font=("Bahnschrift SemiLight", 12),
    foreground="#B04739",
)

def submit():
    
    total=int(DS.get())+int(JF.get())+int(OS.get())
    percent=round(total/3,2)
    if 100>percent>90:
        grade="O"
    elif 90>=percent>80:
        grade="A"
    elif 80>=percent>70:
        grade="B"
    elif 70>=percent>60:
        grade="C"
    elif 60>percent>50 :
        grade="D"
    elif 50>percent>40 :
        grade="E"
    else:
        grade="Fail"

    D=DS.get()
    J=JF.get()
    O=OS.get()
    if roll.get()=="" or Name.get()=="" or Class.get()=="" or gender.get()=="" or DS.get()=="" or JF.get()=="" or OS.get()=="":
        messagebox.showerror("Unfilled","All fields should be filled in")
    elif int(D)>100 or int(J)>100 or int(O)>100:
        messagebox.showerror("Digit","Marks should be less than or equal to 100")
    else:
        Dict = {"Roll no.": roll.get(),"Name": Name.get(),"Class": Class.get(),
    "Gender": gender.get(),"DSA": DS.get(),"Java": JF.get(),"OSY": OS.get(),
    "Total": total,"Percentage": percent,"Grade":grade}
        with open("All_STU_Marks.csv","a",newline="") as A:
            fields=["Roll no.","Name","Class","Gender","DSA","Java","OSY","Total","Percentage","Grade"]
            w=csv.DictWriter(A,fieldnames=fields)
            # w.writeheader()
            w.writerow(Dict)
            A.close()
        messagebox.showinfo("Complete","Marks Submitted Successfully")

roll=StringVar(value="1")
Name=StringVar()
Class=StringVar(value="None")
gender=StringVar(value="Male")
DS=StringVar()
JF=StringVar()
OS=StringVar()

a=Label(r,text="Student Marks Entry Form",font=("Arial Rounded MT Bold",20),pady=17,fg="#C3751F")
a.grid(columnspan=3)

b=Label(r,text="Roll no: ",padx=10,font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
b.grid(row=1,column=2,sticky="W")
c=ttk.Spinbox(r,from_=0,to=100,width=5,font=("Bahnschrift SemiLight",15),textvariable=roll,style="Custom.TSpinbox")
c.grid(row=1,column=2,padx=(100,20))

d=Label(r,text="Enter Name: ",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
d.grid(row=1,column=0,sticky="W")
e=Entry(r,width=23,fg="#B04739",font=("Bahnschrift SemiLight",15),textvariable=Name)
e.grid(row=1,column=1)

f=Label(r,text="Select Gender: ",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
f.grid(row=2,column=0,sticky="W")
g=Radiobutton(r,text="Male",font=("Bahnschrift SemiLight",15),fg="#800000",pady=10,variable=gender,value="Male")
g.grid(row=2,column=1,sticky="W")
h=Radiobutton(r,text="Female",font=("Bahnschrift SemiLight",15),fg="#800000",pady=10,variable=gender,value="Female")
h.grid(row=2,column=1,padx=(100,0))


i=Label(r,text="Select your Class: ",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
i.grid(row=3,column=0,sticky="W")
j=ttk.Combobox(r,
               values=["FY (Diploma)","SY (Diploma)","TY (Diploma)","FE (Degree)","SE (Degree)","TE (Degree)","BE (Degree)"],
               width=15,font=("Bahnschrift SemiLight",15),
               textvariable=Class,style="Custom.TCombobox")
j.grid(row=3,column=1,pady=10)

k=Label(r,text="Enter Marks: ",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
k.grid(row=4,column=0,sticky="W")

l=Label(r,text="Data Structure:",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
l.grid(row=4,column=1,sticky="W")
m=Entry(r,width=8,fg="#B04739",font=("Bahnschrift SemiLight",15),textvariable=DS)
m.grid(row=4,column=2,pady=10)

n=Label(r,text="Java Fundamentals:",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
n.grid(row=5,column=1,sticky="W")
o=Entry(r,width=8,fg="#B04739",font=("Bahnschrift SemiLight",15),textvariable=JF)
o.grid(row=5,column=2,pady=10)

p=Label(r,text="Operating System:",font=("Bahnschrift SemiLight",15),pady=10,fg="#800000")
p.grid(row=6,column=1,sticky="W")
q=Entry(r,width=8,fg="#B04739",font=("Bahnschrift SemiLight",15),textvariable=OS)
q.grid(row=6,column=2,pady=10)

s=Button(r,text="Submit",padx=30,pady=5,font=("Bahnschrift SemiLight",15),fg="#800000",command=submit)
s.grid(row=8,column=0,pady=10)
t=Button(r,text="Clear",padx=30,pady=5,font=("Bahnschrift SemiLight",15),fg="#800000")
t.grid(row=8,column=1,pady=10)
u=Button(r,text="Exit",padx=30,pady=5,font=("Bahnschrift SemiLight",15),fg="#800000")
u.grid(row=8,column=2,pady=10)

r.mainloop()