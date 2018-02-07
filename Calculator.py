from tkinter import*

class Calculator:


     # Defying  functions

    # This function enables  entry to register any button we pressed
    def press_butt(self,text):
        self.entryText=self.display.get()
        self.textLength=len(self.entryText)
        self.display.insert(self.textLength,text)

     #This one deletes everything in the entry
    def clearText(self):
            self.display.delete(0,END)

    #This function calculates the result of math operation,and returns that result to the entry
    def equal_butt(self):
        try:
            result=eval(self.display.get())
        except:
            "Errot"
        self.display.delete(0,END)
        self.display.insert(0,result)

     # Off calculator function
    def quit():
        root.quit

    #This here is our main function
    def __init__(self,master):

        frame=Frame(root,width=20,height=70)
        frame.grid()

        # Making our Entry
        self.display=Entry(root,font="Serif 18",relief=RAISED,justify=RIGHT)
        self.display.grid(row=0,columnspan=5)

        #  fourth row
        self.button7=Button(root,text="7",command=lambda: self.press_butt("7"))
        self.button7.grid(row=1,column=0,sticky="NWNESWSE")

        self.button8=Button(root,text="8",command=lambda: self.press_butt("8"))
        self.button8.grid(row=1,column=1,sticky="NWNESWSE")

        self.button9=Button(root,text="9",command=lambda: self.press_butt("9"))
        self.button9.grid(row=1,column=2,sticky="NWNESWSE")

        self.button_div=Button(root,text="/",command=lambda: self.press_butt("/"))
        self.button_div.grid(row=1,column=3,sticky="NWNESWSE")

        self.button_Off=Button(root,text="Off",bg="red",command=quit)
        self.button_Off.grid(row=1,column=4,sticky="NWNESWSE")

        #  third row
        self.button4=Button(root,text="4",command=lambda: self.press_butt("4"))
        self.button4.grid(row=2,column=0,sticky="NWNESWSE")

        self.button5=Button(root,text="5",command=lambda: self.press_butt("5"))
        self.button5.grid(row=2,column=1,sticky="NWNESWSE")

        self.button6=Button(root,text="6",command=lambda: self.press_butt("6"))
        self.button6.grid(row=2,column=2,sticky="NWNESWSE")

        self.button_mult=Button(root,text="*",command=lambda: self.press_butt("*"))
        self.button_mult.grid(row=2,column=3,sticky="NWNESWSE")

        self.button_closeBacklash=Button(root,text=")",command=lambda: self.press_butt(")"))
        self.button_closeBacklash.grid(row=2,column=4,sticky="NWNESWSE")

        #  second row
        self.button1=Button(root,text="1",command=lambda: self.press_butt("1"))
        self.button1.grid(row=3,column=0,sticky="NWNESWSE")

        self.button1=Button(root,text="2",command=lambda: self.press_butt("2"))
        self.button1.grid(row=3,column=1,sticky="NWNESWSE")

        self.button1=Button(root,text="3",command=lambda: self.press_butt("3"))
        self.button1.grid(row=3,column=2,sticky="NWNESWSE")

        self.button_sub=Button(root,text="-",command=lambda: self.press_butt("-"))
        self.button_sub.grid(row=3,column=3,sticky="NWNESWSE")

        self.button_openBacklash=Button(root,text="(",command=lambda: self.press_butt("("))
        self.button_openBacklash.grid(row=3,column=4,sticky="NWNESWSE")

       #  first row
        self.button0=Button(root,text="0",command=lambda: self.press_butt("0"))
        self.button0.grid(row=4,column=0,sticky="NWNESWSE")

        self.button_eq=Button(root,text="=",command=lambda: self.equal_butt())
        self.button_eq.grid(row=4,column=1,sticky="NWNESWSE")

        self.button_C=Button(root,text="C",command=lambda: self.clearText())
        self.button_C.grid(row=4,column=2,sticky="NWNESWSE")

        self.button_add=Button(root,text="+",command=lambda: self.press_butt("+"))
        self.button_add.grid(row=4,column=3,sticky="NWNESWSE")

        self.button_dott=Button(root,text=".",command=lambda: self.press_butt("."))
        self.button_dott.grid(row=4,column=4,sticky="NWNESWSE")
        root.title("Basic Calculator")


root=Tk()

app=Calculator(root)
root.mainloop()
