from tkinter import*
import tkinter as tk
from tkinter import messagebox
#หน้า UI
ProgramCom = Tk()
ProgramCom.geometry('400x350')
ProgramCom.title('Program Commission')
ProgramCom.configure(background='#6699FF')
#สร้างปุ่ม
Label (ProgramCom,text='Commission',font='20',bg='#6699FF').grid(row=0,column=1)
Label(ProgramCom,text='Enter lock',font='18',bg='#6699FF').grid(row=1,column=0)
Locks = tk.Entry(ProgramCom)
Locks.grid(row=1,column=1)    
Label(ProgramCom,text='Enter stock',font='18',bg='#6699FF').grid(row=2,column=0)
Stocks = tk.Entry(ProgramCom)
Stocks.grid(row=2,column=1)
Label(ProgramCom, text='Enter barrel', font='18', bg='#6699FF').grid(row=3,column=0)
Barrels = tk.Entry(ProgramCom)
Barrels.grid(row=3,column=1)
#result Commission
Label(ProgramCom, text='', font='18', bg='#6699FF').grid(row=4,column=1)
Com = Button(ProgramCom, text='Calculate Commission', font='12', bg='green', command= lambda: rule()).grid(row=5,column=1)
calculate_commis = Label(ProgramCom)
calculate_commis.grid(row=6,column=1)
def rule():
    try:
        lock = int(Locks.get())
        if lock < 1 : messagebox.showinfo("Error Lock","Enter a positive value")
        elif lock > 70 : messagebox.showinfo("Error","lock must not exceed 70 ")
        stock = int(Stocks.get())
        if stock < 1 : messagebox.showinfo("Error Stock","Enter a positive value")
        elif stock > 80 : messagebox.showinfo("Error","stock must not exceed 80 ")
        barrel = int(Barrels.get())
        if barrel < 1 : messagebox.showinfo("Error Barrel","Enter a positive value")
        elif barrel > 90 : messagebox.showinfo("Error","barrel must not exceed 90 ")   
    
    except ValueError: messagebox.showinfo("Error","Enter a numberic value")
    if lock > 0 and stock > 0 and barrel > 0:
        commission = Calculate(lock,stock,barrel)
        calculate_commis.config(text="You get commission " + str(commission))
    else:
        messagebox.showinfo("Error","Enter a positive value")

    #calculate_commis.config(text="You get commission " + str(commission))
def Calculate(lock,stock,barrel):#คำนวณ
    sales = (45 * lock ) + (30 * stock) + (25 * barrel)
    if (sales <= 1000):
        commission = 0.10 * 1000
        commission = commission + 0.10 * sales 
    elif (sales <= 1800):
        commission = 0.10 * 1000
        commission = commission + 0.15 * (sales - 1000)
    else:
        commission = commission + 0.15 * 800
        commission = commission + 0.20 * (sales - 1800)
    return commission 
def clear():
    Locks.delete(0,END)
    Barrels.delete(0,END)
    Stocks.delete(0,END)
Clear = Button( text='Clear', font='12', bg='red', command= clear).grid(row=7,column=1)

ProgramCom.mainloop()