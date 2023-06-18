import tkinter
import runpy


top = tkinter.Tk()

def helloCallBack():
    runpy.run_module("volume_track")


B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()