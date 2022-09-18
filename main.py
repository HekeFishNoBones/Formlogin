import os
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import test

root = Tk()
root.geometry("400x300")    
frm = ttk.Frame(root, padding=10)
frm.grid()

login = tkinter.StringVar()
password = tkinter.StringVar()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'login_details.txt')

def start():
    test.start_vpn(loginBox.get(), passwordBox.get())
    root.destroy()

def Savedata():
    # создание или перезапись файла для хранения логина и пароля
    with open(my_file, "w") as file:
        if os.stat(my_file).st_size == 0:
            file.write("login: " + login.get())
            file.write("\npassword: " + password.get()) 
        else:
            file.flush()
            file.write("login: " + login.get())
            file.write("\npassword: " + password.get()) 
        file.close()

def Loaddata():
    # загрузка логина и пароля, если они уже созданы
    loginBox.delete(0, END)
    passwordBox.delete(0, END)
    with open(my_file, "r") as file:
        if os.stat(my_file).st_size == 0:
            tkinter.messagebox.showwarning(title=None, message="KEKW")
        else:
            details = file.readlines()
            login = details[0][7:]
            ind = login.__len__()
            login = login[:ind - 1]
            password = details[1][10:]

            loginBox.insert(0, login)
            passwordBox.insert(0, password)
        file.close()

def flush():
    loginBox.delete(0, END)
    passwordBox.delete(0, END)
    with open(my_file, "w") as file:
        file.flush()
        file.close()

ttk.Label(frm, text="Login").grid(column=0, row=0)
loginBox = Entry(frm, textvariable = login)
loginBox.grid(column=1, row=0)

ttk.Label(frm, text="Password").grid(column=0, row=1)
passwordBox = Entry(frm, textvariable = password)
passwordBox.grid(column=1, row=1)

#button_icon = tkinter.PhotoImage(file = 'F:\\Memes\\pepega.png')
ttk.Button(frm, text="Save", command=Savedata).grid(column=1, row=2)

# Загрузка данных из файла
ttk.Button(frm, text="Load", command=Loaddata).grid(column=2, row=2)
# Отчистка файла с логином и паролем
ttk.Button(frm, text="Flush", command=flush).grid(column=3, row=2)
# Кнопка запуска скрипта
ttk.Button(frm, text="Connect", command=start).grid(column=3, row=2)

root.mainloop()