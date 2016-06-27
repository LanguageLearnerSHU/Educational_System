#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *

class Admin():
    flag = 'index' 
    def __init__(self):
        self.admin_root = Tk()
        self.admin_root.geometry('1000x600')

        ################添加列表##################
        self.MainMenu = Menu(self.admin_root, borderwidth = 1, font = ('黑体', 10, 'bold'))
        #添加
        self.add = Menu(self.MainMenu, tearoff = 0)
        self.add.add_command(label = '      管理员  ', command = self.add_Admin)
        self.add.add_command(label = '      教师  ', command = self.add_Teacher)
        self.add.add_command(label = '      学生  ', command = self.add_Student)
        self.add.add_command(label = '      课程  ', command = self.add_Course)
        self.add.add_command(label = '      学院  ', command = self.add_College)
        self.add.add_command(label = '      专业  ', command = self.add_Major)

        #删除
        self.delete = Menu(self.MainMenu, tearoff = 0)
        self.delete.add_command(label = '      管理员', command = self.delete_Admin)
        self.delete.add_command(label = '      教师', command = self.delete_Teacher)
        self.delete.add_command(label = '      学生', command = self.delete_Student)
        
        #修改
        self.modify = Menu(self.MainMenu, tearoff = 0)
        self.modify.add_command(label = '      密码', command = self.modify_Passwd)
        self.modify.add_command(label = '      教师信息', command = self.modify_Teacher)
        self.modify.add_command(label = '      学生信息', command = self.modify_Student)

        #查询
        self.select = Menu(self.MainMenu, tearoff = 0)
        self.select.add_command(label = '      管理员', command = self.select_Admin)
        self.select.add_command(label = '      教师', command = self.select_Teacher)
        self.select.add_command(label = '      学生', command = self.select_Student)
        self.select.add_command(label = '      课程', command = self.select_Course)
        #self.select.add_command(label = '', command = self.select_)
        #self.select.add_command(label = '', command = self.select_)
        #self.select.add_command(label = '', command = self.select_)

        
        #为MainMenu添加下拉菜单
        self.MainMenu.add_cascade(label = '           添 加           ', menu = self.add)
        self.MainMenu.add_cascade(label = '           删 除           ', menu = self.delete)
        self.MainMenu.add_cascade(label = '           修 改           ', menu = self.modify)
        self.MainMenu.add_cascade(label = '           查 询           ', menu = self.select)
        #注销
        self.MainMenu.add_command(label = '           注 销           ', command = self.logout)

        self.admin_root['menu'] = self.MainMenu

        ############### 添加控件 ##################

        #默认界面
        if Admin.flag == 'index':
            self.index_lb = Label(self.admin_root, text = '欢迎使用教学管理系统',font = ('黑体','20','bold')).place(x = 350, y = 200)


        ### 添加模块界面 ###
        #添加管理员界面
        elif Admin.flag == 'add_Admin':
            self.add_lb = Label(self.admin_root, text = '添加管理员').place(x = 100, y = 100)

        #添加教师界面
        elif Admin.flag == 'add_Teacher':
            self.add_lb = Label(self.admin_root, text = '添加教师').place(x = 100, y = 100)


        #添加学生界面
        elif Admin.flag == 'add_Student':
            self.add_lb = Label(self.admin_root, text = '添加学生').place(x = 100, y = 100)

        #添加课程界面
        elif Admin.flag == 'add_Course':
            self.add_lb = Label(self.admin_root, text = '添加课程').place(x = 100, y = 100)

        #添加学院界面
        elif Admin.flag == 'add_College':
            self.add_lb = Label(self.admin_root, text = '添加学院').place(x = 100, y = 100)

        #添加专业界面
        elif Admin.flag == 'add_Major':
            self.add_lb = Label(self.admin_root, text = '添加专业').place(x = 100, y = 100)

        ### 删除模块界面 ###
        #删除管理员界面

        #删除教师界面

        #删除学生界面


        ### 修改模块界面 ###
        #修改教师信息界面
        
        #修改学生信息界面
        
        #修改密码界面
        

        ###查询模块界面 ###
        #查询管理员界面
        
        #查询教师界面
        
        #查询学生界面
        
        #查询课程界面


    ################ 响应函数模块 ###################

    #添加模块响应函数
    def add_Admin(self):
        if Admin.flag == 'add_Admin':
            return 
        Admin.flag = 'add_Admin'
        Admin()
        self.admin_root.destroy()

    
    def add_Course(self):
        if Admin.flag == 'add_Course':
            return
        Admin.flag = 'add_Course'
        Admin()
        self.admin_root.destroy()


    def add_Teacher(self):
        if Admin.flag == 'add_Teacher':
            return
        Admin.flag = 'add_Teacher'
        Admin()
        self.admin_root.destroy()

    def add_Student(self):
        if Admin.flag == 'add_Student':
            return
        Admin.flag = 'add_Student'
        Admin()
        self.admin_root.destroy()

    def add_College(self):
        if Admin.flag == 'add_College':
            return
        Admin.flag = 'add_College'
        Admin()
        self.admin_root.destroy()

    def add_Major(self):
        if Admin.flag == 'add_Major':
            return
        Admin.flag = 'add_Major'
        Admin()
        self.admin_root.destroy()


    #删除模块响应函数
    def delete_Admin(self):
        if Admin.flag == 'delete_Admin':
            return
        Admin.flag = 'delete_Admin'
        Admin()
        self.admin_root.destroy()

    def delete_Teacher(self):
        if Admin.flag == 'delete_Teacher':
            return
        Admin.flag = 'delete_Teacher'
        Admin()
        self.admin_root.destroy()

    def delete_Student(self):
        if Admin.flag == 'delete_Student':
            return
        Admin.flag = 'delete_Student'
        Admin()
        self.admin_root.destroy()


    #修改模块响应函数
    def modify_Passwd(self):
        if Admin.flag == 'modify_Passwd':
            return
        Admin.flag = 'modify_Passwd'
        Admin()
        self.admin_root.destroy()

    def modify_Teacher(self):
        if Admin.flag == 'modify_Teacher':
            return
        Admin.flag = 'modify_Teacher'
        Admin()
        self.admin_root.destroy()

    def modify_Student(self):
        if Admin.flag == 'modify_Student':
            return
        Admin.flag = 'modify_Student'
        Admin()
        self.admin_root.destroy()

    #查询模块响应函数
    def select_Admin(self):
        if Admin.flag == 'select_Admin':
            return
        Admin.flag = 'select_Admin'
        Admin()
        self.admin_root.destroy()

    def select_Teacher(self):
        if Admin.flag == 'select_Teacher':
            return
        Admin.flag = 'select_Teacher'
        Admin()
        self.admin_root.destroy()

    def select_Student(self):
        if Admin.flag == 'select_Student':
            return
        Admin.flag = 'select_Student'
        Admin()
        self.admin_root.destroy()

    def select_Course(self):
        if Admin.flag == 'select_Course':
            return
        Admin.flag = 'select_Course'
        Admin()
        self.admin_root.destroy()


    #注销
    def logout(self):
        self.admin_root.destroy()
        import Educational_System.login
        Educational_System.login.Login()


if __name__=='__main__':
    administrator = Admin()
    administrator.admin_root.mainloop()
