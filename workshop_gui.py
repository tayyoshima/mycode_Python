import tkinter as tk

window = tk.Tk()
window.geometry("500x600")

def showText():
    lbShow.configure(text="Hello World")

def hideText():
    lbShow.configure(text=" ")

bt1 = tk.Button(text = "Show Text",font=("TH Sarabun PSK",50),command=showText)
bt1.pack()

bt2 = tk.Button(text = "Hide Text",font=("TH Sarabun PSK",50),command=hideText)
bt2.pack()

lbShow = tk.Label(text="Hello World")
lbShow.pack()
window.mainloop()