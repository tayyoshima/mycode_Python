import tkinter as tk
root = tk.Tk()

tk.Button(root,text='A', bg = "yellow").pack(side=tk.RIGHT,fill = tk.BOTH, expand=True)
tk.Button(root,text='B', bg = "yellow").pack(side=tk.RIGHT,fill = tk.BOTH, expand=True)
tk.Button(root,text='C', bg = "yellow").pack(side=tk.RIGHT,fill = tk.BOTH, expand=True)
tk.Button(root,text='D', bg = "yellow").pack(side=tk.RIGHT,fill = tk.BOTH, expand=True)

root.mainloop()