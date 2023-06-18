from tkinter import *
import runpy
from dark_title_bar import *
import subprocess


def volume():
    runpy.run_module("volume_track")
    
def mouse():
    runpy.run_module("mouse_track")
    
def snip():
    runpy.run_module("snip_control1")
    
def drag():
    runpy.run_module("drag1")
    
def btn_clicked():
    path='ClikAI_manual.pdf'
    subprocess.Popen([path],shell=True)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#242526")
window.title("ClickAI")
canvas = Canvas(
    window,
    bg = "#242526",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    775, 302,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = volume,
    relief = "flat")

b0.place(
    x = 67, y = 100,
    width = 421,
    height = 104)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 400, y = 25,
    width = 152,
    height = 58)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = mouse,
    relief = "flat")

b2.place(
    x = 67, y = 200,
    width = 421,
    height = 104)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = snip,
    relief = "flat")

b3.place(
    x = 67, y = 300,
    width = 421,
    height = 104)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = drag,
    relief = "flat")

b4.place(
    x = 67, y = 400,
    width = 421,
    height = 104)

window.resizable(False, False)
dark_title_bar(window)
window.mainloop()
