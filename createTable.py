#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb

#创建教学管理系统(Educational_System)的各类主体表

db = MySQLdb.connect(host="localhost", user="zeng", passwd="8963708",\
                     db="student",charset="utf8")

cursor=db.cursor()


#院系表(College)
cursor.execute("DROP TABLE IF EXISTS College")

sql = """create table College (
         学院代码 varchar(5) not null primary key,
         名称 varchar(50),
         院长 varchar(10) not null)
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

# 教研室信息(TeacherOffice)
cursor.execute("drop table if exists TeacherOffice")

sql = """create table TeacherOffice (
         教研室代码 varchar(5) not null primary key,
         名称 varchar(50),
         地点 varchar(20),
         所在学院 varchar(5))
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

# 学生专业信息表(Major)
cursor.execute("DROP TABLE IF EXISTS Major")

sql = """create table Major (
         专业代码 varchar(5) not null primary key,
         名称 varchar(50),
         所在学院 varchar(5) not null)
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

#班级信息表(Class)
cursor.execute("drop table if exists Class")

sql = """create table Class (
         班级代码 varchar(5) not null primary key,
         年级 varchar(10),
         班级 varchar(10),
         专业代码 varchar(5) not null,
         班主任 varchar(10) not null,
         人数 int(4) )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

#教师信息表(Teacher)
cursor.execute("drop table if exists Teacher")

sql = """create table Teacher (
         职工号 varchar(10) not null primary key,
         姓名 varchar(20),
         性别 varchar(4),
         所在教研室 varchar(5),
         任课 varchar(5),
         电话 varchar(11) )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

#学生信息表(Student)
cursor.execute("drop table if exists Student")

sql = """create table Student (
         学号 varchar(10) not null primary key,
         姓名 varchar(20),
         性别 varchar(4),
         专业代码 varchar(5),
         班级代码 varchar(5),
         贯籍 varchar(50) )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

sql = """insert into Student(学号,姓名,性别,专业代码,班级代码,贯籍) 
                     values (\'10001\',\'zzc\', \'男\', \'10001\', \'10001\', \'陆丰\')"""

cursor.execute(sql)

db.commit()

#课程信息表(Course)
cursor.execute("drop table if exists Course")

sql = """create table Course (
         课程号 varchar(5) not null primary key,
         名称 varchar(30),
         任课老师 varchar(10),
         起始周 int(2),
         结束周 int(2),
         上课时间 char(5),
         下课时间 char(5),
         地点 varchar(10) )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

#选课信息表(OptionCourse)
cursor.execute("drop table if exists OptionCourse")

sql = """create table OptionCourse (
         学号 varchar(10),
         课程号 varchar(5),
         成绩 int,
         constraint prik primary key (学号,课程号))
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)

#管理员登陆表 Adm_Passwd
cursor.execute("drop table if exists Adm_Passwd")

sql = """create table Adm_Passwd (
         管理员 varchar(20) not null primary key,
         密码 varchar(20) not null )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)                               

sql = """insert into Adm_Passwd(管理员, 密码) 
                     values (\'root\',\'root\')"""
         
cursor.execute(sql)

#教师登陆表 Tea_Passwd
cursor.execute("drop table if exists Tea_Passwd")

sql = """create table Tea_Passwd (
         职工号 varchar(10) not null primary key,
         密码 varchar(20) not null )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)                               
sql = """insert into Tea_Passwd(职工号, 密码) 
                     values (\'10001\',\'8963708\')"""
cursor.execute(sql)

#学生登陆表 Stu_Passwd
cursor.execute("drop table if exists Stu_Passwd")

sql = """create table Stu_Passwd (
         学号 varchar(10) not null primary key,
         密码 varchar(20) not null )
         default charset=utf8 default collate=utf8_bin"""

cursor.execute(sql)                               

sql = """insert into Stu_Passwd(学号,密码) 
                     values (\'10001\',\'8963708\')"""

cursor.execute(sql)

db.commit()

cursor.close()

db.close()

