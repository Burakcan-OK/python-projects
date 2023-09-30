import tkinter as tk

window=tk.Tk()
window.title("Burak Can OK Hesap Makinası")
window.geometry("360x460")
window.resizable(height=False,width=False)
#işlem penceresi
mat_frame=tk.Frame(master=window)
mat_frame.grid(column=0,row=0,sticky="nsew")
def can():
    print(num_entry.delete(0,tk.END))
    print(num_entry1.delete(0,tk.END))
    print(num_result.delete(0,tk.END))
def add():
    a=(num_entry1.get())
    if type(a)==float:
        return a
    elif type(a)==int:
        return a
    y=a+"+"
    print(num_entry1.delete(0,tk.END))
    print(num_entry1.insert(tk.END,y))
    print(num_entry.delete(0,tk.END))
def min():
    a=(num_entry1.get())
    if type(a)==float:
        return a
    elif type(a)==int:
        return a
    y=a+"-"
    print(num_entry1.delete(0,tk.END))
    print(num_entry1.insert(tk.END,y))
    print(num_entry.delete(0,tk.END))
def mul():
    a=(num_entry1.get())
    if type(a)==float:
        return a
    elif type(a)==int:
        return a
    y=a+"*"
    print(num_entry1.delete(0,tk.END))
    print(num_entry1.insert(tk.END,y))
    print(num_entry.delete(0,tk.END))
def div():
    a=(num_entry1.get())
    if type(a)==float:
        return a
    elif type(a)==int:
        return a
    y=a+"/"
    print(num_entry1.delete(0,tk.END))
    print(num_entry1.insert(tk.END,y))
    print(num_entry.delete(0,tk.END))
def equ():
    print(num_result.delete(0,tk.END))
    result=num_entry1.get()
    result=str(eval(result))
    print(num_entry.delete(0,tk.END))
    print(num_entry1.delete(0,tk.END))
    print(num_result.insert(tk.END,result))
    print(num_entry1.insert(tk.END,result))

cnl_bt=tk.Button(master=mat_frame,text="C",pady=10,padx=15,command=can)
cnl_bt.grid(row=0,column=0,ipady=5,ipadx=5)

add_bt=tk.Button(master=mat_frame,text="+",pady=10,padx=15,command=add)
add_bt.grid(row=1,column=0,ipady=5,ipadx=5)

min_bt=tk.Button(master=mat_frame,text="-",pady=10,padx=15,command=min)
min_bt.grid(row=2,column=0,ipady=5,ipadx=5)

mul_bt=tk.Button(master=mat_frame,text="x",pady=10,padx=15,command=mul)
mul_bt.grid(row=3,column=0,ipady=5,ipadx=5)

div_bt=tk.Button(master=mat_frame,text="/",pady=10,padx=15,command=div)
div_bt.grid(row=4,column=0,ipady=5,ipadx=5)

eq_bt=tk.Button(master=mat_frame,text="=",pady=10,padx=15,command=equ)
eq_bt.grid(row=5,column=0,ipady=5,ipadx=5)



# girilen sayı ve sonuç penceresi
entry_frame=tk.Frame(master=window,relief=tk.SUNKEN)
entry_frame.grid(column=1,row=0,sticky="n")

say_label=tk.Label(master=entry_frame,text="SAYI GİRİN",height=3,relief=tk.SUNKEN)
say_label.grid(column=0,row=0,sticky="nsew",padx=10)

num_entry=tk.Entry(master=entry_frame,relief=tk.GROOVE,width=25)
num_entry.grid(column=0,row=1,padx=10,pady=10)

num_entry1=tk.Entry(master=entry_frame,relief=tk.GROOVE,width=25)
num_entry1.grid(column=0,row=2,padx=10,pady=10)

son_label=tk.Label(master=entry_frame,text="SONUÇ",height=3,relief=tk.SUNKEN)
son_label.grid(column=0,row=3,sticky="nsew",padx=10)

num_result=tk.Entry(master=entry_frame,relief=tk.GROOVE,width=25,)
num_result.grid(column=0,row=4,padx=10,pady=10)

#numaralar
num_frame=tk.Frame(master=window,relief=tk.FLAT)
num_frame.grid(column=1,row=1,sticky="n")

def one():
    print(num_entry.insert(tk.END,"1"))
    print(num_entry1.insert(tk.END,"1"))
num_button=tk.Button(master=num_frame,text=1,padx=20,command=one)
num_button.grid(row=0,column=0,sticky="nsew")
def two():
    print(num_entry.insert(tk.END,"2"))
    print(num_entry1.insert(tk.END,"2"))
num_button=tk.Button(master=num_frame,text=2,padx=20,command=two)
num_button.grid(row=0,column=1,sticky="nsew")
def three():
    print(num_entry.insert(tk.END,"3"))
    print(num_entry1.insert(tk.END,"3"))
num_button=tk.Button(master=num_frame,text=3,padx=20,command=three)
num_button.grid(row=0,column=2,sticky="nsew")
def four():
    print(num_entry.insert(tk.END,"4"))
    print(num_entry1.insert(tk.END,"4"))
num_button=tk.Button(master=num_frame,text=4,padx=20,command=four)
num_button.grid(row=1,column=0,sticky="nsew")
def five():
    print(num_entry.insert(tk.END,"5"))
    print(num_entry1.insert(tk.END,"5"))
num_button=tk.Button(master=num_frame,text=5,padx=20,command=five)
num_button.grid(row=1,column=1,sticky="nsew")
def six():
    print(num_entry.insert(tk.END,"6"))
    print(num_entry1.insert(tk.END,"6"))
num_button=tk.Button(master=num_frame,text=6,padx=20,command=six)
num_button.grid(row=1,column=2,sticky="nsew")
def seven():
    print(num_entry.insert(tk.END,"7"))
    print(num_entry1.insert(tk.END,"7"))
num_button=tk.Button(master=num_frame,text=7,padx=20,command=seven)
num_button.grid(row=2,column=0,sticky="nsew")
def eight():
    print(num_entry.insert(tk.END,"8"))
    print(num_entry1.insert(tk.END,"8"))
num_button=tk.Button(master=num_frame,text=8,padx=20,command=eight)
num_button.grid(row=2,column=1,sticky="nsew")

def nine():
    print(num_entry.insert(tk.END,"9"))
    print(num_entry1.insert(tk.END,"9"))
num_button=tk.Button(master=num_frame,text=9,padx=20,command=nine)
num_button.grid(row=2,column=2,sticky="nsew")

def deicimal():
    print(num_entry.insert(tk.END,"."))
    print(num_entry1.insert(tk.END,"."))
num_button=tk.Button(master=num_frame,text=".",padx=20,command=deicimal)
num_button.grid(row=3,column=0,sticky="nsew")

def zero():
    print(num_entry.insert(tk.END,"0"))
    print(num_entry1.insert(tk.END,"0"))
num_button=tk.Button(master=num_frame,text=0,padx=20,command=zero)
num_button.grid(row=3,column=1,sticky="nsew")

def dell():
    a=(len(num_entry1.get())-1)
    print(num_entry1.delete(a))
num_button=tk.Button(master=num_frame,text="\N{LEFTWARDS BLACK ARROW}",padx=20,command=dell)
num_button.grid(row=3,column=2,sticky="nsew")


window.mainloop()
