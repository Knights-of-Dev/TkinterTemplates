#brings up a login window; if the login = the correct variables it brings up a new window :3



import tkinter as tk






#functions
def leave():
    root.destroy()









def Mainwindow():
    pass




#window set up / settings
root = tk.Tk()
root.title("Basic login set up :3")
root.geometry("300x200")

#widgits being created
exit = tk.Button(root, command = leave)
username = tk.Entry(root)
password = tk.Entry(root)


#add widget to windows :3
exit.grid(row= 3, column= 2)
username.grid(row= 0, column= 1)
password.grid(row= 0, column= 1)


root.mainloop()





