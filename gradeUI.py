# 创建管理员和用户的操作界面
# 分备完成权限内的全部操作

import grade_table
import user_table
import admin_table
from tkinter import *
from showUI import *
from tkinter.messagebox import *

import matplotlib.pyplot as plt
import numpy as np


def ShowGradeUI(b):
    win_showgrade = Tk()
    win_showgrade.title(" %s 的成绩" % b[0]["stu_name"])
    lbl1 = Label(win_showgrade, text="大学数学:%s " % b[0]["math"]).grid(row=0, column=0)
    lbl2 = Label(win_showgrade, text="大学英语一:%s " % b[0]["english"]).grid(
        row=0, column=2
    )
    lbl3 = Label(win_showgrade, text="程序设计基础一:%s " % b[0]["software"]).grid(
        row=0, column=3
    )
    lbl4 = Label(win_showgrade, text="------GPA:%s------ " % b[0]["gpa"]).grid(
        row=1, column=1, columnspan=3
    )
    win_showgrade.mainloop()


def UserUI(ID):
    # 调用 ShowGradeUI() 显示所有成绩
    def ShowGrade():
        b = grade_table.Select(grade_table.table, ID)
        print(b)
        ShowGradeUI(b)

    # 显示修改密码界面,通过按钮调用 ChangePassword()
    def ChangePasswordUI():
        def Ready():
            user_table.Update(ID, entNewPw.get())
            showinfo(title="", message="修改成功！")

        win_userupdate = Tk()
        lblTip = Label(win_userupdate, text="新密码:").grid(row=0, column=0)
        entNewPw = Entry(win_userupdate, width=15)
        btnUpdate = Button(win_userupdate, text="修改", command=Ready).grid(
            row=1, column=0
        )
        entNewPw.grid(row=0, column=1)
        win_userupdate.mainloop()

    win_user = Tk()
    win_user.title("用户")

    lblTip = Label(win_user, text="欢迎您，%s" % user_table.GetUserName(ID))
    btnSelect = Button(win_user, text="查询我的成绩", command=ShowGrade)
    btnUpdate = Button(win_user, text="修改密码", command=ChangePasswordUI)

    lblTip.pack()
    btnSelect.pack()
    btnUpdate.pack()
    win_user.mainloop()


def AdminUI(adminID):
    win_admin = Tk()
    win_admin.title("管理员")

    def InsertGradeUI():
        win_insert = Tk()

        def Ready():
            if grade_table.Exist(ent0.get()) == True:
                showinfo(title="", message="该学生信息已存在!")
            else:
                x = grade_table.Insert(
                    ent0.get(),
                    ent20.get(),
                    ent1.get(),
                    ent2.get(),
                    ent3.get(),
                    ent4.get(),
                )
                showinfo(title="", message="成功！")

        lbl0 = Label(win_insert, text="学号:").grid(row=0, column=1)
        ent0 = Entry(win_insert, width=12)
        ent0.grid(row=0, column=2)
        lbl20 = Label(win_insert, text="姓名:").grid(row=0, column=3)
        ent20 = Entry(win_insert, width=8)
        ent20.grid(row=0, column=4)
        lbl1 = Label(win_insert, text="大学数学:").grid(row=1, column=1)
        ent1 = Entry(win_insert, width=4)
        ent1.grid(row=1, column=2)
        lbl2 = Label(win_insert, text="大学英语一:").grid(row=1, column=3)
        ent2 = Entry(win_insert, width=4)
        ent2.grid(row=1, column=4)
        lbl3 = Label(win_insert, text="程序设计基础一:").grid(row=2, column=1)
        ent3 = Entry(win_insert, width=4)
        ent3.grid(row=2, column=2)
        lbl4 = Label(win_insert, text="GPA:").grid(row=3, column=1)
        ent4 = Entry(win_insert, width=5)
        ent4.grid(row=3, column=3, sticky=W)
        btn0 = Button(win_insert, text="增加学生成绩", command=Ready).grid(
            row=8, column=0, columnspan=6
        )

        win_insert.mainloop()

    def ChangePasswordUI():
        def Ready():
            admin_table.Update(adminID, entNewPw.get())
            showinfo(title="", message="修改成功！")

        win_adminupdate = Tk()
        lblTip = Label(win_adminupdate, text="新密码:").grid(row=0, column=0)
        entNewPw = Entry(win_adminupdate, width=15)
        btnUpdate = Button(win_adminupdate, text="修改", command=Ready).grid(
            row=1, column=0
        )
        entNewPw.grid(row=0, column=1)
        win_adminupdate.mainloop()

    def SelectGradeUI():
        def Ready():
            if grade_table.Exist(entID.get()) == False:
                showinfo(title="", message="学号输入错误!")
            else:
                b = grade_table.Select(grade_table.table, entID.get())
                ShowGradeUI(b)

        win_enter = Tk()
        lbl0 = Label(win_enter, text="请输入学生学号:")
        entID = Entry(win_enter, width=15)
        btnEnter = Button(win_enter, text="查看成绩", command=Ready)
        lbl0.grid(row=0, column=0)
        entID.grid(row=1, column=0)
        btnEnter.grid(row=2, column=0)
        win_enter.mainloop()

    def DeleteGradeUI():
        def Ready():
            if grade_table.Exist(entID.get()) == False:
                showinfo(title="", message="学号输入错误!")
            else:
                b = grade_table.Delete(grade_table.table, entID.get())
                showinfo(title="", message="删除成功!")

        win_enter = Tk()
        lbl0 = Label(win_enter, text="请输入学生学号:")
        entID = Entry(win_enter, width=15)
        btnEnter = Button(win_enter, text="删除成绩", command=Ready)
        lbl0.grid(row=0, column=0)
        entID.grid(row=1, column=0)
        btnEnter.grid(row=2, column=0)
        win_enter.mainloop()

    def UpdateOne():
        win_update = Tk()

        def Ready():
            if grade_table.Exist(ent0.get()) == False:
                showinfo(title="", message="学号输入错误!")
            else:
                grade_table.Update(
                    ent0.get(),
                    ent20.get(),
                    ent1.get(),
                    ent2.get(),
                    ent3.get(),
                    ent4.get(),
                )
                showinfo(title="", message="成功!")
                b = grade_table.Select(grade_table.table, ent0.get())
                ShowGradeUI(b)

        lbl0 = Label(win_update, text="学号:").grid(row=0, column=1)
        ent0 = Entry(win_update, width=12)
        ent0.grid(row=0, column=2)
        lbl20 = Label(win_update, text="姓名:").grid(row=0, column=3)
        ent20 = Entry(win_update, width=8)
        ent20.grid(row=0, column=4)
        lbl1 = Label(win_update, text="大学数学:").grid(row=1, column=0)
        ent1 = Entry(win_update, width=3)
        ent1.grid(row=1, column=1)
        lbl2 = Label(win_update, text="大学英语一:").grid(row=1, column=2)
        ent2 = Entry(win_update, width=3)
        ent2.grid(row=1, column=3)
        lbl3 = Label(win_update, text="程序设计基础一:").grid(row=1, column=4)
        ent3 = Entry(win_update, width=3)
        ent3.grid(row=1, column=5)
        lbl4 = Label(win_update, text="GPA:").grid(row=2, column=1)
        ent4 = Entry(win_update, width=5)
        ent4.grid(row=2, column=2, sticky=W)
        lbl5 = Label(win_update, text="--------请输入学生的全部成绩信息--------")
        btn0 = Button(win_update, text="修改学生成绩", command=Ready).grid(
            row=3, column=0, columnspan=6
        )

        win_update.mainloop()

    # # 这里有很大问题，子函数没有封装好，把所有情况全写了一遍。主要是不会用按钮传参数，只能写不带参数的函数。
    # def SelectAll():
    #     def select_1():  # 注意字符串和整数转换
    #         grade_list = []  # 存有所有人 dw1_grade 的列表
    #         b_grade = grade_table.Select1(1)
    #         for i in b_grade:
    #             grade_list.append(i["math"])  # i 是 b_dw1 字典中的每一行
    #         print(grade_list)
    #         grade = np.zeros(101)  # 考 i 分的有 grade[i] 人
    #         for i in range(-1, 101):
    #             grade[i] = grade_list.count(str(i))
    #         # print(grade)
    #         i = np.arange(-1, 101, 1)
    #         plt.plot(i, grade[i], "r-")
    #         plt.show()

    #     def select_2():
    #         grade_list = []
    #         b_grade = grade_table.Select1(2)
    #         for i in b_grade:
    #             grade_list.append(i["english"])
    #         print(grade_list)
    #         grade = np.zeros(101)
    #         for i in range(-1, 101):
    #             grade[i] = grade_list.count(str(i))
    #         # print(grade)
    #         i = np.arange(-1, 101, 1)
    #         plt.plot(i, grade[i], "b-")
    #         plt.show()

    #     def select_3():
    #         grade_list = []
    #         b_grade = grade_table.Select1(3)
    #         for i in b_grade:
    #             grade_list.append(i["software"])
    #         print(grade_list)
    #         grade = np.zeros(101)
    #         for i in range(-1, 101):
    #             grade[i] = grade_list.count(str(i))
    #         # print(grade)
    #         i = np.arange(-1, 101, 1)
    #         plt.plot(i, grade[i], "y-")
    #         plt.show()

    #     win_selectall = Tk()
    #     lbl0 = Label(win_selectall, text="您要查看哪门课的成绩情况？").grid(
    #         row=0, column=0, columnspan=3
    #     )
    #     btn1 = Button(win_selectall, text="大学数学", command=select_1).grid(
    #         row=1, column=0
    #     )
    #     btn2 = Button(win_selectall, text="大学英语一", command=select_2).grid(
    #         row=1, column=1
    #     )
    #     btn3 = Button(win_selectall, text="程序设计基础一", command=select_3).grid(
    #         row=1, column=2
    #     )
    #     win_selectall.mainloop()

    def Select_course():
        def select_grade(grade_name, course_id):
            plt.rcParams["font.family"] = ["STSong"]
            plt.title("班级成绩分布")
            grade_list = []
            b_grade = grade_table.SelectSingle(course_id)
            if b_grade is None:
                print("没有找到该课程的成绩记录")
                return
            for i in b_grade:
                grade_list.append(int(i[grade_name]))
            grade_count = {"不及格": 0, "一般": 0, "中": 0, "良": 0, "优秀": 0}
            for grade in grade_list:
                if grade < 60:
                    grade_count["不及格"] += 1
                elif grade < 70:
                    grade_count["一般"] += 1
                elif grade < 80:
                    grade_count["中"] += 1
                elif grade < 90:
                    grade_count["良"] += 1
                else:
                    grade_count["优秀"] += 1
            labels = []
            sizes = []
            for grade, count in grade_count.items():
                labels.append(grade + "：" + str(count))
                sizes.append(count)
            plt.pie(sizes, labels=labels, autopct="%1.1f%%")
            plt.legend(loc="upper right")
            plt.show()

        win_selectall = Tk()
        lbl0 = Label(win_selectall, text="您要查看哪门课的成绩情况？").grid(
            row=0, column=0, columnspan=3
        )
        btn1 = Button(
            win_selectall, text="大学数学", command=lambda: select_grade("math", 1)
        ).grid(row=1, column=0)
        btn2 = Button(
            win_selectall, text="大学英语一", command=lambda: select_grade("english", 2)
        ).grid(row=1, column=1)
        btn3 = Button(
            win_selectall,
            text="程序设计基础一",
            command=lambda: select_grade("software", 3),
        ).grid(row=1, column=2)
        win_selectall.mainloop()

    lblTip = Label(win_admin, text="欢迎您，管理员%s" % adminID)
    btnSelectOne = Button(win_admin, text="查询学生成绩", command=SelectGradeUI)
    btnSelectAll = Button(win_admin, text="查看成绩分布", command=Select_course)
    btnUpdateOne = Button(win_admin, text="修改学生成绩", command=UpdateOne)
    btnUpdatePw = Button(win_admin, text="修改登陆密码", command=ChangePasswordUI)
    btnDelete = Button(win_admin, text="删除学生成绩", command=DeleteGradeUI)
    btnInsert = Button(win_admin, text="增加学生成绩", command=InsertGradeUI)

    lblTip.grid(row=0, column=0, columnspan=2, pady=5)
    btnInsert.grid(row=1, column=0, padx=5, pady=5)
    btnDelete.grid(row=1, column=1, padx=5, pady=5)
    btnSelectOne.grid(row=2, column=0, padx=5, pady=5)
    btnSelectAll.grid(row=2, column=1, padx=5, pady=5)
    btnUpdateOne.grid(row=3, column=0, padx=5, pady=5)
    btnUpdatePw.grid(row=3, column=1, padx=5, pady=5)
    win_admin.mainloop()
