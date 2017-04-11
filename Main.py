from Tkinter import *


class calculate():

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("370x180")

        self.resultwindow = Entry(self.root)
        self.resultwindow.grid(row=0,column=0,columnspan=6)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()  # Sets focus on the input text area

        # Buttons
        self.button1 = Button(self.root, text="1", width=3)
        self.button1.grid(row=1,column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))
        self.button2 = Button(self.root, text="2", width=3)
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))
        self.button3 = Button(self.root, text="3", width=3)
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))
        self.button4 = Button(self.root, text="4", width=3)
        self.button4.grid(row=2, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))
        self.button5 = Button(self.root, text="5", width=3)
        self.button5.grid(row=2, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))
        self.button6 = Button(self.root, text="6", width=3)
        self.button6.grid(row=2, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))
        self.button7 = Button(self.root, text="7", width=3)
        self.button7.grid(row=3, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))
        self.button8 = Button(self.root, text="8", width=3)
        self.button8.grid(row=3, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))
        self.button9 = Button(self.root, text="9", width=3)
        self.button9.grid(row=3, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.buttonplus = Button(self.root, text="+", width=3)
        self.buttonplus.grid(row=1, column=3, padx=3, pady=3)
        self.buttonplus.config(font=("Arial", 18))
        self.buttonminus = Button(self.root, text="-", width=3)
        self.buttonminus.grid(row=1, column=4, padx=3, pady=3)
        self.buttonminus.config(font=("Arial", 18))

        self.buttondivide = Button(self.root, text="/", width=3)
        self.buttondivide.grid(row=2, column=3, padx=3, pady=3)
        self.buttondivide.config(font=("Arial", 18))
        self.buttonmultiply = Button(self.root, text="*", width=3)
        self.buttonmultiply.grid(row=2, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttonresult = Button(self.root, text="=", width=6)
        self.buttonresult.grid(row=3, column=3, padx=3, pady=3, columnspan=2)
        self.buttonresult.config(font=("Arial", 18))

        self.root.mainloop()


if __name__ == "__main__":
    calculate()