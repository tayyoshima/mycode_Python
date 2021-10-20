import tkinter as tk

window = tk.Tk()
window.geometry("500x300")

lb1 = tk.Label(text='Email',bd=50,font=("TH Sarabun PSK",20))
lb1.grid(row=0, column=0)
txtbox1 = tk.Entry(width=30)
txtbox1.grid(row=0, column=1)

lb2 = tk.Label(text='Password',font=("TH Sarabun PSK",20))
lb2.grid(row=1, column=0)
txtbox2 = tk.Entry(width=30)
txtbox2.grid(row=1, column=1)

window.mainloop()