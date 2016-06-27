#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import MySQLdb
import tkMessageBox

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
        self.select.add_command(label = '      课 程', command = self.select_Course)

        
        #为MainMenu添加下拉菜单
        self.MainMenu.add_cascade(label = '           修 改           ', menu = self.modify)
        self.MainMenu.add_cascade(label = '           查 询           ', menu = self.select)
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
        
        #修改密码界面
        if Student.flag == 'modify_Passwd':
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
        
        #查询课程界面


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
                return 
            elif self.NewPasswd1.get() != self.NewPasswd2.get():
                tkMessageBox.showinfo('Message', '两次密码不一致')
                return
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
            return 



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
