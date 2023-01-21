#!/user/bin/env python
# -*- coding:utf-8 -*-
# @software: Visual Studio Code
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import tkinter as tk
import ctypes
import webbrowser
import time
import threading
from ttkthemes import*
from time import strftime
import winsound
import socket
import getpass
import os
import sys
from tkinter.scrolledtext import ScrolledText
from pynput.keyboard import Key, Controller
#root=Tk()
root=ThemedTk(theme="adapta", toplevel=True, themebg=True)
winWidth = 720
winHeight = 480
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry(f"{winWidth}x{winHeight}+{x}+{y}")
root.title("社交软件重复发送信息工具")
root.resizable(0,0)
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
keyboard = Controller()

label_1 = Label(root,
                   text='社交软件重复发送信息工具',
                   font=("Microsoft YaHei UI", 14))
label_1.pack()
label_2 = Label(root,
                   text='运行提示',
                   font=("Microsoft YaHei UI", 10))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
label_3 = Label(root,
                   text='控制中心',
                   font=("Microsoft YaHei UI", 10))
label_3.place(relx=0.55, y=40, relwidth=0.45, height=25)
label_4 = Label(root,
                   text='输入',
                   font=("Microsoft YaHei UI", 10))
label_4.place(relx=0.03, y=195, relwidth=0.45, height=25)
class hello(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait() 
            time.sleep(0.2)
            keyboard.type(textExample.get("1.0","end"))
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
threads = []
t = hello()
threads.append(t)
t.pause()
if __name__ == '__main__':
    for t in threads:
        t.daemon=True
        t.start()

def control():
    control['state'] = DISABLED
    end['state'] = NORMAL
    textExample['state'] = DISABLED
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n")
    state.insert(INSERT, "您可以点击“停止运行”从而停止运行程序\n注意：你需要将软件发送消息的按键改为enter")
    t.resume()
def end():  
    control['state'] = NORMAL
    end['state'] = DISABLED
    textExample['state'] = NORMAL
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：空闲\n")
    state.insert(INSERT, "您可以在“输入”中输入你想重复发送的内容后点击“开始运行”从而运行程序")
    state.configure(state='disabled')
    t.pause()
def minimize():
    root.iconify()
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
def t_close_handler():
    root.attributes("-disabled", 0)
    window.destroy()
def status():
    def apply():
        alpha = scale.get()
        alpha = alpha / 100
        root.attributes('-alpha',alpha)
        acc = round(alpha,2)
        viewa = f"当前设定值:{str(acc)}"
                
            

    if demoStatus.get():
        global window
        window = Toplevel(root)
        window.geometry("620x300+200+250")
        window.title("透明效果设置")
        root.attributes('-alpha',0.85)
        tip2_window = Label(window,
                    text='透明效果设置\n',
                    font=("Microsoft YaHei UI", 12),
                    foreground="black")
        tip2_window.pack()
        scale = Scale(window, from_=10, to_=96,orient=HORIZONTAL,length=220)
        scale.set(85)
        scale.pack()

        root.attributes('-disabled', 1)#Top=window
        tip_window = Label(window,
                    text='提示：\n'
                    '通过拖动或点击滑动条设置主窗口透明度。\n'
                            '数值越小，透明程度越高；数值越大，则反之\n'
                            '建议的值为85-95之间，默认值为85',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
        tip_window.pack()






        apply = Button(window,
                    text='应用',
                    command=apply)
        apply.place(relx=0.4, y=260, relwidth=0.2, height=35)
        window.resizable(0,0)
        window.attributes('-toolwindow', True)
        window.protocol("WM_DELETE_WINDOW", t_close_handler)
        #window.mainloop()

    else:
        root.attributes('-alpha',1)
def topview():
    if homoStatus.get():
        root.attributes('-topmost', -1)
    else:
       root.attributes('-topmost', 0)    

state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
state.place(relx=0.03, y=70, relwidth=0.5, height=120)
state.insert(INSERT, "当前状态：空闲\n")
state.insert(INSERT, "您可以在“输入”中输入你想重复发送的内容后点击“开始运行”从而运行程序")
state.configure(state='disabled')
control = Button(root, text ="开始运行", command = control)
control.place(relx=0.55, y=70, relwidth=0.4, height=60)
end = Button(root, text ="停止运行", command = end)
end.place(relx=0.55, y=130, relwidth=0.4, height=60)
end['state'] = DISABLED


textExample=Text(root) 
textExample.place(relx=0.02, y=230, relwidth=0.96, height=200)

menubar = Menu(root)


winmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Window', menu=winmenu)
demoStatus = BooleanVar()
demoStatus.set(False)
homoStatus = BooleanVar()
homoStatus.set(False)
winmenu.add_checkbutton(label = "透明效果",command=status,variable=demoStatus)
winmenu.add_checkbutton(label = "窗口前置",command=topview,variable=homoStatus)
root.config(menu=menubar)
winmenu.add_separator()
winmenu.add_command(label='退出程序', command=root.quit)
    
    


#<Button - 3>
rightmenu = Menu(root,tearoff=False)
rightmenu.add_command(label="Minimize",command=minimize)
rightmenu.add_command(label="Exit",command=root.destroy)
root.bind("<Button-3>",showPopupMenu)

root.mainloop()
