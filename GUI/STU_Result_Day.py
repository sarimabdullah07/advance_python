from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

r=Tk()
r.title("Result")
style = ttk.Style()

style.configure("Treeview",
                font=("Bahnschrift SemiLight",15),
                rowheight=35,foreground="#11125E")

# Apply bold font to headings
style.configure("Treeview.Heading",
                font=("Bahnschrift SemiLight",15,"bold"),
                foreground="#11125E",
                padding=(10,10))


a=Label(r,text="Student Results",font=("Arial Rounded MT Bold",23),pady=17,fg="#264258")
a.grid(row=0,column=0)

#treeview declaration
head=["Sr.No.","Name","Roll No.","Class","DSA","JAVA","OSY","Total","Percent","Grade"]
tree1=ttk.Treeview(r,columns=head,show="headings",height=6)

#create columns
tree1.column("Sr.No.",anchor=CENTER,width=50)
tree1.column("Name",anchor=CENTER,width=150)
tree1.column("Roll No.",anchor=CENTER,width=70)
tree1.column("Class",anchor=CENTER,width=90)
tree1.column("DSA",anchor=CENTER,width=70)
tree1.column("JAVA",anchor=CENTER,width=80)
tree1.column("OSY",anchor=CENTER,width=70)
tree1.column("Total",anchor=CENTER,width=90)
tree1.column("Percent",anchor=CENTER,width=120)
tree1.column("Grade",anchor=CENTER,width=50)

#Create Headings
tree1.heading("Sr.No.",text="Sr.No.")
tree1.heading("Name",text="Name")
tree1.heading("Roll No.",text="Roll No.")
tree1.heading("Class",text="Class")
tree1.heading("DSA",text="DSA")
tree1.heading("JAVA",text="JAVA")
tree1.heading("OSY",text="OSY")
tree1.heading("Total",text="Total")
tree1.heading("Percent",text="Percent")
tree1.heading("Grade",text="Grade")

#Add data into the rows
Sr=[1,2,3,4,5,6]
Name=["ALice","Bob","Charlie","David","Eve","Frank"]
Roll=[12,43,65,32,76,14]
Class=["TE","SE","SE","BE","TE","FE"]
Dsa=[87,69,85,70,58,95]
jav=[79,50,78,59,49,60]
os=[74,95,92,79,59,76]
total=[240,214,255,208,166,231]
percent=[80.00,71.33,85.00,69.33,55.33,77.00]
grade=["A","B","A","C","D","B"]

for i in range(len(Sr)):
    tree1.insert("",END,values=(Sr[i],Name[i],Roll[i],Class[i],Dsa[i],jav[i],os[i],total[i],percent[i],grade[i]))


tree1.grid(row=1,column=0,padx=10,pady=10)
r.mainloop()
