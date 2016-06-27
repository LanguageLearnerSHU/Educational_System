#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *

class Teacher():
    flag = 'index' 
    def __init__(self):
        self.teacher_root = Tk()
        self.teacher_root.geometry('1000x600')

        ################添加列表##################
        self.MainMenu = Menu(self.teacher_root, borderwidth = 1, font = ('黑体', 10, 'bold'))
        #插入
        self.add = Menu(self.MainMenu, tearoff = 0)
        self.add.add_command(label = '      学生成绩  ', command = self.add_Student)

        #删除
        self.delete = Menu(self.MainMenu, tearoff = 0)
        self.delete.add_command(label = '      学生成绩', command = self.delete_Student)
        
        #修改
        self.modify = Menu(self.MainMenu, tearoff = 0)
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
        self.MainMenu.add_cascade(label = '           删 除           ', menu = self.delete)
        self.MainMenu.add_cascade(label = '           修 改           ', menu = self.modify)
        self.MainMenu.add_cascade(label = '           查 询           ', menu = self.select)
        #注销
        self.MainMenu.add_command(label = '           注 销           ', command = self.logout)

        self.teacher_root['menu'] = self.MainMenu

        ############### 添加控件 ##################

        #默认界面
        if Teacher.flag == 'index':
            self.index_lb = Label(self.teacher_root, text = '欢迎使用教学管理系统',font = ('黑体','20','bold')).place(x = 350, y = 200)


        ### 插入模块界面 ###
        #插入学生成绩界面
        elif Teacher.flag == 'add_Student':
            self.add_lb = Label(self.teacher_root, text = '添加学生').place(x = 100, y = 100)


        ### 删除模块界面 ###
        #删除学生成绩界面


        ### 修改模块界面 ###
        #修改学生成绩界面
        
        #修改密码界面
        

        ###查询模块界面 ###
        #查询学生成绩界面
        
        #查询所教课程界面


    ################ 响应函数模块 ###################

    #添加模块响应函数
    
    def add_Student(self):
        if Teacher.flag == 'add_Student':
            return
        Teacher.flag = 'add_Student'
        Teacher()
        self.teacher_root.destroy()



    #删除模块响应函数
    def delete_Student(self):
        if Teacher.flag == 'delete_Student':
            return
        Teacher.flag = 'delete_Student'
        Teacher()
        self.teacher_root.destroy()


    #修改模块响应函数
    def modify_Passwd(self):
        if Teacher.flag == 'modify_Passwd':
            return
        Teacher.flag = 'modify_Passwd'
        Teacher()
        self.teacher_root.destroy()

    def modify_Student(self):
        if Teacher.flag == 'modify_Student':
            return
        Teacher.flag = 'modify_Student'
        Teacher()
        self.teacher_root.destroy()

    #查询模块响应函数
    def select_Student(self):
        if Teacher.flag == 'select_Student':
            return
        Teacher.flag = 'select_Student'
        Teacher()
        self.teacher_root.destroy()

    def select_Course(self):
        if Teacher.flag == 'select_Course':
            return
        Teacher.flag = 'select_Course'
        Teacher()
        self.teacher_root.destroy()


    #注销
    def logout(self):
        self.teacher_root.destroy()
        import Educational_System.login
        Educational_System.login.Login()


if __name__=='__main__':
    teacher = Teacher()
    teacher.teacher_root.mainloop()
