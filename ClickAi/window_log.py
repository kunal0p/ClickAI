from tkinter import *
import runpy
from tkinter import messagebox
from dark_title_bar import *
import mysql.connector


def btn_clicked():
   
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="kunal1234", database="project_record")
    mycursor=mysqldb.cursor()
    uname=edt_luname.get()
    upass=edt_lpass.get()
    
    sql="select * from login where uname = %s and upass = %s"
    mycursor.execute(sql,[(uname),(upass)])
    results=mycursor.fetchall()
    
    if results:
        window.destroy()
        runpy.run_module("window")
        return True
    
    else:
        messagebox.showinfo("","incorrect username and password")
        return False
    
     
        

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#242526")
window.title("Login")
canvas = Canvas(
    window,
    bg = "#242526",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_log.png")
background = canvas.create_image(
    550, 302,
    image=background_img)

img0 = PhotoImage(file = f"btn_reg.png")

img1 = PhotoImage(file = f"btn_login.png")
btn_llogin = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btn_llogin.place(
    x = 110, y = 380,
    width = 269,
    height = 51)

entry0_img = PhotoImage(file = f"edt_uname.png")
entry0_bg = canvas.create_image(
    -242.5, -94.5,
    image = entry0_img)

edt_luname = Entry(
    bd = 0,
    bg = "#454745",
    highlightthickness = 0,
    fg="#fff",
    font=('Times',16))

edt_luname.place(
    x = 100, y = 180,
    width = 290.0,
    height = 51)

entry1_img = PhotoImage(file = f"edt_pass.png")
entry1_bg = canvas.create_image(
    -242.5, -11.5,
    image = entry1_img)

edt_lpass = Entry(
    bd = 0,
    bg = "#454745",
    highlightthickness = 0,
    show="*",
    fg="#fff",
    font=('Times',16))

edt_lpass.place(
    x = 100, y = 296,
    width = 290.0,
    height = 51)


window.resizable(False, False)
dark_title_bar(window)
window.mainloop()

