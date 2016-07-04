#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import MySQLdb
import tkMessageBox

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Student():
    flag = 'index' 
    User = ''
    def __init__(self):
        self.db = MySQLdb.connect(host = 'localhost', user = 'zeng', passwd = '8963708', db = 'student', charset = 'utf8')
        self.cursor = self.db.cursor()
        self.student_root = Tk()
        self.student_root.geometry('1000x600')

        ################添加列表##################
        self.MainMenu = Menu(self.student_root, borderwidth = 1, font = ('黑体', 10, 'bold'))
        #修改
        self.modify = Menu(self.MainMenu, tearoff = 0)
        self.modify.add_command(label = '      密码', command = self.modify_Passwd)
        self.modify.add_command(label = '      个人信息', command = self.modify_Student)

        #查询
        self.select = Menu(self.MainMenu, tearoff = 0)
        self.select.add_command(label = '      成 绩', command = self.select_Student_OptionCourse)
        self.select.add_command(label = '      课程表', command = self.select_Course)

        #选课
        self.optionCourse = Menu(self.MainMenu, tearoff = 0)
        self.optionCourse.add_command(label = '      课 程', command = self.option_Course)
        
        #为MainMenu添加下拉菜单
        self.MainMenu.add_cascade(label = '           修 改           ', menu = self.modify)
        self.MainMenu.add_cascade(label = '           查 询           ', menu = self.select)
        self.MainMenu.add_cascade(label = '           选 课           ', menu = self.optionCourse)
        #注销
        self.MainMenu.add_command(label = '           注 销           ', command = self.logout)

        self.student_root['menu'] = self.MainMenu

        ############### 添加控件 ##################

        #默认界面
        if Student.flag == 'index':
            sql = "select * from Student where 学号 ='%s'"%Student.User
            count = self.cursor.execute(sql)
            if count > 0:
                result = self.cursor.fetchone()
                name = str(result[1])
                self.index_lb = Label(self.student_root, text = '%s 欢迎使用教学管理系统'%name,font = ('黑体','20','bold')).place(x = 350, y = 200)


        ### 修改模块界面 ###
        #修改个人信息界面
        elif Student.flag == 'modify_Student':
            Label(self.student_root, text = "修改个人信息:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.student_root, text = "姓名:").place(x = 200, y = 100)
            Label(self.student_root, text = "性别:").place(x = 540, y = 100)
            Label(self.student_root, text = "贯籍:").place(x = 200, y = 170)
            self.StudentNAME = Entry(self.student_root, width = 20)
            self.StudentNAME.place(x = 250, y =100)
            self.StudentSEX = Entry(self.student_root, width = 20)
            self.StudentSEX.place(x = 600, y = 100)
            self.StudentLOCAL = Entry(self.student_root, width = 20)
            self.StudentLOCAL.place(x = 250, y = 170)
            Button(self.student_root, text = "确定", width = 8, command = self.modify_Student_Sure).place(x = 700, y = 250)            

        #修改密码界面
        elif Student.flag == 'modify_Passwd':
            Label(self.student_root, text = "修改密码:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.student_root, text = '原密码:').place(x = 350, y = 100)
            self.OldPasswd = Entry(self.student_root, width = 20)
            self.OldPasswd.place(x = 410, y = 100)
            self.OldPasswd['show'] = '*'
            
            Label(self.student_root, text = '新密码:').place(x = 350, y = 150)
            self.NewPasswd1 = Entry(self.student_root, width = 20)
            self.NewPasswd1.place(x = 410, y = 150)
            self.NewPasswd1['show'] = '*'
            
            Label(self.student_root, text = '重新输入:').place(x = 350, y = 200)
            self.NewPasswd2 = Entry(self.student_root, width = 20)
            self.NewPasswd2.place(x = 410, y = 200)
            self.NewPasswd2['show'] = '*'

            Button(self.student_root, text = '确定',width = 8,command = self.modify_Passwd_Sure).place(x = 600, y = 250)
        

        ###查询模块界面 ###
        #查询成绩界面
        elif Student.flag == 'select_Student_OptionCourse':
            Label(self.student_root, text = "查询成绩:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.student_root, text = '%-*s%-*s'%(80,'  科  目',80,'成  绩')).place(x = 5, y = 35)
	    self.SelectScorse = Listbox(self.student_root, height = 29, width = 135)
            self.sl = Scrollbar(self.student_root)
            self.sl.place(x = 954, y =60, height = 525, width = 20)
            self.SelectScorse['yscrollcommand'] = self.sl.set
	    self.SelectScorse.place(x = 5, y = 60)
            self.sl['command'] = self.SelectScorse.yview
            sql = "select 名称, 成绩 from Course, OptionCourse where 学号='%s' and Course.课程号=OptionCourse.课程号"%Student.User
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s'%(70,i[0],10,i[1])
                    self.SelectScorse.insert(END, fm)
        
        #查询课程界面
        elif Student.flag == 'select_Course':
            Label(self.student_root, text = "查询课程:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.student_root, text = '%-*s%-*s%-*s%-*s%-*s'%(70,'  科  目',30,'老 师',30,'地点',60,'上课周',60,'时 间')).place(x = 5, y = 35)
	    self.SelectCourse = Listbox(self.student_root, height = 29, width = 135)
            self.sl1 = Scrollbar(self.student_root)
            self.sl1.place(x = 954, y =60, height = 525, width = 20)
            self.SelectCourse['yscrollcommand'] = self.sl1.set
	    self.SelectCourse.place(x = 5, y = 60)
            self.sl1['command'] = self.SelectCourse.yview
            sql = "select 名称,姓名,地点,起始周,结束周,上课时间,下课时间 from Course, OptionCourse,Teacher where 学号='%s' and Course.课程号=OptionCourse.课程号 and 任课老师=职工号"%Student.User
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s'%(60,i[0],23,i[1],27,i[2],50,'%s - %s'%(i[3],i[4]),50,'%s - %s'%(i[5],i[6]))
                    self.SelectCourse.insert(END, fm)

        ###选课模块界面###
        #选课
        elif Student.flag == 'option_Course':
            Label(self.student_root, text = "选课:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.student_root, text = '%-*s%-*s%-*s%-*s%-*s%-*s'%(20,'课程号',40,'  科  目',30,'老 师',30,'地点',60,'上课周',60,'时 间')).place(x = 5, y = 35)
	    self.OptionCourseLB = Listbox(self.student_root,selectmode = MULTIPLE, height = 29, width = 105)
            self.sl2 = Scrollbar(self.student_root)
            self.sl2.place(x = 744, y =60, height = 525, width = 20)
            self.OptionCourseLB['yscrollcommand'] = self.sl2.set
	    self.OptionCourseLB.place(x = 5, y = 60)
            self.sl2['command'] = self.OptionCourseLB.yview
            sql = "select 课程号,名称,姓名,地点,起始周,结束周,上课时间,下课时间 from Course,Teacher where 任课老师=职工号 and Course.课程号 NOT IN (select OptionCourse.课程号 from OptionCourse where 学号='%s')"%Student.User
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s'%(15,i[0],30,i[1],23,i[2],27,i[3],50,'%s - %s'%(i[4],i[5]),50,'%s - %s'%(i[6],i[7]))
                    self.OptionCourseLB.insert(END, fm)

            Button(self.student_root, text = '确定',width = 8,command = self.Option_Student_Sure).place(x = 780, y = 400)
            Button(self.student_root, text = '取消',width = 8,command = self.Cancel_Student_Sure).place(x = 900, y = 400)

    ################ 响应函数模块 ###################

    
    #修改模块响应函数
    def modify_Passwd_Sure(self):
        sql = "select * from Stu_Passwd where 学号 ='%s'"%Student.User
        count = self.cursor.execute(sql)
        if count > 0:
            result = self.cursor.fetchone()
            passwd = str(result[1])
            if passwd != self.OldPasswd.get():
                tkMessageBox.showinfo('Message','原密码错误')
            elif self.NewPasswd1.get() != self.NewPasswd2.get():
                tkMessageBox.showinfo('Message', '两次密码不一致')
            else:
                sql = "update Stu_Passwd set  密码='%s' where 学号 ='%s'"%(self.NewPasswd1.get(),Student.User)
                self.cursor.execute(sql)
                self.db.commit()
                self.OldPasswd.delete(0, 20)
                self.NewPasswd1.delete(0, 20)
                self.NewPasswd2.delete(0, 20)
                tkMessageBox.showinfo('Message', '修改成功')
        else:
            tkMessageBox.showinfo('Message','passwd error')


    def modify_Passwd(self):
        if Student.flag == 'modify_Passwd':
            return
        Student.flag = 'modify_Passwd'
        Student()
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()

    def modify_Student(self):
        if Student.flag == 'modify_Student':
            return
        Student.flag = 'modify_Student'
        Student()
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()

    def modify_Student_Sure(self):
        sql = "update Student set  姓名='%s',性别='%s',贯籍='%s' where 学号 ='%s'"%(self.StudentNAME.get(), self.StudentSEX.get(), self.StudentLOCAL.get(),Student.User)
        count = self.cursor.execute(sql)
        self.db.commit()
        if count > 0:
            self.StudentNAME.delete(0, 20)
            self.StudentSEX.delete(0, 20)
            self.StudentLOCAL.delete(0, 20)
            tkMessageBox.showinfo("Message", "修改成功！")
        else:
            self.StudentNAME.delete(0, 20)
            self.StudentSEX.delete(0, 20)
            self.StudentLOCAL.delete(0, 20)
            tkMessageBox.showinfo("error", "修改失败！")


    #查询模块响应函数
    def select_Student_OptionCourse(self):
        if Student.flag == 'select_Student_OptionCourse':
            return
        Student.flag = 'select_Student_OptionCourse'
        Student()
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()

    def select_Course(self):
        if Student.flag == 'select_Course':
            return
        Student.flag = 'select_Course'
        Student()
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()

    #选课模块响应函数
    def option_Course(self):
        if Student.flag == 'option_Course':
            return
        Student.flag = 'option_Course'
        Student()
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()

    def Option_Student_Sure(self):
        for item in self.OptionCourseLB.curselection():
            course = self.OptionCourseLB.get(item)[0:5]
            sql = "select * from OptionCourse where 课程号 = '%s' and 学号='%s'"%(course,Student.User)
            count = self.cursor.execute(sql)
            if count > 0:
                tkMessageBox.showinfo("Message", "已选修该课程！")
            else:
                sql = "insert into OptionCourse(学号, 课程号) values('%s','%s')"%(Student.User,course)
                count = self.cursor.execute(sql)
                self.db.commit()
                if count > 0:
                    tkMessageBox.showinfo("Message", "选课成功！")
                    self.OptionCourseLB.delete(item,item)
                else:
                    tkMessageBox.showinfo("Message", "选课失败！")

    def Cancel_Student_Sure(self):
        self.OptionCourseLB.selection_clear(0,END)


    #注销
    def logout(self):
        self.cursor.close()
        self.db.close()
        self.student_root.destroy()
        import Educational_System.login
        Educational_System.login.Login()


if __name__=='__main__':
    student = Student()
    student.student_root.mainloop()
