import tkinter as tk
import os,time
from ctypes import windll
import pyautogui as pag
from pynput.keyboard import Listener
import threading
import random
import sys
import pyautogui

import win32api
import win32con,win32gui
import cv2

pyautogui.PAUSE = 0.1
window = tk.Tk()
window.title('yys')
##窗口尺寸
window.geometry('700x500')
class yys_class(object):
    def __init__(self):

        self.stad = 1     # 是否启动
        self.i = 1       # 鼠标两个位置移动
        self.img_sbtf = "1"    # 是否开启识别图片
        self.tim = 0     # 定时关闭
        self.zhonrw = 0   # 等于1时关闭
        self.xziimg = "juz.png"    #识别图片
        self.kun28_sta = 0
        self.kun28_notsta = 0

        self.sb1 = 0.8    # 协助
        self.sb2 = 0.6    # 接受邀请
        self.sb3 = 0.6    # 宝箱
        self.sb4 = 0.6    # 点击确定
        self.sb5 = 0.6    # 打小怪
        self.sb6 = 0.5    # 打boos
        self.sb7 = 0.7    # 点击探索
        self.sb8 = 0.7    # 点击挑战

        self.s_x,self.s_y = 0, 0
        self.f_x, self.f_y = 0, 0
        self.kun28pylian = 50
        self.dtime = '{}'
        self.csh = 0
        self.cj_tszj()
        self.time_daoj = tk.Label(window,text='',font=('Arial', 13),bg='red')
    # 创建探索组件
    def cj_tszj(self):
        self.spboxvar4 = tk.StringVar()
        self.spboxvar5 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var3.set('10')

        def tsms_xz():
            # print(var3.get())
            self.kun28_notsta = int(self.var3.get())
            self.sb2 = float(self.spinbox4.get())
            self.sb3 = float(self.spinbox5.get())

            self.sb4 = float(self.spinbox21.get())
            self.sb5 = float(self.spinbox22.get())
            self.sb6 = float(self.spinbox23.get())
            self.sb7 = float(self.spinbox24.get())
            self.sb8 = float(self.spinbox25.get())
            self.kun28pylian = int(self.spinbox26.get())
            self.save_pz()

        self.l8 = tk.Label(window, text="探索模式选择:")
        self.r8 = tk.Radiobutton(window, text='坐车', variable=self.var3, value='0', command=tsms_xz)
        self.r9 = tk.Radiobutton(window, text='队长', variable=self.var3, value='1', command=tsms_xz)
        self.r10 = tk.Radiobutton(window, text='我都要', variable=self.var3, value='4', command=tsms_xz)
        self.r11 = tk.Radiobutton(window, text='单人探索', variable=self.var3, value='5', command=tsms_xz)

        self.l9 = tk.Label(window, text="接受邀请识别率:")
        self.spboxvar4.set(0.6)
        self.spboxvar5.set(0.7)

        self.spinbox4 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                              command=tsms_xz, textvariable=self.spboxvar4)

        self.l10 = tk.Label(window, text="输入宝箱识别率:")
        self.spinbox5 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                              command=tsms_xz, textvariable=self.spboxvar5)

        self.sl21 = tk.Label(window, text="点击确定识别率:")
        self.sl22 = tk.Label(window, text="攻击小怪识别率:")
        self.l23 = tk.Label(window, text="攻击boos识别率:")
        self.l24 = tk.Label(window, text="点击探索识别率:")
        self.l25 = tk.Label(window, text="点击挑战识别率:")
        self.l26 = tk.Label(window, text="小怪偏移量:")
        self.spboxvar21 = tk.StringVar()  # 点击确定识别率
        self.spboxvar22 = tk.StringVar()  # 攻击小怪识别率
        self.spboxvar23 = tk.StringVar()  # 攻击boos识别率
        self.spboxvar24 = tk.StringVar()  # 点击探索识别率
        self.spboxvar25 = tk.StringVar()  # 点击挑战识别率
        self.spboxvar26 = tk.StringVar()  # 小怪偏移量
        self.spboxvar21.set(0.6)
        self.spboxvar22.set(0.6)
        self.spboxvar23.set(0.5)
        self.spboxvar24.set(0.7)
        self.spboxvar25.set(0.8)
        self.spboxvar26.set(50)
        self.spinbox21 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                               command=tsms_xz, textvariable=self.spboxvar21)
        self.spinbox22 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                               command=tsms_xz, textvariable=self.spboxvar22)
        self.spinbox23 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                               command=tsms_xz, textvariable=self.spboxvar23)
        self.spinbox24 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                               command=tsms_xz, textvariable=self.spboxvar24)
        self.spinbox25 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                               command=tsms_xz, textvariable=self.spboxvar25)
        self.spinbox26 = tk.Spinbox(window, from_='0', to='100000', increment=10, width=5,
                                    command=tsms_xz, textvariable=self.spboxvar26)
    def mrpz(self):
        self.spboxvar1 = tk.StringVar()
        self.spboxvar2 = tk.StringVar()
        self.spboxvar1.set(0)
        self.spboxvar2.set(1)
        spinbox1 = tk.Spinbox(window, from_='0', to='100', increment=0.2, width=5,
                              textvariable=self.spboxvar1)
        spinbox2 = tk.Spinbox(window, from_='0', to='100', increment=0.2, width=5,
                              textvariable=self.spboxvar2)

        # shijsz()
        # scale = tk.Scale(window,orient = tk.HORIZONTAL,from_ = 50,to = 80,resolution = 0.5)
        # l4 = tk.Label(window, height=2, text='间隔时间',state = "disabled")
        l5 = tk.Label(window, height=2, text='间隔最短时间：')
        l6 = tk.Label(window, height=2, text='间隔最长时间：')

        l5.grid(row=4, column=1, columnspan=2, sticky='W')
        spinbox1.grid(row=4, column=3, sticky='W')
        l6.grid(row=4, column=4, sticky='W')
        spinbox2.grid(row=4, column=5, sticky='W')

        timevar = tk.StringVar()
        def timesz():
            if var2.get() == '1':
                b1 = tk.Button(window, text="开始定时", command=sta_time)
                spinbox10 = tk.Spinbox(window, from_='0', to='100000', increment=10, width=5,textvariable=timevar)
                spinbox10.grid(row=5, column=4, sticky='W')
                b1.grid(row=5, column=5, sticky='W')
            else:
                b1 = tk.Button(window, text="开始定时", command=sta_time,state="disabled")
                spinbox10 = tk.Spinbox(window, from_='0', to='100000', increment=10, width=5,state="disabled",textvariable=timevar)
                spinbox10.grid(row=5, column=4, sticky='W')
                b1.grid(row=5, column=5, sticky='W')



        def sta_time():
            self.tim = timevar.get()
            thread4.start()

        var2 = tk.StringVar()
        l7 = tk.Label(window, text="是否开启定时:")
        var2.set('2')
        r6 = tk.Radiobutton(window, text='是', variable=var2, value='1', command=timesz)
        r7 = tk.Radiobutton(window, text='否', variable=var2, value='2', command=timesz)
        l7.grid(row=5, column=1, columnspan=2, sticky='W')
        r6.grid(row=5, column=3, sticky='W')
        r7.grid(row=5, column=6, columnspan=2, sticky='W')

        timesz()


        if self.var.get() == '3':
            self.kun28_sta = 1
            self.l8.grid(row=6, column=1, columnspan=2, sticky='W')
            self.r8.grid(row=6, column=3, sticky='W')
            self.r9.grid(row=6, column=4, sticky='W')
            self.l9.grid(row=7, column=1, columnspan=2, sticky='W')
            self.spinbox4.grid(row=7, column=3, sticky='W')
            self.r10.grid(row=6, column=5, sticky='W')
            self.r11.grid(row=6, column=6, sticky='W')
            self.sl21.grid(row=9, column=1, columnspan=2, sticky='W')
            self.spinbox21.grid(row=9, column=3, sticky='W')
            self.sl22.grid(row=10, column=1, columnspan=2, sticky='W')
            self.spinbox22.grid(row=10, column=3, sticky='W')
            self.l23.grid(row=11, column=1, columnspan=2, sticky='W')
            self.spinbox23.grid(row=11, column=3, sticky='W')
            self.l24.grid(row=12, column=1, columnspan=2, sticky='W')
            self.spinbox24.grid(row=12, column=3, sticky='W')
            self.l25.grid(row=13, column=1, columnspan=2, sticky='W')
            self.spinbox25.grid(row=13, column=3, sticky='W')
            self.l26.grid(row=14, column=1, columnspan=2, sticky='W')
            self.spinbox26.grid(row=14, column=3, sticky='W')
            self.l10.grid(row=8, column=1, columnspan=2, sticky='W')
            self.spinbox5.grid(row=8, column=3, sticky='W')
            self.kun28_notsta = int(self.var3.get())
            self.sb2 = float(self.spinbox4.get())
            self.sb3 = float(self.spinbox5.get())
            self.sb4 = float(self.spinbox21.get())
            self.sb5 = float(self.spinbox22.get())
            self.sb6 = float(self.spinbox23.get())
            self.sb7 = float(self.spinbox24.get())
            self.sb8 = float(self.spinbox25.get())
            self.kun28pylian = int(self.spinbox26.get())
        else:
            self.kun28_sta = 0
            self.kun28_notsta = 0

            # l8.grid(row=6, column=1, columnspan=2, sticky='W')
            self.l8.grid_remove()
            self.r8.grid_remove()
            self.r9.grid_remove()
            self.l9.grid_remove()
            self.spinbox4.grid_remove()
            self.r10.grid_remove()
            self.r11.grid_remove()
            self.sl21.grid_remove()
            self.spinbox21.grid_remove()
            self.sl22.grid_remove()
            self.spinbox22.grid_remove()
            self.l23.grid_remove()
            self.spinbox23.grid_remove()
            self.l24.grid_remove()
            self.spinbox24.grid_remove()
            self.l25.grid_remove()
            self.spinbox25.grid_remove()
            self.l26.grid_remove()
            self.spinbox26.grid_remove()

            self.l10.grid_remove()
            self.spinbox5.grid_remove()




        def XieZhu():
            self.sb1 = float(spboxvar20.get())
            if var4.get() == '1':
                self.img_sbtf = "1"
                self.xziimg = "jies.png"
            elif var4.get() == '3':
                self.img_sbtf = "1"
                self.xziimg = "juz.png"
                # self.sb1 = 0.8
            elif var4.get() == '2':
                # self.img_sbtf = "1"
                pass

            self.save_pz()
        var4 = tk.StringVar()
        var4.set('3')
        spboxvar20=tk.StringVar()
        spboxvar20.set(0.8)
        l11 = tk.Label(window, text="自动接受协助:")
        r12 = tk.Radiobutton(window, text='自动接受', variable=var4, value='1', command=XieZhu)
        r13 = tk.Radiobutton(window, text='自动拒绝', variable=var4, value='3', command=XieZhu)
        r14 = tk.Radiobutton(window, text='关闭', variable=var4, value='2', command=XieZhu)
        lspinbox20 = tk.Label(window, text='协助识别率：')
        spinbox20 = tk.Spinbox(window, from_='0', to='1', increment=0.1, width=5,
                              command=XieZhu, textvariable=spboxvar20)
        if var4.get() == '1':
            self.img_sbtf = "1"
            self.xziimg = "jies.png"
        elif var4.get() == '3':
            self.img_sbtf = "1"
            self.xziimg = "juz.png"
            # self.sb1 = 0.8
        elif var4.get() == '2':
            # self.img_sbtf = "1"
            pass
        l11.grid(row=15, column=1, columnspan=2, sticky='W')
        r12.grid(row=15, column=3, sticky='W')
        r13.grid(row=15, column=4, sticky='W')
        r14.grid(row=15, column=5, sticky='W')
        lspinbox20.grid(row=15, column=6, sticky='W')
        spinbox20.grid(row=15, column=7, sticky='W')
        def x_yfw():
            self.s_x = int(spinbox6.get())
            self.s_y = int(spinbox7.get())

            self.save_pz()

        spboxvar6 = tk.StringVar()
        spboxvar7 = tk.StringVar()
        spboxvar6.set(8)
        spboxvar7.set(10)
        l12 = tk.Label(window, text="x轴、y轴的随机移动范围:")
        l13 = tk.Label(window, text="x轴:", width=5)
        l14 = tk.Label(window, text="y轴:", )
        spinbox6 = tk.Spinbox(window, from_='0', to='1000', increment=1, width=5, command=x_yfw,textvariable=spboxvar6)
        spinbox7 = tk.Spinbox(window, from_='0', to='1000', increment=1, width=5, command=x_yfw,textvariable=spboxvar7)
        self.s_x = int(spinbox6.get())
        self.s_y = int(spinbox7.get())
        l12.grid(row=16, column=1, columnspan=3, sticky='W')
        l13.grid(row=16, column=4)
        spinbox6.grid(row=16, column=5)
        l14.grid(row=16, column=6, sticky='W')
        spinbox7.grid(row=16, column=7, sticky='W')

        def x_yYXfw():
            self.f_x = int(spinbox8.get())
            self.f_y = int(spinbox9.get())

            self.save_pz()
        spboxvar8 = tk.StringVar()
        spboxvar9 = tk.StringVar()
        spboxvar8.set(30)
        spboxvar9.set(30)
        l15 = tk.Label(window, text="x轴、y轴的允许移动的范围:")
        l16 = tk.Label(window, text="x轴:", width=5)
        l17 = tk.Label(window, text="y轴:", )
        spinbox8 = tk.Spinbox(window, from_='0', to='1000', increment=1, width=5,command=x_yYXfw,textvariable=spboxvar8)
        spinbox9 = tk.Spinbox(window, from_='0', to='1000', increment=1, width=5,command=x_yYXfw,textvariable=spboxvar9)
        self.f_x = int(spinbox8.get())
        self.f_y = int(spinbox9.get())
        l15.grid(row=17, column=1, columnspan=3, sticky='W')
        l16.grid(row=17, column=4)
        spinbox8.grid(row=17, column=5)
        l17.grid(row=17, column=6, sticky='W')
        spinbox9.grid(row=17, column=7, sticky='W')

        l20 = tk.Label(window,text='f2开始，f3停止',font=('Arial', 14))
        lstak = tk.Label(window,text='当前状态是：',font=('Arial', 12))
        self.lstak2 = tk.Label(window, text='停止', font=('Arial', 13),bg='red')
        self.l21 = tk.Label(window,text='第一个定位是(f4定位)：',font=('Arial', 10))
        self.l22 = tk.Label(window, text='第二个定位是(f5定位)：',font=('Arial', 10))
        l20.grid(row=18, column=4, columnspan=3, sticky='W')
        lstak.grid(row=19, column=2, sticky='W')
        self.lstak2.grid(row=19, column=3, columnspan=3, sticky='W')
        self.l21.grid(row=20, column=2,columnspan=2)
        self.l22.grid(row=20, column=5,columnspan=2)

        if self.var1.get() == '1':

            type_ = self.var.get()
            with open("type" + type_ + ".txt", "r") as f:
                all_text = f.read().split(";")

                self.kslee_time, self.enmslee_time = float(all_text[0].split(",")[0]), float(all_text[0].split(",")[1])
                self.spboxvar1.set(self.kslee_time)
                self.spboxvar2.set(self.enmslee_time)
                # spinbox2.insert('2')

                self.s_x,self.s_y = int(all_text[1].split(",")[0]), int(all_text[1].split(",")[1])
                # print(self.s_x,self.s_y)
                spboxvar6.set(self.s_x)
                spboxvar7.set(self.s_y)
                self.f_x, self.f_y = int(all_text[2].split(",")[0]), int(all_text[2].split(",")[1])
                spboxvar8.set(self.f_x)
                spboxvar9.set(self.f_y)
                self.dtime = all_text[3]

                self.tim = int(all_text[4])

                ##
                self.img_sbtf = all_text[5]
                ##
                self.xziimg = all_text[6]
                if self.xziimg == "jies.png":
                    var4.set('1')
                elif self.xziimg =="juz.png":
                    var4.set('3')
                else:
                    var4.set('2')

                self.sb1 = float(all_text[7])
                spboxvar20.set(self.sb1)
                self.sb2 = float(all_text[8])
                self.spboxvar4.set(self.sb2)
                self.sb3 = float(all_text[9])
                self.spboxvar5.set(self.sb3)
                self.kun28_notsta = int(all_text[10])
                self.var3.set(self.kun28_notsta)

                self.sb4 = float(all_text[11])
                self.spboxvar21.set(self.sb4)

                self.sb5 = float(all_text[12])
                self.spboxvar22.set(self.sb5)

                self.sb6 = float(all_text[13])
                self.spboxvar23.set(self.sb6)

                self.sb7 = float(all_text[14])
                self.spboxvar24.set(self.sb7)

                self.sb8 = float(all_text[15])
                self.spboxvar25.set(self.sb8)
                xz = "3"
                # print("\n-----------------默认配置-------------------|\n"
                #       "|1、间隔时间为{}-{}  \n"
                #       "|2、x轴移动范围为{}，y轴移动范围为{} \n"
                #       "|3、x轴最大移动范围为{}，y轴最大移动范围为{}\n"
                #       "|4、拒绝或接受邀请的识别率为{}\n"
                #       "|5、接受组队邀请的识别率为{}\n"
                #       "|6、宝箱的识别率为{}\n"
                #       "|注意：如果上次有设置定时等配置也保存了下来\n"
                #       "|--------------------------------------------|\n".format(self.kslee_time, self.enmslee_time, self.s_x, self.s_y, self.f_x,
                #                                                                 self.f_y, self.sb1, self.sb2, self.sb3))
                f.close()
        self.csh=1
    def save_pz(self):
        with open("type" + self.var.get() + ".txt", "w") as f:
            f.write(str(self.spboxvar1.get()) + "," + str(self.spboxvar2.get()) + ";")
            f.write(str(self.s_x) + "," + str(self.s_y) + ";")
            f.write(str(self.f_x) + "," + str(self.f_y) + ";")
            f.write(self.dtime + ";")
            f.write(str(self.tim) + ";")
            f.write(self.img_sbtf + ";")
            f.write(self.xziimg + ";")
            f.write(str(self.sb1) + ";")
            f.write(str(self.sb2) + ";")
            f.write(str(self.sb3) + ";")
            f.write(str(self.kun28_notsta) + ";")
            f.write(str(self.sb4) + ";")
            f.write(str(self.sb5) + ";")
            f.write(str(self.sb6) + ";")
            f.write(str(self.sb7) + ";")
            f.write(str(self.sb8) + ";")
            f.close()
    def sheZhi(self):


        type = self.var.get()
        # print(type)
        self.var1 = tk.StringVar()
        if os.path.exists("type" + type + ".txt"):

            l3 = tk.Label(window, height=2, text='是否用默认配置：')
            r4 = tk.Radiobutton(window, text='是', variable=self.var1, value='1', command=self.mrpz)
            r5 = tk.Radiobutton(window, text='否', variable=self.var1, value='2', command=self.mrpz)
            l3.grid(row=3, column=1, columnspan=2, sticky='W')
            r4.grid(row=3, column=3, sticky='W')
            r5.grid(row=3, column=4, sticky='W')
            self.var1.set('1')
        else:
            l3 = tk.Label(window, height=2, text='是否用默认配置：', state="disabled")
            r4 = tk.Radiobutton(window, text='是', variable=self.var1, value='1', command=self.mrpz, state="disabled")
            r5 = tk.Radiobutton(window, text='否', variable=self.var1, value='2', command=self.mrpz, state="disabled")
            l3.grid(row=3, column=1, columnspan=2, sticky='W')
            r4.grid(row=3, column=3, sticky='W')
            r5.grid(row=3, column=4, sticky='W')
            self.var1.set('2')

        self.mrpz()
    def stadyys(self):
        # kslee_time, enmslee_time= input("输入两个数将在这两个数内随机间隔点击：")

        self.var = tk.StringVar()
        # l = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
        # l1 = tk.Label(window, height=2, text='模式：')
        # def print_selection(self):
        #     l.config(text='选择的模式是' + self.var.get())
        #     l.config(text='选择的模式是' + self.var.get())
            # type_ = self.var.get()



            # mrpz_mok(type_)

        # 创建几个Radiobutton
        r1 = tk.Radiobutton(window, text='单人',
                            variable=self.var, value='1',
                            command=self.sheZhi,
                            )

        r2 = tk.Radiobutton(window, text='双人',
                            variable=self.var, value='2',
                            command=self.sheZhi,
                            )

        r3 = tk.Radiobutton(window, text='探索',
                            variable=self.var, value='3',
                            command=self.sheZhi,
                            )
        self.var.set(1)
        r1.grid(row=1, column=1, sticky='W')
        r2.grid(row=1, column=2, sticky='W')
        r3.grid(row=1, column=3, sticky='W')


        while 1:

            if self.zhonrw ==1:
                sys.exit()
            if self.var.get() == "2" or self.kun28_notsta==4:
                while True:
                    if self.zhonrw ==1:
                        sys.exit()
                    if self.stad == 1:
                        time.sleep(1)
                        break
                    # print("Press Ctrl-C to end")


                    if self.i==1:
                        self.one_xx, self.one_yx = self.one_x, self.one_y
                        if (self.one_xx - self.one_x < self.f_x and self.one_xx - self.one_x > -self.f_x) and (self.one_yx - self.one_y < self.f_y and self.one_yx - self.one_y > -self.f_y):
                            self.one_xx += random.randint(-self.s_x, self.s_x)
                            self.one_yx += random.randint(-self.s_y, self.s_y)
                            windll.user32.SetCursorPos(self.one_xx, self.one_yx)
                        else:
                            x, y = self.one_x, self.one_y
                            self.one_xx = self.one_x
                            self.one_yx = self.one_y
                            windll.user32.SetCursorPos(x, y)
                        self.i=2

                    elif self.i==2:
                        self.two_xx, self.two_yx = self.two_x, self.two_y
                        if (self.two_xx - self.two_x < self.f_x and self.two_xx - self.two_x > -self.f_x) and (
                                self.two_yx - self.two_y < self.f_y and self.two_yx - self.two_y > -self.f_y):
                            self.two_xx += random.randint(-self.s_x, self.s_x)
                            self.two_yx += random.randint(-self.s_y, self.s_y)
                            windll.user32.SetCursorPos(self.two_xx, self.two_yx)
                        else:
                            x, y = self.two_x, self.two_y
                            self.two_xx = self.two_x
                            self.two_yx = self.two_y
                            windll.user32.SetCursorPos(x, y)
                        self.i = 1
                    # print(posStr)   打印坐标
                    pag.click()
                    # time.sleep(random.random())
                    time.sleep(random.uniform(float(self.spboxvar1.get()), float(self.spboxvar2.get())))

            elif self.kun28_notsta==0 or self.kun28_notsta ==5:
                # print('456789')
                yuan_x, yuan_y = pag.position()
                self.yuan_one_x, self.yuan_one_y = yuan_x, yuan_y
                while 1:
                    if self.zhonrw ==1:
                        sys.exit()
                    if self.stad == 1:
                        time.sleep(1)
                        break
                    #print("Press Ctrl-C to end")
                    x, y = pag.position()  # 返回鼠标的坐标


                    if (self.yuan_one_x - yuan_x < self.f_x and self.yuan_one_x - yuan_x> -self.f_x) and (self.yuan_one_y - yuan_y < self.f_y and self.yuan_one_y - yuan_y > -self.f_y):
                        self.yuan_one_x += random.randint(-self.s_x,self.s_x)
                        self.yuan_one_y += random.randint(-self.s_y,self.s_y)
                        windll.user32.SetCursorPos(self.yuan_one_x, self.yuan_one_y)
                    else:
                        self.yuan_one_x = yuan_x
                        self.yuan_one_y = yuan_y
                        windll.user32.SetCursorPos(yuan_x, yuan_y)
                    #print(posStr)   打印坐标
                    pag.click()
                    # windll.user32.SetCursorPos(x, y)

                    time.sleep(random.uniform(float(self.spboxvar1.get()), float(self.spboxvar2.get())))
            else:
                time.sleep(5)

    def stad_press(self,key):
        print(key)

    def emd_press(self,key):
        if str(key)=="Key.f3":
            self.stad=1
            self.lstak2.config(text='停止',bg='red')
            # print("停止")
        elif str(key)=="Key.f2":
            self.stad = 0
            self.lstak2.config(text='开始',bg='green')

        elif str(key)=="Key.f4":
            self.one_x, self.one_y = pag.position()
            # print("点一坐标：({},{})".format(self.one_x,self.one_y))
            self.l21.config(text='第一个位置是(f4定位)：({},{})'.format(self.one_x,self.one_y))
            print("把鼠标放在第二个位置上按f5(如是探索模式就把鼠标放在向右移动的位置上)")
        elif str(key)=="Key.f5":
            self.two_x, self.two_y = pag.position()
            # print("点二坐标：({},{})".format(self.two_x, self.two_y))
            self.l22.config(text='第二个位置是(f5定位)：({},{})'.format(self.two_x, self.two_y))
            print("点击f2开始，f3停止")
        elif str(key)=="Key.f11":
            sys.exit()


    def stad_yys(self):

        with Listener(on_press=self.stad_press) as listener:
            print(listener.join())

    def jc_emd(self):

        with Listener(on_press=self.emd_press) as listener:
            listener.join()


    def img_sb(self):
        while 1:
            if self.zhonrw == 1:
                sys.exit()
            time.sleep(2.5)
            if self.stad == 1 or self.img_sbtf == "2":
                pass
            else:
                # 图像识别（一个）
                btm = pyautogui.locateOnScreen(self.xziimg, confidence=self.sb1)

                if btm:
                    left, top, width, height = btm
                    center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                    self.jz_click(center)
                    time.sleep(1)
                else:
                    pass
    def jz_click(self,center):
        pyautogui.click(center)
        # pass
    def gbuck(self):
        self.save_pz()
        window.destroy()
        # self.stad = 1
        # self.tim = 0
        # self.zhonrw = 1
        a = os.getpid()
        os.system("taskkill /F /IM "+str(a))
        # win32api.keybd_event(122, 0, 0, 0)  # 按f11
        # time.sleep(0.2)
        # win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        sys.exit(0)



    def times(self):
        if self.tim !=0:
            self.time_daoj.grid(row=5, column=7, sticky='W')
            time_sum = (int(self.tim)*60)
            for i in range(time_sum,0,-1):
                self.time_daoj.config(text='剩下{}秒'.format(i))
                time.sleep(1)
            # self.stad = 1
            # self.tim = 0
            # self.zhonrw = 1
            # print("即将关闭")
            os.system("taskkill /F /IM "+str(os.getpid()))
            sys.exit()


    def kun28_zuoce(self):
        jishu = 0
        pm_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / 2
        pm_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        # hld = win32gui.FindWindow(None, u"阴阳师-网易游戏")
        #
        # left, top, right, bottom = win32gui.GetWindowRect(hld)

        # jl = right - left
        # print(jl / 6)
        while 1:
            if self.zhonrw == 1:
                sys.exit()
            # time.sleep(0.)
            if self.stad == 1 or self.kun28_sta == 0:
                time.sleep(2)
                pass
            else:

                # 图像识别（一个）
                btm = pyautogui.locateOnScreen("kun282.png", confidence=self.sb2,grayscale=True)
                btm2 = pyautogui.locateOnScreen("baox.png", confidence=self.sb3,grayscale=True)

                if (btm and self.kun28_notsta == 0) or (btm and self.kun28_notsta == 4):
                    left, top, width, height = btm
                    center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                    self.jz_click(center)
                elif btm2:

                    left, top, width, height = btm2
                    center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                    self.jz_click(center)
                elif self.kun28_notsta == 1 or self.kun28_notsta == 4:
                    btm3 = pyautogui.locateOnScreen("kun28qued.png", confidence=self.sb4,grayscale=True)
                    btm4 = pyautogui.locateOnScreen("kun28zd.jpg", confidence=self.sb5,grayscale=True,region=(0,0,int(pm_x),pm_y))
                    btm5 = pyautogui.locateOnScreen('kun28boss.png', confidence=self.sb6,grayscale=True,region=(0,0,int(pm_x),pm_y))
                    btm6 = pyautogui.locateOnScreen('kun28ts2.jpg', confidence=self.sb7,grayscale=True)
                    btm7 = pyautogui.locateOnScreen('kun28tiaoz.png', confidence=self.sb8,grayscale=True)
                    if btm3:
                        left, top, width, height = btm3
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm4:
                        left, top, width, height = btm4
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心

                        center2 = pyautogui.center((left-int(self.kun28pylian), top, width, height))
                        self.jz_click(center)
                        self.jz_click(center2)
                    elif btm5:
                        left, top, width, height = btm5
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm6:
                        left, top, width, height = btm6
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm7:
                        left, top, width, height = btm7
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    # else:
                    #     jishu += 1
                    #     if jishu <= 5:
                    #         self.two_xx,self.two_yx = self.two_x,self.two_y
                    #         if (self.two_xx - self.two_x < 7 and self.two_xx - self.two_x > -7) and (
                    #                 self.two_yx - self.two_y < 7 and self.two_yx - self.two_y > -7):
                    #             self.two_xx += random.randint(-7, 7)
                    #             self.two_yx += random.randint(-7, 7)
                    #             windll.user32.SetCursorPos(self.two_xx, self.two_yx)
                    #         else:
                    #             x, y = self.two_x, self.two_y
                    #             self.two_xx = self.two_x
                    #             self.two_yx = self.two_y
                    #             windll.user32.SetCursorPos(x, y)
                    #         pag.click()
                    #         time.sleep(1)
                    #     elif jishu <= 10:
                    #         self.one_xx,self.one_yx = self.one_x, self.one_y
                    #         if (self.one_xx - self.one_x < 7 and self.one_xx - self.one_x > -7) and (
                    #                 self.one_yx - self.one_y < 7 and self.one_yx - self.one_y > -7):
                    #             self.one_xx += random.randint(-7, 7)
                    #             self.one_yx += random.randint(-7, 7)
                    #             windll.user32.SetCursorPos(self.one_xx, self.one_yx)
                    #         else:
                    #             x, y = self.one_x, self.one_y
                    #             self.one_xx = self.one_x
                    #             self.one_yx = self.one_y
                    #             windll.user32.SetCursorPos(x, y)
                    #         pag.click()
                    #         time.sleep(1)
                    #     else:
                    #         jishu = 0

                elif self.kun28_notsta == 5:
                    btm3 = pyautogui.locateOnScreen("kun28qued.png", confidence=self.sb4)
                    btm4 = pyautogui.locateOnScreen("kun28zd.jpg", confidence=self.sb5)
                    btm5 = pyautogui.locateOnScreen('kun28boss.png', confidence=self.sb6)
                    btm6 = pyautogui.locateOnScreen('kun28ts2.jpg', confidence=self.sb7)
                    if btm3:
                        left, top, width, height = btm3
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm4:
                        left, top, width, height = btm4
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm5:
                        left, top, width, height = btm5
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                    elif btm6:
                        left, top, width, height = btm6
                        center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
                        self.jz_click(center)
                else:
                    time.sleep(10)
    # def run(self):



if __name__ == '__main__':
    a = yys_class()
    thread1 = threading.Thread(target=a.stadyys)
    thread2 = threading.Thread(target=a.jc_emd)
    thread3 = threading.Thread(target=a.img_sb)
    thread4 = threading.Thread(target=a.times)
    thread5 = threading.Thread(target=a.kun28_zuoce)

    thread1.start()
    thread2.start()
    thread3.start()
    thread5.start()
    window.protocol("WM_DELETE_WINDOW",a.gbuck)
    window.mainloop()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread1.join()
    sys.exit()
