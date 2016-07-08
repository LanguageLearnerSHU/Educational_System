#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import MySQLdb
import tkMessageBox

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Admin():
    flag = 'index'
    User = ''
    def __init__(self):
        self.db = MySQLdb.connect(host = 'localhost', user = 'zeng', passwd = '8963708', db = 'student', charset = 'utf8')
        self.cursor = self.db.cursor()
        self.admin_root = Tk()
        self.admin_root.geometry('1000x600')

        ################添加列表##################
        self.MainMenu = Menu(self.admin_root, borderwidth = 1, font = ('黑体', 10, 'bold'))
        #添加
        self.add = Menu(self.MainMenu, tearoff = 0)
        self.add.add_command(label = '      管理员  ', command = self.add_Admin)
        self.add.add_command(label = '      教 师  ', command = self.add_Teacher)
        self.add.add_command(label = '      学 生  ', command = self.add_Student)
        self.add.add_command(label = '      课 程  ', command = self.add_Course)
        self.add.add_command(label = '      学 院  ', command = self.add_College)
        self.add.add_command(label = '      专 业  ', command = self.add_Major)
        self.add.add_command(label = '      教研室  ', command = self.add_TeacherOffice)
        self.add.add_command(label = '      班 级  ', command = self.add_Class)

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
            self.index_lb = Label(self.admin_root, text = '%s 欢迎使用教学管理系统'%Admin.User,font = ('黑体','20','bold')).place(x = 350, y = 200)


        ### 添加模块界面 ###
        #添加管理员界面
        elif Admin.flag == 'add_Admin':
            Label(self.admin_root, text = "添加管理员:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            if Admin.User == 'root':
                Label(self.admin_root, text = "管理员:").place(x = 400, y = 100)
                Label(self.admin_root, text = "密码:").place(x = 400, y = 170)
                Label(self.admin_root, text = "确认:").place(x = 400, y = 240)
                self.NewAdmin = Entry(self.admin_root, width = 20)
                self.NewAdmin.place(x = 450, y = 100)
                self.NewAdminPasswd1 = Entry(self.admin_root, width = 20)
                self.NewAdminPasswd1.place(x = 450, y =170)
                self.NewAdminPasswd1['show'] = '*'
                self.NewAdminPasswd2 = Entry(self.admin_root, width = 20)
                self.NewAdminPasswd2.place(x = 450, y = 240)
                self.NewAdminPasswd2['show'] = '*'
                Button(self.admin_root, text = "确定", width = 8, command = self.add_Admin_Sure).place(x = 700, y = 350)
            else:
                tkMessageBox.showinfo("Warnning", "你无权限添加管理员！")

        #添加教师界面
        elif Admin.flag == 'add_Teacher':
            Label(self.admin_root, text = "添加教师:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "职工号:").place(x = 190, y = 100)
            Label(self.admin_root, text = "姓名:").place(x = 530, y = 100)
            Label(self.admin_root, text = "性别:").place(x = 190, y = 170)
            Label(self.admin_root, text = "教研室代码:").place(x = 530, y = 170)
            Label(self.admin_root, text = "任课代码:").place(x = 190, y = 240)
            Label(self.admin_root, text = "电话:").place(x = 530, y = 240)
            self.NewTeacherID = Entry(self.admin_root, width = 20)
            self.NewTeacherID.place(x = 250, y = 100)
            self.NewTeacherNAME = Entry(self.admin_root, width = 20)
            self.NewTeacherNAME.place(x = 600, y =100)
            self.NewTeacherSEX = Entry(self.admin_root, width = 20)
            self.NewTeacherSEX.place(x = 250, y = 170)
            self.NewTeacherOFFICE = Entry(self.admin_root, width = 20)
            self.NewTeacherOFFICE.place(x = 600, y = 170)
            self.NewTeacherCOURSE = Entry(self.admin_root, width = 20)
            self.NewTeacherCOURSE.place(x = 250, y = 240)
            self.NewTeacherPHONE = Entry(self.admin_root, width = 20)
            self.NewTeacherPHONE.place(x = 600, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_Teacher_Sure).place(x = 700, y = 350)


        #添加学生界面
        elif Admin.flag == 'add_Student':
            Label(self.admin_root, text = "添加学生:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "学号:").place(x = 400, y = 100)
            Label(self.admin_root, text = "姓名:").place(x = 400, y = 170)
            Label(self.admin_root, text = "专业代码:").place(x = 400, y = 240)
            Label(self.admin_root, text = "班级代码:").place(x = 400, y = 310)
            self.NewStudentID = Entry(self.admin_root, width = 20)
            self.NewStudentID.place(x = 450, y = 100)
            self.NewStudentNAME = Entry(self.admin_root, width = 20)
            self.NewStudentNAME.place(x = 450, y = 170)
            self.NewStudentMAJOR = Entry(self.admin_root, width = 20)
            self.NewStudentMAJOR.place(x = 450, y = 240)
            self.NewStudentCLASS = Entry(self.admin_root, width = 20)
            self.NewStudentCLASS.place(x = 450, y = 310)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_Student_Sure).place(x = 700, y = 400)

        #添加课程界面
        elif Admin.flag == 'add_Course':
            Label(self.admin_root, text = "添加课程:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "课程号:").place(x = 190, y = 100)
            Label(self.admin_root, text = "名称:").place(x = 530, y = 100)
            Label(self.admin_root, text = "任课职工号:").place(x = 190, y = 170)
            Label(self.admin_root, text = "地点:").place(x = 530, y = 170)
            Label(self.admin_root, text = "起始周:").place(x = 190, y = 240)
            Label(self.admin_root, text = "结束周:").place(x = 530, y = 240)
            Label(self.admin_root, text = "上课时间:").place(x = 190, y = 310)
            Label(self.admin_root, text = "下课时间:").place(x = 530, y = 310)

            self.NewCourseID = Entry(self.admin_root, width = 20)
            self.NewCourseID.place(x = 260, y = 100)
            self.NewCourseNAME = Entry(self.admin_root, width = 20)
            self.NewCourseNAME.place(x = 600, y =100)
            self.NewCourseTEACHER = Entry(self.admin_root, width = 20)
            self.NewCourseTEACHER.place(x = 260, y = 170)
            self.NewCourseLOCAL = Entry(self.admin_root, width = 20)
            self.NewCourseLOCAL.place(x = 600, y = 170)
            self.NewCourseBEGINWEEK = Entry(self.admin_root, width = 20)
            self.NewCourseBEGINWEEK.place(x = 260, y = 240)
            self.NewCourseENDWEEK = Entry(self.admin_root, width = 20)
            self.NewCourseENDWEEK.place(x = 600, y = 240)
            self.NewCourseBEGINTIME = Entry(self.admin_root, width = 20)
            self.NewCourseBEGINTIME.place(x = 260, y = 310)
            self.NewCourseENDTIME = Entry(self.admin_root, width = 20)
            self.NewCourseENDTIME.place(x = 600, y = 310)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_Course_Sure).place(x = 700, y = 400)

        #添加学院界面
        elif Admin.flag == 'add_College':
            Label(self.admin_root, text = "添加学院:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "学院代码:").place(x = 400, y = 100)
            Label(self.admin_root, text = "名 称:").place(x = 400, y = 170)
            Label(self.admin_root, text = "院长职工号:").place(x = 400, y = 240)
            self.NewCollegeID = Entry(self.admin_root, width = 20)
            self.NewCollegeID.place(x = 450, y = 100)
            self.NewCollegeNAME = Entry(self.admin_root, width = 20)
            self.NewCollegeNAME.place(x = 450, y = 170)
            self.NewCollegePRESIDENT = Entry(self.admin_root, width = 20)
            self.NewCollegePRESIDENT.place(x = 450, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_College_Sure).place(x = 700, y = 350)

        #添加专业界面
        elif Admin.flag == 'add_Major':
            Label(self.admin_root, text = "添加专业:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "专业代码:").place(x = 400, y = 100)
            Label(self.admin_root, text = "名 称:").place(x = 400, y = 170)
            Label(self.admin_root, text = "所在学院:").place(x = 400, y = 240)
            self.NewMajorID = Entry(self.admin_root, width = 20)
            self.NewMajorID.place(x = 450, y = 100)
            self.NewMajorNAME = Entry(self.admin_root, width = 20)
            self.NewMajorNAME.place(x = 450, y = 170)
            self.NewMajorCOLLEGE = Entry(self.admin_root, width = 20)
            self.NewMajorCOLLEGE.place(x = 450, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_Major_Sure).place(x = 700, y = 350)

        #添加教研室界面
        elif Admin.flag == 'add_TeacherOffice':
            Label(self.admin_root, text = "添加教研室:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "教研室代码:").place(x = 400, y = 100)
            Label(self.admin_root, text = "名 称:").place(x = 400, y = 170)
            Label(self.admin_root, text = "地 点:").place(x = 400, y = 240)
            Label(self.admin_root, text = "所在学院:").place(x = 400, y = 310)
            self.NewTeacherOfficeID = Entry(self.admin_root, width = 20)
            self.NewTeacherOfficeID.place(x = 450, y = 100)
            self.NewTeacherOfficeNAME = Entry(self.admin_root, width = 20)
            self.NewTeacherOfficeNAME.place(x = 450, y = 170)
            self.NewTeacherOfficeLOCAL = Entry(self.admin_root, width = 20)
            self.NewTeacherOfficeLOCAL.place(x = 450, y = 240)
            self.NewTeacherOfficeCOLLEGE = Entry(self.admin_root, width = 20)
            self.NewTeacherOfficeCOLLEGE.place(x = 450, y = 310)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_TeacherOffice_Sure).place(x = 700, y = 400)

        #添加班级界面 
        elif Admin.flag == 'add_Class':
            Label(self.admin_root, text = "添加班级:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "班级代码:").place(x = 190, y = 100)
            Label(self.admin_root, text = "年级:").place(x = 530, y = 100)
            Label(self.admin_root, text = "班级:").place(x = 190, y = 170)
            Label(self.admin_root, text = "专业代码:").place(x = 530, y = 170)
            Label(self.admin_root, text = "班主任:").place(x = 190, y = 240)
            Label(self.admin_root, text = "人数:").place(x = 530, y = 240)
            self.NewClassID = Entry(self.admin_root, width = 20)
            self.NewClassID.place(x = 250, y = 100)
            self.NewClassGRADE = Entry(self.admin_root, width = 20)
            self.NewClassGRADE.place(x = 600, y =100)
            self.NewClassCLASS = Entry(self.admin_root, width = 20)
            self.NewClassCLASS.place(x = 250, y = 170)
            self.NewClassMAJOR = Entry(self.admin_root, width = 20)
            self.NewClassMAJOR.place(x = 600, y = 170)
            self.NewClassHEADMASTER = Entry(self.admin_root, width = 20)
            self.NewClassHEADMASTER.place(x = 250, y = 240)
            self.NewClassNUMBER = Entry(self.admin_root, width = 20)
            self.NewClassNUMBER.place(x = 600, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.add_Class_Sure).place(x = 700, y = 350)

        ### 删除模块界面 ###
        #删除管理员界面
        elif Admin.flag == 'delete_Admin':
            Label(self.admin_root, text = "删除管理员:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            if Admin.User == 'root':
                Label(self.admin_root, text = "管理员:").place(x = 400, y = 200)
                self.DeleteAdmin = Entry(self.admin_root, width = 20)
                self.DeleteAdmin.place(x = 450, y = 200)
                Button(self.admin_root, text = "确定", width = 8, command = self.delete_Admin_Sure).place(x = 700, y = 350)
            else:
                tkMessageBox.showinfo("Warnning", "你无权限删除管理员！")

        #删除教师界面
        elif Admin.flag == 'delete_Teacher':
            Label(self.admin_root, text = "删除教师:",font = ('黑体','12','bold')).place(x = 10, y = 10)

        #删除学生界面
        elif Admin.flag == 'delete_Student':
            Label(self.admin_root, text = "删除学生:",font = ('黑体','12','bold')).place(x = 10, y = 10)

        ### 修改模块界面 ###
        #修改教师信息界面 
        elif Admin.flag == 'modify_Teacher':
            Label(self.admin_root, text = "修改教师信息:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "职工号:").place(x = 190, y = 100)
            Label(self.admin_root, text = "姓名:").place(x = 530, y = 100)
            Label(self.admin_root, text = "性别:").place(x = 190, y = 170)
            Label(self.admin_root, text = "教研室:").place(x = 530, y = 170)
            Label(self.admin_root, text = "任课:").place(x = 190, y = 240)
            Label(self.admin_root, text = "电话:").place(x = 530, y = 240)
            self.ModifyTeacherID = Entry(self.admin_root, width = 20)
            self.ModifyTeacherID.place(x = 250, y = 100)
            self.ModifyTeacherNAME = Entry(self.admin_root, width = 20)
            self.ModifyTeacherNAME.place(x = 600, y =100)
            self.ModifyTeacherSEX = Entry(self.admin_root, width = 20)
            self.ModifyTeacherSEX.place(x = 250, y = 170)
            self.ModifyTeacherOFFICE = Entry(self.admin_root, width = 20)
            self.ModifyTeacherOFFICE.place(x = 600, y = 170)
            self.ModifyTeacherCOURSE = Entry(self.admin_root, width = 20)
            self.ModifyTeacherCOURSE.place(x = 250, y = 240)
            self.ModifyTeacherPHONE = Entry(self.admin_root, width = 20)
            self.ModifyTeacherPHONE.place(x = 600, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.modify_Teacher_Sure).place(x = 700, y = 350)
 
        #修改学生信息界面 
        elif Admin.flag == 'modify_Student':
            Label(self.admin_root, text = "修改学生信息:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = "学号:").place(x = 430, y = 100)
            Label(self.admin_root, text = "专业代码:").place(x = 430, y = 170)
            Label(self.admin_root, text = "班级代码:").place(x = 430, y = 240)
            self.ModifyStudentID = Entry(self.admin_root, width = 20)
            self.ModifyStudentID.place(x = 500, y = 100)
            self.ModifyStudentMAJOR = Entry(self.admin_root, width = 20)
            self.ModifyStudentMAJOR.place(x = 500, y = 170)
            self.ModifyStudentCLASS = Entry(self.admin_root, width = 20)
            self.ModifyStudentCLASS.place(x = 500, y = 240)
            Button(self.admin_root, text = "确定", width = 8, command = self.modify_Student_Sure).place(x = 700, y = 350)
        
        #修改密码界面
        elif Admin.flag == 'modify_Passwd':
            Label(self.admin_root, text = "修改密码:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = '原密码:').place(x = 350, y = 100)
            self.OldPasswd = Entry(self.admin_root, width = 20)
            self.OldPasswd.place(x = 410, y = 100)
            self.OldPasswd['show'] = '*'
            
            Label(self.admin_root, text = '新密码:').place(x = 350, y = 150)
            self.NewPasswd1 = Entry(self.admin_root, width = 20)
            self.NewPasswd1.place(x = 410, y = 150)
            self.NewPasswd1['show'] = '*'
            
            Label(self.admin_root, text = '重新输入:').place(x = 350, y = 200)
            self.NewPasswd2 = Entry(self.admin_root, width = 20)
            self.NewPasswd2.place(x = 410, y = 200)
            self.NewPasswd2['show'] = '*'

            Button(self.admin_root, text = '确定',width = 8,command = self.modify_Passwd_Sure).place(x = 600, y = 250)
        

        ###查询模块界面 ###
        #查询管理员界面
        elif Admin.flag == 'select_Admin':
            Label(self.admin_root, text = "查询管理员:",font = ('黑体','12','bold')).place(x = 10, y = 10)
        
        #查询教师界面
        elif Admin.flag == 'select_Teacher':
            Label(self.admin_root, text = "查询教师:",font = ('黑体','12','bold')).place(x = 10, y = 10)
        
        #查询学生界面
        elif Admin.flag == 'select_Student':
            Label(self.admin_root, text = "查询学生:",font = ('黑体','12','bold')).place(x = 10, y = 10)

            self.SelectStudentVar = StringVar(self.admin_root)
            self.SelectStudentVar.set('学号')
            self.SelectOM = OptionMenu(self.admin_root, self.SelectStudentVar, '学号','姓名','专业','学院')
            self.SelectOM.place(x = 780, y = 200)
            self.SelectStudentText = Entry(self.admin_root, width = 15)
            self.SelectStudentText.place(x = 860, y = 204	)
            def CleanSelectStudentText(event):
                self.SelectStudentText.delete(0, 15)
            self.SelectOM.bind('<Button-1>',CleanSelectStudentText)
            Button(self.admin_root, text = '确定',width = 7,command = self.Select_Student_Sure).place(x = 900, y = 250)
            Button(self.admin_root, text = '全部',width = 7,command = self.Select_ALLStudent_Sure).place(x = 780, y = 250)
            

            Label(self.admin_root, text = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(25,'  学 号',25,'姓 名',20,'性 别',50,'学 院',50,'专 业',20,'年 级',50,'贯 籍')).place(x = 5, y = 35)
            self.ListboxVar = StringVar()
	    self.SelectStudent = Listbox(self.admin_root,listvariable=self.ListboxVar, height = 29, width = 105)
            self.sl2 = Scrollbar(self.admin_root)
            self.sl2.place(x = 744, y =60, height = 525, width = 20)
            self.SelectStudent['yscrollcommand'] = self.sl2.set
	    self.SelectStudent.place(x = 5, y = 60)
            self.sl2['command'] = self.SelectStudent.yview
            sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                    self.SelectStudent.insert(END, fm)
        
        #查询课程界面
        elif Admin.flag == 'select_Course':
            Label(self.admin_root, text = "查询课程:",font = ('黑体','12','bold')).place(x = 10, y = 10)
            Label(self.admin_root, text = '%-*s%-*s%-*s%-*s%-*s'%(70,'  科  目',30,'老 师',30,'地点',60,'上课周',60,'时 间')).place(x = 5, y = 35)
	    self.SelectCourse = Listbox(self.admin_root, height = 29, width = 105)
            self.sl1 = Scrollbar(self.admin_root)
            self.sl1.place(x = 744, y =60, height = 525, width = 20)
            self.SelectCourse['yscrollcommand'] = self.sl1.set
	    self.SelectCourse.place(x = 5, y = 60)
            self.sl1['command'] = self.SelectCourse.yview
            sql = "select 名称,姓名,地点,起始周,结束周,上课时间,下课时间 from Course,Teacher where 任课老师=职工号"
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s'%(60,i[0],20,i[1],30,i[2],50,'%s - %s'%(i[3],i[4]),50,'%s - %s'%(i[5],i[6]))
                    self.SelectCourse.insert(END, fm)

    ################ 响应函数模块 ###################

    #添加模块响应函数
    def add_Admin(self):
        if Admin.flag == 'add_Admin':
            return 
        Admin.flag = 'add_Admin'
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()
        Admin()
        Admin.flag = 'add_Admin'

    def add_Admin_Sure(self):
        sql = "select * from Adm_Passwd where 管理员 = '%s'"%self.NewAdmin.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "存在该管理员，添加失败！")
            self.NewAdmin.delete(0, 20)
            self.NewAdminPasswd1.delete(0, 20)
            self.NewAdminPasswd2.delete(0, 20)

        elif self.NewAdminPasswd1.get() != self.NewAdminPasswd2.get():
            tkMessageBox.showinfo("error", "两次密码不一致，添加失败！")
            self.NewAdmin.delete(0, 20)
            self.NewAdminPasswd1.delete(0, 20)
            self.NewAdminPasswd2.delete(0, 20)
        else:
            sql = "insert into Adm_Passwd values(\'%s\', \'%s\')"%(self.NewAdmin.get(), self.NewAdminPasswd1.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count > 0:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewAdmin.delete(0, 20)
                self.NewAdminPasswd1.delete(0, 20)
                self.NewAdminPasswd2.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加失败！")
                self.NewAdmin.delete(0, 20)
                self.NewAdminPasswd1.delete(0, 20)
                self.NewAdminPasswd2.delete(0, 20)

    def add_Course(self):
        if Admin.flag == 'add_Course':
            return
        Admin.flag = 'add_Course'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def add_Course_Sure(self):
        sql = "select * from Course where 课程号 = '%s'"%self.NewCourseID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该课程，添加失败！")
            self.NewCourseID.delete(0, 20)
            self.NewCourseNAME.delete(0, 20)
            self.NewCourseTEACHER.delete(0, 20)
            self.NewCourseLOCAL.delete(0, 20)
            self.NewCourseBEGINWEEK.delete(0, 20)
            self.NewCourseENDWEEK.delete(0, 20)
            self.NewCourseBEGINTIME.delete(0, 20)
            self.NewCourseENDTIME.delete(0, 20)
        else:
            sql = "insert into Course values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"%\
(self.NewCourseID.get(), self.NewCourseNAME.get(), self.NewCourseTEACHER.get(), self.NewCourseBEGINWEEK.get(),\
self.NewCourseENDWEEK.get(), self.NewCourseBEGINTIME.get(), self.NewCourseENDTIME.get(), self.NewCourseLOCAL.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.NewCourseID.delete(0, 20)
                self.NewCourseNAME.delete(0, 20)
                self.NewCourseTEACHER.delete(0, 20)
                self.NewCourseLOCAL.delete(0, 20)
                self.NewCourseBEGINWEEK.delete(0, 20)
                self.NewCourseENDWEEK.delete(0, 20)
                self.NewCourseBEGINTIME.delete(0, 20)
                self.NewCourseENDTIME.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewCourseID.delete(0, 20)
                self.NewCourseNAME.delete(0, 20)
                self.NewCourseTEACHER.delete(0, 20)
                self.NewCourseLOCAL.delete(0, 20)
                self.NewCourseBEGINWEEK.delete(0, 20)
                self.NewCourseENDWEEK.delete(0, 20)
                self.NewCourseBEGINTIME.delete(0, 20)
                self.NewCourseENDTIME.delete(0, 20)
        


    def add_Teacher(self):
        if Admin.flag == 'add_Teacher':
            return
        Admin.flag = 'add_Teacher'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def add_Teacher_Sure(self):
        sql = "select * from Tea_Passwd where 职工号 = '%s'"%self.NewTeacherID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该教师，添加失败！")
            self.NewTeacherID.delete(0, 20)
            self.NewTeacherNAME.delete(0, 20)
            self.NewTeacherSEX.delete(0, 20)
            self.NewTeacherOFFICE.delete(0, 20)
            self.NewTeacherPHONE.delete(0, 20)
            self.NewTeacherCOURSE.delete(0, 20)
        else:
            sql1 = "insert into Tea_Passwd values(\'%s\', \'%s\')"%(self.NewTeacherID.get(), self.NewTeacherID.get())
            count1 = self.cursor.execute(sql1)
            self.db.commit()
            sql2 = "insert into Teacher values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"%(self.NewTeacherID.get(), self.NewTeacherNAME.get(), self.NewTeacherSEX.get(), self.NewTeacherOFFICE.get(), self.NewTeacherCOURSE.get(), self.NewTeacherPHONE.get())
            count2 = self.cursor.execute(sql2)
            self.db.commit()
            if count1 == 0 or count2 == 0:
                sql = "delete from Tea_Passwd where 职工号 = '%s'"%self.NewTeacherID.get()
                count1 = self.cursor.execute(sql)
                self.db.commit()
                sql = "delete from Teacher where 职工号 = '%s'"%self.NewTeacherID.get()
                count1 = self.cursor.execute(sql)
                self.db.commit()

                tkMessageBox.showinfo("error", "添加失败！")
                self.NewTeacherID.delete(0, 20)
                self.NewTeacherNAME.delete(0, 20)
                self.NewTeacherSEX.delete(0, 20)
                self.NewTeacherOFFICE.delete(0, 20)
                self.NewTeacherPHONE.delete(0, 20)
                self.NewTeacherCOURSE.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewTeacherID.delete(0, 20)
                self.NewTeacherNAME.delete(0, 20)
                self.NewTeacherSEX.delete(0, 20)
                self.NewTeacherOFFICE.delete(0, 20)
                self.NewTeacherPHONE.delete(0, 20)
                self.NewTeacherCOURSE.delete(0, 20)

    def add_Student(self):
        if Admin.flag == 'add_Student':
            return
        Admin.flag = 'add_Student'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def add_Student_Sure(self):
        sql = "select * from Stu_Passwd where 学号 = '%s'"%self.NewStudentID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该学生，添加失败！")
            self.NewStudentID.delete(0, 20)
            self.NewStudentNAME.delete(0, 20)
            self.NewStudentMAJOR.delete(0, 20)
            self.NewStudentCLASS.delete(0, 20)
        else:
            sql1 = "insert into Stu_Passwd values(\'%s\', \'%s\')"%(self.NewStudentID.get(), self.NewStudentID.get())
            count1 = self.cursor.execute(sql1)
            self.db.commit()
            sql2 = "insert into Student(学号, 姓名,专业代码, 班级代码) values(\'%s\', \'%s\', \'%s\', \'%s\')"%(self.NewStudentID.get(),self.NewStudentNAME.get(), self.NewStudentMAJOR.get(), self.NewStudentCLASS.get())
            count2 = self.cursor.execute(sql2)
            self.db.commit()
            if count1 == 0 or count2 == 0:
                sql = "delete from Stu_Passwd where 学号 = '%s'"%self.NewStudentID.get()
                count1 = self.cursor.execute(sql)
                self.db.commit()
                sql = "delete from Student where 学号 = '%s'"%self.NewStudentID.get()
                count1 = self.cursor.execute(sql)
                self.db.commit()

                tkMessageBox.showinfo("error", "添加失败！")
                self.NewStudentID.delete(0, 20)
                self.NewStudentNAME.delete(0, 20)
                self.NewStudentMAJOR.delete(0, 20)
                self.NewStudentCLASS.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewStudentID.delete(0, 20)
                self.NewStudentNAME.delete(0, 20)
                self.NewStudentMAJOR.delete(0, 20)
                self.NewStudentCLASS.delete(0, 20)

    def add_College(self):
        if Admin.flag == 'add_College':
            return
        Admin.flag = 'add_College'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def add_College_Sure(self):
        sql = "select * from College where 学院代码 = '%s'"%self.NewCollegeID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该学院，添加失败！")
            self.NewCollegeID.delete(0, 20)
            self.NewCollegeNAME.delete(0, 20)
            self.NewCollegePRESIDENT.delete(0, 20)
        else:
            sql = "insert into College values(\'%s\', \'%s\', \'%s\')"%\
(self.NewCollegeID.get(), self.NewCollegeNAME.get(), self.NewCollegePRESIDENT.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.NewCollegeID.delete(0, 20)
                self.NewCollegeNAME.delete(0, 20)
                self.NewCollegePRESIDENT.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewCollegeID.delete(0, 20)
                self.NewCollegeNAME.delete(0, 20)
                self.NewCollegePRESIDENT.delete(0, 20)

    def add_Major(self):
        if Admin.flag == 'add_Major':
            return
        Admin.flag = 'add_Major'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def add_Major_Sure(self):
        sql = "select * from Major where 专业代码 = '%s'"%self.NewMajorID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该专业，添加失败！")
            self.NewMajorID.delete(0, 20)
            self.NewMajorNAME.delete(0, 20)
            self.NewMajorCOLLEGE.delete(0, 20)
        else:
            sql = "insert into Major values(\'%s\', \'%s\', \'%s\')"%\
(self.NewMajorID.get(), self.NewMajorNAME.get(), self.NewMajorCOLLEGE.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.NewMajorID.delete(0, 20)
                self.NewMajorNAME.delete(0, 20)
                self.NewMajorCOLLEGE.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewMajorID.delete(0, 20)
                self.NewMajorNAME.delete(0, 20)
                self.NewMajorCOLLEGE.delete(0, 20)

    def add_TeacherOffice(self):
        if Admin.flag == 'add_TeacherOffice':
            return 
        Admin.flag = 'add_TeacherOffice'
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()
        Admin()
        Admin.flag = 'add_TeacherOffice'

    def add_TeacherOffice_Sure(self):
        sql = "select * from TeacherOffice where 教研室代码 = '%s'"%self.NewTeacherOfficeID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该教研室，添加失败！")
            self.NewTeacherOfficeID.delete(0, 20)
            self.NewTeacherOfficeNAME.delete(0, 20)
            self.NewTeacherOfficeLOCAL.delete(0, 20)
            self.NewTeacherOfficeCOLLEGE.delete(0, 20)
        else:
            sql = "insert into TeacherOffice values(\'%s\', \'%s\', \'%s\', \'%s\')"%\
(self.NewTeacherOfficeID.get(), self.NewTeacherOfficeNAME.get(), self.NewTeacherOfficeLOCAL.get(), self.NewTeacherOfficeCOLLEGE.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.NewTeacherOfficeID.delete(0, 20)
                self.NewTeacherOfficeNAME.delete(0, 20)
                self.NewTeacherOfficeLOCAL.delete(0, 20)
                self.NewTeacherOfficeCOLLEGE.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewTeacherOfficeID.delete(0, 20)
                self.NewTeacherOfficeNAME.delete(0, 20)
                self.NewTeacherOfficeLOCAL.delete(0, 20)
                self.NewTeacherOfficeCOLLEGE.delete(0, 20)

 


    def add_Class(self):
        if Admin.flag == 'add_Class':
            return 
        Admin.flag = 'add_Class'
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()
        Admin()
        Admin.flag = 'add_Class'

    def add_Class_Sure(self):
        sql = "select * from Class where 班级代码 = '%s'"%self.NewClassID.get()
        count = self.cursor.execute(sql)
        if count > 0:
            tkMessageBox.showinfo("error", "已存在该班级，添加失败！")
            self.NewClassID.delete(0, 20)
            self.NewClassGRADE.delete(0, 20)
            self.NewClassCLASS.delete(0, 20)
            self.NewClassMAJOR.delete(0, 20)
            self.NewClassHEADMASTER.delete(0, 20)
            self.NewClassNUMBER.delete(0, 20)

        else:
            sql = "insert into Class values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"%\
(self.NewClassID.get(), self.NewClassGRADE.get(), self.NewClassCLASS.get(), self.NewClassMAJOR.get(), self.NewClassHEADMASTER.get(), self.NewClassNUMBER.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.NewClassID.delete(0, 20)
                self.NewClassGRADE.delete(0, 20)
                self.NewClassCLASS.delete(0, 20)
                self.NewClassMAJOR.delete(0, 20)
                self.NewClassHEADMASTER.delete(0, 20)
                self.NewClassNUMBER.delete(0, 20)
 

            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.NewClassID.delete(0, 20)
                self.NewClassGRADE.delete(0, 20)
                self.NewClassCLASS.delete(0, 20)
                self.NewClassMAJOR.delete(0, 20)
                self.NewClassHEADMASTER.delete(0, 20)
                self.NewClassNUMBER.delete(0, 20)



    #删除模块响应函数
    def delete_Admin(self):
        if Admin.flag == 'delete_Admin':
            return
        Admin.flag = 'delete_Admin'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def delete_Admin_Sure(self):
        sql = "select * from Adm_Passwd where 管理员 = '%s'"%self.DeleteAdmin.get()
        count = self.cursor.execute(sql)
        if count == 0:
            tkMessageBox.showinfo("error", "不存在该管理员！")
            self.DeleteAdmin.delete(0, 20)
        else:
            sql = "delete from Adm_Passwd where 管理员='%s'"%self.DeleteAdmin.get()
            count = self.cursor.execute(sql)
            self.db.commit()
            if count > 0:
                tkMessageBox.showinfo("Message", "删除成功！")
                self.DeleteAdmin.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "删除失败！")
                self.DeleteAdmin.delete(0, 20)


    def delete_Teacher(self):
        if Admin.flag == 'delete_Teacher':
            return
        Admin.flag = 'delete_Teacher'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def delete_Student(self):
        if Admin.flag == 'delete_Student':
            return
        Admin.flag = 'delete_Student'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()


    #修改模块响应函数
    def modify_Passwd(self):
        if Admin.flag == 'modify_Passwd':
            return
        Admin.flag = 'modify_Passwd'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def modify_Passwd_Sure(self):
        sql = "select * from Adm_Passwd where 管理员 ='%s'"%Admin.User
        count = self.cursor.execute(sql)
        if count > 0:
            result = self.cursor.fetchone()
            passwd = str(result[1])
            if passwd != self.OldPasswd.get():
                tkMessageBox.showinfo('Message','原密码错误')
            elif self.NewPasswd1.get() != self.NewPasswd2.get():
                tkMessageBox.showinfo('Message', '两次密码不一致')
            else:
                sql = "update Adm_Passwd set  密码='%s' where 管理员 ='%s'"%(self.NewPasswd1.get(),Admin.User)
                self.cursor.execute(sql)
                self.db.commit()
                tkMessageBox.showinfo('Message', '修改成功')
                self.OldPasswd.delete(0, 20)
                self.NewPasswd1.delete(0, 20)
                self.NewPasswd2.delete(0, 20)
        else:
            tkMessageBox.showinfo('Message','passwd error')


    def modify_Teacher(self):
        if Admin.flag == 'modify_Teacher':
            return
        Admin.flag = 'modify_Teacher'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def modify_Teacher_Sure(self):
        sql = "select * from Tea_Passwd where 职工号 = '%s'"%self.ModifyTeacherID.get()
        count = self.cursor.execute(sql)
        if count == 0:
            tkMessageBox.showinfo("error", "不存在该教师，修改失败！")
            self.ModifyTeacherID.delete(0, 20)
            self.ModifyTeacherNAME.delete(0, 20)
            self.ModifyTeacherSEX.delete(0, 20)
            self.ModifyTeacherOFFICE.delete(0, 20)
            self.ModifyTeacherCOURSE.delete(0, 20)
            self.ModifyTeacherPHONE.delete(0, 20)
        else:
            sql = "update Teacher set  姓名='%s',性别='%s',所在教研室='%s',任课='%s',电话='%s' where 职工号 ='%s'"%(self.ModifyTeacherNAME.get(), self.ModifyTeacherSEX.get(), self.ModifyTeacherOFFICE.get(), self.ModifyTeacherCOURSE.get(), self.ModifyTeacherPHONE.get(),self.ModifyTeacherID.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.ModifyTeacherID.delete(0, 20)
                self.ModifyTeacherNAME.delete(0, 20)
                self.ModifyTeacherSEX.delete(0, 20)
                self.ModifyTeacherOFFICE.delete(0, 20)
                self.ModifyTeacherCOURSE.delete(0, 20)
                self.ModifyTeacherPHONE.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.ModifyTeacherID.delete(0, 20)
                self.ModifyTeacherNAME.delete(0, 20)
                self.ModifyTeacherSEX.delete(0, 20)
                self.ModifyTeacherOFFICE.delete(0, 20)
                self.ModifyTeacherCOURSE.delete(0, 20)
                self.ModifyTeacherPHONE.delete(0, 20)


    def modify_Student(self):
        if Admin.flag == 'modify_Student':
            return
        Admin.flag = 'modify_Student'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()


    def modify_Student_Sure(self):
        sql = "select * from Stu_Passwd where 学号 = '%s'"%self.ModifyStudentID.get()
        count = self.cursor.execute(sql)
        if count == 0:
            self.ModifyStudentID.delete(0, 20)
            self.ModifyStudentMAJOR.delete(0, 20)
            self.ModifyStudentCLASS.delete(0, 20)
            tkMessageBox.showinfo("error", "不存在该学生，修改失败！")
        else:
            sql = "update Student set  专业代码='%s',班级代码='%s' where 学号='%s'"%(self.ModifyStudentMAJOR.get(), self.ModifyStudentCLASS.get(),self.ModifyStudentID.get())
            count = self.cursor.execute(sql)
            self.db.commit()
            if count == 0:
                tkMessageBox.showinfo("error", "添加失败！")
                self.ModifyStudentID.delete(0, 20)
                self.ModifyStudentMAJOR.delete(0, 20)
                self.ModifyStudentCLASS.delete(0, 20)
            else:
                tkMessageBox.showinfo("Message", "添加成功！")
                self.ModifyStudentID.delete(0, 20)
                self.ModifyStudentMAJOR.delete(0, 20)
                self.ModifyStudentCLASS.delete(0, 20)

    #查询模块响应函数
    def select_Admin(self):
        if Admin.flag == 'select_Admin':
            return
        Admin.flag = 'select_Admin'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def select_Teacher(self):
        if Admin.flag == 'select_Teacher':
            return
        Admin.flag = 'select_Teacher'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def select_Student(self):
        if Admin.flag == 'select_Student':
            return
        Admin.flag = 'select_Student'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()

    def Select_Student_Sure(self):
        self.ListboxVar.set('')
        if self.SelectStudentVar.get() == '学号':
            sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where Student.学号='%s' and Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"%self.SelectStudentText.get()
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                    self.SelectStudent.insert(END, fm)

        elif self.SelectStudentVar.get() == '姓名':
            sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where Student.姓名='%s' and Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"%self.SelectStudentText.get()
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                    self.SelectStudent.insert(END, fm)

        elif self.SelectStudentVar.get() == '专业':
            sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where Major.名称='%s' and Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"%self.SelectStudentText.get()
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                    self.SelectStudent.insert(END, fm)

        elif self.SelectStudentVar.get() == '学院':
            sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where College.名称='%s' and Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"%self.SelectStudentText.get()
            num = self.cursor.execute(sql)
            if num > 0:
                result = self.cursor.fetchmany(num)
                for i in result:
                    fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                    self.SelectStudent.insert(END, fm)

    def Select_ALLStudent_Sure(self):
        self.ListboxVar.set('')
        sql = "select Student.学号,Student.姓名,Student.性别,College.名称,Major.名称,年级,班级,贯籍 from Student,Major,Class,College where Student.专业代码=Major.专业代码 and Student.班级代码=Class.班级代码 and Major.所在学院=College.学院代码"
        num = self.cursor.execute(sql)
        if num > 0:
            result = self.cursor.fetchmany(num)
            for i in result:
                fm = '%-*s%-*s%-*s%-*s%-*s%-*s%-*s'%(20,i[0],20,i[1],15,i[2],35,i[3],38,i[4],15,'%s.%s'%(i[5],i[6]),50,i[7])
                self.SelectStudent.insert(END, fm)


    def select_Course(self):
        if Admin.flag == 'select_Course':
            return
        Admin.flag = 'select_Course'
        Admin()
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()


    #注销
    def logout(self):
        self.cursor.close()
        self.db.close()
        self.admin_root.destroy()
        import Educational_System.login
        Educational_System.login.Login()


if __name__=='__main__':
    administrator = Admin()
    Admin.User = 'root'
    administrator.admin_root.mainloop()
