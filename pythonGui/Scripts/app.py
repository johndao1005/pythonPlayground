import tkinter as tk
from tkinter import filedialog, Text
import os # make app to run app
root = tk.Tk() #html like which is the root of applications
apps=[]
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir ="/", title="Slect File",filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg="gray")
        label.pack(fill=str)
def runApp():
    for app in apps:
        os.startfile(app)
canvas = tk.Canvas(root, height = 700, width = 700, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg="pink")
frame.place(relwidth = 0.8, relheight = 0.8, relx =0.1,rely=0.1)
openfile = tk.Button(root, text="Open File",padx=10, command =addApp)
openfile.pack()
runApps = tk.Button(root,text="Run Apps",padx=10,pady=5,fg="white",bg="Black", command=runApp)
runApps.pack()
root.mainloop()

with open('save.text', 'w') as f:
    for app in apps:
        f.write(app + ',')
