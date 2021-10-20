import tkinter as tk

def ce_to_fa():
    ce = inputCe.get()
    fa = (float(ce)*9/5)+32
    label_result["text"] = "  "+str(fa)+" \N{DEGREE FAHRENHEIT}"

window = tk.Tk()
window.iconbitmap("C:/Users/paisitw/Desktop/All my work/หลักสูตร Python Advance (DEMO)/Code_Material/tem.ico")
window.title("โปรแกรมแปลงหน่วยอุณหภูมิ")
window.geometry("400x40")

inputCe = tk.Entry()
inputCe.config(width=20,font=("RSU",10))
inputCe.pack(side='left')

label1 = tk.Label()
label1.config(text=" \N{DEGREE CELSIUS}")
label1.pack(side='left')

button1 = tk.Button(text="=>",width=10,command=ce_to_fa)
button1.pack(side='left')

label_result = tk.Label()
label_result.config(text=" ",font=("RSU",10))
label_result.pack(side='left')

window.mainloop()