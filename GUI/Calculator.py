from tkinter import *

window_root=Tk()
# window_root.geometry("1024x600")
window_root.resizable(True,True)
window_root.title("My First GUI Application by Python")

Label(window_root,text="Caluculator",font=("Old English Text MT",50,"bold")).grid(row=0,column=1)

button_1=Button(window_root,text="1",font=("Elephant",30,"bold"),padx=70,pady=5)
button_1.grid(row=1,column=0)

button_2=Button(window_root,text="2",font=("Elephant",30,"bold"),padx=70,pady=5)
button_2.grid(row=1,column=1)

button_3=Button(window_root,text="3",font=("Elephant",30,"bold"),padx=70,pady=5)
button_3.grid(row=1,column=2)

button_4=Button(window_root,text="4",font=("Elephant",30,"bold"),padx=70,pady=5)
button_4.grid(row=2,column=0)

button_5=Button(window_root,text="5",font=("Elephant",30,"bold"),padx=70,pady=5)
button_5.grid(row=2,column=1)

button_6=Button(window_root,text="6",font=("Elephant",30,"bold"),padx=70,pady=5)
button_6.grid(row=2,column=2)

button_7=Button(window_root,text="7",font=("Elephant",30,"bold"),padx=70,pady=5)
button_7.grid(row=3,column=0)

button_8=Button(window_root,text="8",font=("Elephant",30,"bold"),padx=70,pady=5)
button_8.grid(row=3,column=1)

button_9=Button(window_root,text="9",font=("Elephant",30,"bold"),padx=70,pady=5)
button_9.grid(row=3,column=2)

button_0=Button(window_root,text="0",font=("Elephant",30,"bold"),padx=70,pady=5)
button_0.grid(row=4,column=1)

button_p=Button(window_root,text="+",font=("Elephant",30,"bold"),padx=70,pady=40)
button_p.grid(row=1,column=4)

button_m=Button(window_root,text="-",font=("Elephant",30,"bold"),padx=80,pady=40)
button_m.grid(row=2,column=4)

button_e=Button(window_root,text="=",font=("Elephant",30,"bold"),padx=70,pady=40)
button_e.grid(row=3,column=4)

window_root.mainloop()
