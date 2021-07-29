import re
import tkinter as tk
from typing import Counter, Text
from urllib import parse
#消息盒子
import tkinter.messagebox as msgbox
# 操作浏览器
import webbrowser

class movieApp():
    #构造函数
    def __init__(self,width=600,height=500) -> None:
        self.w  = width
        self.h = height
        self.title = '免费播放vip视频（腾讯，爱奇艺）'
        #初始化 tkinter
        self.root = tk.Tk(className=self.title)
        self.root.geometry('{width}x{height}'.format(width=width,height=height))
        self.url = tk.StringVar()
        #控制单选框
        self.v = tk.IntVar()
        self.v.set(1)

        #软件空间划分
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        #软件控件内容设置
        group = tk.Label(frame_1,text='播放通道:',padx=10,pady=10)
        tb = tk.Radiobutton(frame_1,text='唯一通道',variable=self.v,value=1,width=10,height=3)
        
        label = tk.Label(frame_2,text='请输入视频播放地址：')
        entry = tk.Entry(frame_2,textvariable=self.url,highlightcolor='Fuchsia',highlightthickness=1,width=30)
        play = tk.Button(frame_2,text='播放',font=('楷体',12),fg='Purple',width=2,height=1,command=self.video_play)

    #控件布局
        frame_1.pack()
        frame_2.pack()
        group.grid(row=0,column=0)
        tb.grid(row=0,column=1)

        label.grid(row=0,column=0)
        entry.grid(row=0,column=1)

        play.grid(row=0,column=2,ipadx=10,ipady=10) 
    
    def video_play(self):
        port = 'https://www.administratorw.com/video.php?url='
        if re.match(r'https?:/{2}\w.+$',self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='错误',message='视频地址无效，请重新输入')

    
    def loop(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = movieApp()
    app.loop()