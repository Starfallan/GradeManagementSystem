# 登陆窗口，从 admin_table 和 user_table 检验登陆是否成功
# 如登陆成功，从 UI.py 中调用可以进行 grade_table 数据库操作的窗口

from tkinter import *
from tkinter.messagebox import *
from admin_table import *
from user_table import *
import gradeUI


def WrongUI():
    showinfo(title="wrong", message="用户名或密码错误")


#    不知道 tkinter.messagebox 的时候手写了一个
#    win_wrong = Tk()
#    win_wrong.title('!')
#    lblWrong = Label(win_wrong, text='用户名或密码错误')
#    btnWrong = Button(win_wrong, text='确定', command = win_wrong.destroy)
#
#    lblWrong.pack()
#    btnWrong.pack()
#
#    win_wrong.mainloop()


def LogIn(ID, PW, isAdmin):
    if isAdmin == 1:
        print(ID, PW)
        if ExistAdmin(ID, PW) == True:
            gradeUI.AdminUI(ID)
        else:
            WrongUI()
    else:
        if ExistUser(ID, PW) == True:
            gradeUI.UserUI(ID)
        else:
            WrongUI()


def RegUI():
    win_reg = Tk()
    win_reg.title("--")

    # 窗口居中显示
    width, height = 190, 140
    win_reg.geometry(
        "%dx%d+%d+%d"
        % (
            width,
            height,
            (win_reg.winfo_screenwidth() - width) / 2,
            (win_reg.winfo_screenheight() - height) / 2,
        )
    )

    isAdmin = IntVar()
    # isAdmin.set(0)

    # 创建控件
    lblID = Label(win_reg, text="用户名:")
    lblPw = Label(win_reg, text="密码：")
    lblText = Label(win_reg, text="*****用户名和密码默认为学号*****")
    entID = Entry(win_reg, width=15)
    entPW = Entry(win_reg, width=15, show="*")
    btnLogin = Button(win_reg, text="登陆")
    btnCheck = Checkbutton(
        win_reg, text="管理员登陆", variable=isAdmin, onvalue=1, offvalue=0
    )

    # 使用网格布局
    lblID.grid(row=0, column=0, pady=5, sticky=E)
    lblPw.grid(row=1, column=0, sticky=E)
    btnLogin.grid(row=3, column=0, pady=5)
    btnCheck.grid(row=3, column=1, pady=5)
    lblText.grid(row=4, column=0, columnspan=2, pady=5)
    entID.grid(row=0, column=1, pady=5)
    entPW.grid(row=1, column=1, pady=5)

    # 点登陆，把输入的ID和PW传出，然后进行检验
    def Ready(self):
        ID, PW = entID.get(), entPW.get()
        LogIn(ID, PW, isAdmin.get())

    # 绑定登陆按钮执行上述 ready() 操作
    btnLogin.bind("<Button-1>", Ready)

    win_reg.mainloop()


def showUI():
    RegUI()
