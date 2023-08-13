from tkinter import*
def clear(): #ปุ่มลบ
    global expression
    global lable_show_cal
    result="0"
    expression=""
    lable_show_cal.set(result)
def press(number):    #สร้างคำสั่งให้กดเลขได้
    global expression
    global lable_show_cal
    expression = expression + number
    lable_show_cal.set(expression)
def equal():
    try:  #แสดงผลออกมาได้คำตอบเท่าไหร่
        global expression
        global lable_show_cal
        result = str(eval(expression))
        lable_show_cal.set(result)
    except: #ถ้าหาไม่ได้จะเกิด
        result="Error"
        expression=""
        lable_show_cal.set(result)    
m=Tk() #ชื่อ
m.option_add("font","consolas 30")
lable_show_cal=StringVar()
lable_show_cal.set(0)
expression=""

Label(m,textvariable=lable_show_cal,bg="gold").grid(row=0,column=0,columnspan=4,sticky="news")
Button(m,text="clear",command=clear).grid(row=1,column=0,columnspan=4)

Button (m,text="7",command=lambda:press("7")).grid(row=2,column=0) #สร้างปุ่มขึ้นมา
Button (m,text="8",command=lambda:press("8")).grid(row=2,column=1)
Button (m,text="9",command=lambda:press("9")).grid(row=2,column=2)
Button (m,text="/",command=lambda:press("/")).grid(row=2,column=3)

Button (m,text="4",command=lambda:press("4")).grid(row=3,column=0)
Button (m,text="5",command=lambda:press("5")).grid(row=3,column=1)
Button (m,text="6",command=lambda:press("6")).grid(row=3,column=2)
Button (m,text="*",command=lambda:press("*")).grid(row=3,column=3)

Button (m,text="1",command=lambda:press("1")).grid(row=4,column=0)
Button (m,text="2",command=lambda:press("2")).grid(row=4,column=1)
Button (m,text="3",command=lambda:press("3")).grid(row=4,column=2)
Button (m,text="-",command=lambda:press("-")).grid(row=4,column=3)

Button (m,text="0",command=lambda:press("0")).grid(row=5,column=0)
Button (m,text=".",command=lambda:press(".")).grid(row=5,column=1,columnspan=2,sticky="news")
Button (m,text="+",command=lambda:press("+")).grid(row=5,column=3)

Button (m,text="=",command=equal).grid(row=6,column=0,columnspan=4,sticky="news")
m.mainloop() 