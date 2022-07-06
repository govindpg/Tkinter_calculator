import tkinter
import tkinter as Tk

calculation=" "

def add_to_cal(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    pass

def evalute_cal():
    global calculation
    try:
        calculation=str(eval(calculation))

        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")
        pass
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
    pass

root=tkinter.Tk()
root.title("cal")
root.geometry("300x300")

text_result=tkinter.Text(root,height=2,width=30)
text_result.grid(columnspan=5)

btn1=tkinter.Button(root,text="1",command=lambda:add_to_cal(1),width=5)
btn1.grid(row=2,column=1)
btn2=tkinter.Button(root,text="2",command=lambda:add_to_cal(2),width=5)
btn2.grid(row=2,column=2)
btn3=tkinter.Button(root,text="3",command=lambda:add_to_cal(3),width=5)
btn3.grid(row=2,column=3)
btn4=tkinter.Button(root,text="4",command=lambda:add_to_cal(4),width=5)
btn4.grid(row=2,column=4)
btn5=tkinter.Button(root,text="5",command=lambda:add_to_cal(5),width=5)
btn5.grid(row=2,column=5)
btn6=tkinter.Button(root,text="6",command=lambda:add_to_cal(6),width=5)
btn6.grid(row=3,column=1)
btn7=tkinter.Button(root,text="7",command=lambda:add_to_cal(7),width=5)
btn7.grid(row=3,column=2)
btn8=tkinter.Button(root,text="8",command=lambda:add_to_cal(8),width=5)
btn8.grid(row=3,column=3)
btn9=tkinter.Button(root,text="9",command=lambda:add_to_cal(9),width=5)
btn9.grid(row=3,column=4)
btn0=tkinter.Button(root,text="0",command=lambda:add_to_cal(0),width=5)
btn0.grid(row=3,column=5)
btnplus=tkinter.Button(root,text="+",command=lambda:add_to_cal("+"),width=5)
btnplus.grid(row=4,column=1)
btnminus=tkinter.Button(root,text="-",command=lambda:add_to_cal("-"),width=5)
btnminus.grid(row=4,column=2)
btndiv=tkinter.Button(root,text="/",command=lambda:add_to_cal("/"),width=5)
btndiv.grid(row=4,column=3)
btnmul=tkinter.Button(root,text="*",command=lambda:add_to_cal("*"),width=5)
btnmul.grid(row=4,column=4)

btnclr=tkinter.Button(root,text="clr",command=clear_field,width=5)
btnclr.grid(row=5,column=2,columnspan=2)

btnequal=tkinter.Button(root,text="=",command=lambda:evalute_cal(),width=5)
btnequal.grid(row=4,column=5)



root.mainloop()
