#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import MySQLdb
import tkMessageBox

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Teacher():
    flag = 'index' 
    User = ''
    def __init__(self):
        self.db = MySQLdb.connect(host = 'localhost', user = 'zeng', passwd = '8963708', db = 'student', charset = 'utf8')
        self.cursor = self.db.cursor()
        self.teacher_root = Tk()
        self.teacher_root.geometry('1000x600')

        ################添加列表##################
        self.MainMenu = Menu(self.teacher_root, borderwidth = 1, font = ('黑体', 10, 'bold'))
        #插入
        self.add = Menu(self.MainMenu, tearoff = 0)
        self.add.add_command(label = '      学生成绩  ', command = self.add_Student)

        #删除
        #self.delete = Menu(self.MainMenu, tearoff = 0)
        #self.delete.add_command(label = '      学生成绩', command = self.delete_Student)
        
        #修改
        self.modify = Menu(self.MainMenu, tearoff = 0)
        self.modify.add_command(label = '      个人信息', command = self.modify_Teacher)
        self.modify.add_command(label = '      密码', command = self.modify_Passwd)
        self.modify.add_command(label = '      学生成绩', command = self.modify_Student)

        #查询
        self.select = Menu(self.MainMenu, tearoff = 0)
        self.select.add_command(label = '      学生成绩', command = self.select_Student)
        self.select.add_command(label = '      所教课程', command = self.select_Course)
        #self.select.add_command(label = '', command = self.select_)
        #self.select.add_command(label = '', command = self.select_)
        #self.select.add_command(label = '', command = self.select_)

        
        #为MainMenu添加下拉菜单
        self.MainMenu.add_cascade(label = '           插 入           ', menu = self.add)
        #self.MainMenu.add_cascade(label = '           删 除           ', menu = self.delete)
        self.MainMenu.add_cascade(label = '           修 改           ', menu = self.modify)
        self.MainMenu.add_cascade(label = '           查 询           ', menu = self.select)
        #注销
        self.MainMenu.add_command(label = '           注 销           ', command = self.logout)

        self.teacher_root['menu'] = self.MainMenu

        ############### 添加控件 ##################

        #默认界面
        if Teacher.flag == 'index':
            #self.index_lb = Label(self.teacher_root, text = '%s 欢迎使用教学管理系统'%Teacher.User,font = ('黑体','20','bold')).place(x = 350, y = 200)
            sql = "select * from Teacher where 职工号 ='%s'"%Teacher.User
            count = self.cursor.execute(sql)
            if count > 0:
                result = self.cursor.fetchone()
                name = str(result[1].encode('utf-8'))
                self.index_lb = Label(self.teacher_root, text = '%s您好，欢迎使用教学管理系统'%name,font = ('黑体','20','bold')).place(x = 350, y = 200)


        ### 插入模块界面 ###
        #插入学生成绩界面
        elif Teacher.flag == 'add_Student':
            Label(self.teacher_root, text = "插入学生成绩:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.teacher_root, text = "学号:").place(x = 400, y = 150)
            Label(self.teacher_root, text = "成绩:").place(x = 400, y = 220)
            self.IndexStudentID = Entry(self.teacher_root, width = 20)
            self.IndexStudentID.place(x = 450, y = 150)
            self.IndexStudentSCORE = Entry(self.teacher_root, width = 20)
            self.IndexStudentSCORE.place(x = 450, y = 220)
            Button(self.teacher_root, text = "确定", width = 8, command = self.add_Student_Sure).place(x = 700, y = 300)


        ### 删除模块界面 ###
        #删除学生成绩界面
        #elif Teacher.flag == 'delete_Student':
            #Label(self.teacher_root, text = "删除学生成绩:",font = ('黑体','12','bold')).place(x = 10, y = 10)


        ### 修改模块界面 ###
        #修改学生成绩界面
        elif Teacher.flag == 'modify_Student':
            Label(self.teacher_root, text = "修改学生成绩:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.teacher_root, text = "学号:").place(x = 400, y = 150)
            Label(self.teacher_root, text = "成绩:").place(x = 400, y = 220)
            self.ModifyStudentID = Entry(self.teacher_root, width = 20)
            self.ModifyStudentID.place(x = 450, y = 150)
            self.ModifyStudentSCORE = Entry(self.teacher_root, width = 20)
            self.ModifyStudentSCORE.place(x = 450, y = 220)
            Button(self.teacher_root, text = "确定", width = 8, command = self.modify_Student_Sure).place(x = 700, y = 300)
        
        #修改个人信息界面
        elif Teacher.flag == 'modify_Teacher':
            Label(self.teacher_root, text = "修改个人信息:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.teacher_root, text = "姓名:").place(x = 200, y = 100)
            Label(self.teacher_root, text = "性别:").place(x = 540, y = 100)
            Label(self.teacher_root, text = "任课:").place(x = 200, y = 170)
            Label(self.teacher_root, text = "电话:").place(x = 540, y = 170)
            self.TeacherNAME = Entry(self.teacher_root, width = 20)
            self.TeacherNAME.place(x = 250, y =100)
            self.TeacherSEX = Entry(self.teacher_root, width = 20)
            self.TeacherSEX.place(x = 600, y = 100)
            self.TeacherCOURSE = Entry(self.teacher_root, width = 20)
            self.TeacherCOURSE.place(x = 250, y = 170)
            self.TeacherPHONE = Entry(self.teacher_root, width = 20)
            self.TeacherPHONE.place(x = 600, y = 170)
            Button(self.teacher_root, text = "确定", width = 8, command = self.modify_Teacher_Sure).place(x = 700, y = 250)

        #修改密码界面
        elif Teacher.flag == 'modify_Passwd':
            Label(self.teacher_root, text = "修改密码:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.teacher_root, text = '原密码:').place(x = 350, y = 100)
            self.OldPasswd = Entry(self.teacher_root, width = 20)
            self.OldPasswd.place(x = 410, y = 100)
            self.OldPasswd['show'] = '*'
            
            Label(self.teacher_root, text = '新密码:').place(x = 350, y = 150)
            self.NewPasswd1 = Entry(self.teacher_root, width = 20)
            self.NewPasswd1.place(x = 410, y = 150)
            self.NewPasswd1['show'] = '*'
            
            Label(self.teacher_root, text = '重新输入:').place(x = 350, y = 200)
            self.NewPasswd2 = Entry(self.teacher_root, width = 20)
            self.NewPasswd2.place(x = 410, y = 200)
            self.NewPasswd2['show'] = '*'

            Button(self.teacher_root, text = '确定',width = 8,command = self.modify_Passwd_Sure).place(x = 600, y = 250)
        

        ###查询模块界面 ###
        #查询学生成绩界面
        elif Teacher.flag == 'select_Student':
            Label(self.teacher_root, text = "查询学生成绩:",font = ('黑体','12','bold')).place(x = 10, y = 10)

        #查询所教课程界面
        elif Teacher.flag == 'select_Course':
            Label(self.teacher_root, text = "查询所教课程:",font = ('黑体','12','bold')).place(x = 10, y = 10)


    ################ 响应函数模块 ###################

    #插入模块响应函数
    
    def add_Student(self):
        if Teacher.flag == 'add_Student':
            return
        Teacher.flag = 'add_Student'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()

    def add_Student_Sure(self):
        sql = "select 任课 from Teacher where 职工号='%s'"%Teacher.User
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        #name = str(result[1].encode('utf-8'))
        course = result[0]
        #print course
        sql = "select * from OptionCourse where 学号='%s' and 课程号='%s'"%(self.IndexStudentID.get(), course)
        count = self.cursor.execute(sql)
        self.db.commit()
        if count > 0:
            sql = "update OptionCourse set 成绩 = '%s' where 学号='%s' and 课程号='%s'"%(self.IndexStudentSCORE.get(),self.IndexStudentID.get(), course)
            count1 = self.cursor.execute(sql)
            self.db.commit()
            if count1 >0:
                self.IndexStudentID.delete(0, 20)
                self.IndexStudentSCORE.delete(0, 20)
                tkMessageBox.showinfo("Message", "插入成功！")
            else:
                self.IndexStudentID.delete(0, 20)
                self.IndexStudentSCORE.delete(0, 20)
                tkMessageBox.showinfo("Message", "插入失败！")
        else:
            self.IndexStudentID.delete(0, 20)
            self.IndexStudentSCORE.delete(0, 20)
            tkMessageBox.showinfo("error", "该学生无选修该课程！")


    #删除模块响应函数
    #def delete_Student(self):
        #if Teacher.flag == 'delete_Student':
            #return
        #Teacher.flag = 'delete_Student'
        #Teacher()
        #self.cursor.close()
        #self.db.close()
        #self.teacher_root.destroy()


    #修改模块响应函数
    def modify_Passwd(self):
        if Teacher.flag == 'modify_Passwd':
            return
        Teacher.flag = 'modify_Passwd'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()

    def modify_Teacher(self):
        if Teacher.flag == 'modify_Teacher':
            return
        Teacher.flag = 'modify_Teacher'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()


    def modify_Teacher_Sure(self):
        sql = "update Teacher set  姓名='%s',性别='%s',任课='%s',电话='%s' where 职工号 ='%s'"%(self.TeacherNAME.get(), self.TeacherSEX.get(), self.TeacherCOURSE.get(), self.TeacherPHONE.get(),Teacher.User)
        count = self.cursor.execute(sql)
        self.db.commit()
        if count > 0:
            self.TeacherNAME.delete(0, 20)
            self.TeacherSEX.delete(0, 20)
            self.TeacherPHONE.delete(0, 20)
            self.TeacherCOURSE.delete(0, 20)
            tkMessageBox.showinfo("Message", "修改成功！")
        else:
            self.TeacherNAME.delete(0, 20)
            self.TeacherSEX.delete(0, 20)
            self.TeacherPHONE.delete(0, 20)
            self.TeacherCOURSE.delete(0, 20)
            tkMessageBox.showinfo("error", "修改失败！")
 

    def modify_Passwd_Sure(self):
        sql = "select * from Tea_Passwd where 职工号 ='%s'"%Teacher.User
        count = self.cursor.execute(sql)
        if count > 0:
            result = self.cursor.fetchone()
            passwd = str(result[1])
            if passwd != self.OldPasswd.get():
                tkMessageBox.showinfo('Message','原密码错误')
            elif self.NewPasswd1.get() != self.NewPasswd2.get():
                tkMessageBox.showinfo('Message', '两次密码不一致')
            else:
                sql = "update Tea_Passwd set  密码='%s' where 职工号 ='%s'"%(self.NewPasswd1.get(),Teacher.User)
                self.cursor.execute(sql)
                self.db.commit()
                self.OldPasswd.delete(0, 20)
                self.NewPasswd1.delete(0, 20)
                self.NewPasswd2.delete(0, 20)
                tkMessageBox.showinfo('Message', '修改成功')
        else:
            tkMessageBox.showinfo('Message','passwd error')


    def modify_Student(self):
        if Teacher.flag == 'modify_Student':
            return
        Teacher.flag = 'modify_Student'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()

    def modify_Student_Sure(self):
        sql = "select 任课 from Teacher where 职工号='%s'"%Teacher.User
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        #name = str(result[1].encode('utf-8'))
        course = result[0]
        #print course
        sql = "select * from OptionCourse where 学号='%s' and 课程号='%s'"%(self.ModifyStudentID.get(), course)
        count = self.cursor.execute(sql)
        self.db.commit()
        if count > 0:
            sql = "update OptionCourse set 成绩 = '%s' where 学号='%s' and 课程号='%s'"%(self.ModifyStudentSCORE.get(),self.ModifyStudentID.get(), course)
            count1 = self.cursor.execute(sql)
            self.db.commit()
            if count1 >0:
                self.ModifyStudentID.delete(0, 20)
                self.ModifyStudentSCORE.delete(0, 20)
                tkMessageBox.showinfo("Message", "修改成功！")
            else:
                self.ModifyStudentID.delete(0, 20)
                self.ModifyStudentSCORE.delete(0, 20)
                tkMessageBox.showinfo("Message", "修改失败！")
        else:
            self.ModifyStudentID.delete(0, 20)
            self.ModifyStudentSCORE.delete(0, 20)
            tkMessageBox.showinfo("error", "该学生无选修该课程！")


    #查询模块响应函数
    def select_Student(self):
        if Teacher.flag == 'select_Student':
            return
        Teacher.flag = 'select_Student'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()

    def select_Course(self):
        if Teacher.flag == 'select_Course':
            return
        Teacher.flag = 'select_Course'
        Teacher()
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()


    #注销
    def logout(self):
        self.cursor.close()
        self.db.close()
        self.teacher_root.destroy()
        import Educational_System.login
        Educational_System.login.Login()


if __name__=='__main__':
    teacher = Teacher()
    teacher.teacher_root.mainloop()
