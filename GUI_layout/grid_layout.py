import tkinter as tk

root = tk.Tk()

tk.Button(root,text='A', bg = "yellow").grid(row=0, column=0, sticky='NSEW')
tk.Button(root,text='B', bg = "yellow").grid(row=0, column=1, sticky='NSEW')
tk.Button(root,text='C', bg = "yellow").grid(row=0, column=2, sticky='NSEW')
tk.Button(root,text='D', bg = "yellow").grid(row=1, column=0, sticky='NSEW')
tk.Button(root,text='E', bg = "yellow").grid(row=1, column=1, sticky='NSEW')
tk.Button(root,text='F', bg = "yellow").grid(row=1, column=2, sticky='NSEW')
tk.Button(root,text='G', bg = "yellow").grid(row=2, column=0, sticky='NSEW')
tk.Button(root,text='H', bg = "yellow").grid(row=2, column=1, sticky='NSEW')
tk.Button(root,text='I', bg = "yellow").grid(row=2, column=2, sticky='NSEW')
root.mainloop()