from tkinter import *
import runpy
from dark_title_bar import *
from tkinter import messagebox
import mysql.connector


def btn_reg():
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="kunal1234", database="project_record")
    mycursor=mysqldb.cursor()
    upass=edt_upass.get()
    cpass=edt_cpass.get()
    uname=edt_uname.get()
    
    if(upass==cpass):
        mycursor.execute("insert into login(uname,upass) values(%s,%s)",(uname,upass))
        mysqldb.commit()
        mysqldb.close()
       
        window.destroy()
        runpy.run_module("window_log")
        return True
    
    else:
        messagebox.showinfo("","Password doesn't match")
        return False
    

def btn_log():
    window.destroy()
    runpy.run_module("window_log")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#242526")
window.title("Register")
canvas = Canvas(
    window,
    bg = "#242526",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_reg.png")
background = canvas.create_image(
    550, 302,
    image=background_img)

img0 = PhotoImage(file = f"btn_reg.png")
btn_reg = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_reg,
    relief = "flat")

btn_reg.place(
    x = 110, y = 420,
    width = 269,
    height = 51)

img1 = PhotoImage(file = f"btn_login.png")
btn_login = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_log,
    relief = "flat")

btn_login.place(
    x = 110, y = 490,
    width = 269,
    height = 51)

entry0_img = PhotoImage(file = f"edt_uname.png")
entry0_bg = canvas.create_image(
    -242.5, -94.5,
    image = entry0_img)

edt_uname = Entry(
    bd = 0,
    bg = "#454745",
    highlightthickness = 0)

edt_uname.place(
    x = 100, y = 175,
    width = 290.0,
    height = 51)

entry1_img = PhotoImage(file = f"edt_pass.png")
entry1_bg = canvas.create_image(
    -242.5, -11.5,
    image = entry1_img)

edt_upass = Entry(
    bd = 0,
    bg = "#454745",
    highlightthickness = 0)

edt_upass.place(
    x = 100, y = 258,
    width = 290.0,
    height = 51)

entry2_img = PhotoImage(file = f"edt_cpass.png")
entry2_bg = canvas.create_image(
    -242.5, 71.5,
    image = entry2_img)

edt_cpass = Entry(
    bd = 0,
    bg = "#454745",
    highlightthickness = 0)

edt_cpass.place(
    x = 100, y = 341,
    width = 290.0,
    height = 51)

window.resizable(False, False)
dark_title_bar(window)
window.mainloop()

