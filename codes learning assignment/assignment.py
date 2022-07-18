# 1 write a python program to find reminde when the number is divided by 2

# a = int(input("enter the number:="))
# x = a%2
# print("The reminder of given no.after divided by 2 is",x)

#2 write a python program to find average of two number entered by user

# a = int(input('enter first number:='))
# b = int(input("enter second number:="))
# x = (a+b)/2
# print("the average of","and",b,"is",x)

#3 write a python program to detect spaces in a string
import re

# str = "my name is saiprasad"
# x = str.find(" ")
# print(x)

#4 write a python program to store five fruits in list entered by user

# lst = []
# n = int(input("enter the elements in the list:="))
# for i in range(n):
#     lst.append(input("enter fruit name:="))
#
# print(lst)

#5 write a python program to accept marks of 6 student and display them in sorted manner

# stu_marks = []
# n = int(input("enter the no. of student marks:="))
# for i in range(n):
#      stu_marks.append(input("enter the marks:="))
#      stu_marks.sort()
#
# print(stu_marks)

#6 write a python program to sum a list with 4 numbers

# lst = [10,20,30,40]
#print(sum(lst))

#7 write a python program to count no. of zeros in tuple
# t = (7,0,8,0,0,9)
# print(t.count(0))

# 8 write a python program to create a dictionary hindi words as value and theire english transalation

# d ={}
# n = int(input("enter the no.of element in dict:="))
# for i in range(n):
#     k = input("enter the hindi word:=")
#     v = input("enter the translation:= ")
#     d.update({k:v})
#
# print(d)
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))

# 9 create an empty dictionary allow 4 freind to enter theire favorite language as value and use key as theire name

# favorite = {}
# n = int(input("enter the no.of element in dict:="))
# for i in range(n):
#      k = input("enter the name of friend:=")
#      v = input("enter the favorite language:= ")
#      favorite.update({k:v})
# print(favorite)

# 10 write a program to find greatest of four number entered by user
# lst = []
# n = int(input("enter the no.s in list:="))
# for i in range(n):
#     lst.append(input("enter number:="))
#
#
# print("the greatest no.is",max(lst))

# 11 write a programm to check whether the student is pass or fail,if it require total 40%and
# at least 33% in each subject to pass assume 3 subject and take marks from the user

# marks = []
# n = int(input("enter the no.of subject:="))
# for i in range(n):
#     marks.append(int(input("enter the marks")))
# print(marks)
# sum = 0
# for x in marks:
#     if x<33:
#         print("student is fail")
#         break
#         sum = sum + i
#
#     elif sum / 3 < 40:
#         print("fail")
#
#     else:
#         print("student is pass")

# 12 write a program to find out greatest of three numbers using function

# def greatest(n1,n2,n3):
#     if n1>n2:
#         print(n1,"is greatest")
#     elif n2>n3>n1:
#         print(n2,"is greatest")
#     else:
#         print(n3,"is greatest")
#
# greatest(151,85,45)
#

#13 write a recursive function to calculate the sum of first n natural numbers

# def rec_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + rec_sum(n-1)
#
# print(rec_sum(16))

# 14 write a python program function to remove a given word from a list and strip it at the same time
# def show(str,word):
#     new_str= str.replace(word," ")
#     return new_str.strip()
#
# this = "saiprasad is a good boy"
# n = show(this,"saiprasad")
# print(n)

#15 write a python program to print multiplication table of a given number using for loop

# n = int(input("enter number to find its table:="))
# for i in range(1,11):
#     print(f'{n}*{i}={n*i}')

# 16 write a program to read the text from a given file "poem text"and find out wheather it continues the word twinlkle

# with open("poem.txt","w") as f:
#     f.writelines("""Twinkle, twinkle, little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle, twinkle, little star
# How I wonder what you are
# When the blazing sun is gone
# When he nothing shines upon
# Then you show your little light
# Twinkle, twinkle, all the night
# Twinkle, twinkle, little star
# How I wonder what you are""")

# f = open("poem.txt","r")
# data = f.read()
# import re
# patt = re.compile("twinkle")
# matches = patt.finditer(data)
# for match in matches:
#     print(match)
# print(data[118:125])

# method 2
# with open("poem.txt","r") as f:
#     data = f.read()
#     if "twinkle" in data:
#         print("twinkle is present")
#     else:
#         print("twinkle is not present")

# 17 write a program to find out whether a file is identical and makes content of another file

# with open("log.txt","r")as f:
#     f1 =f.read()
# with open("this.txt","r") as f:
#     f2 =f.read()
#
# if f1==f2:
#     print("file is identical")
# else:
#     print("file is not identical")

#18 create a class programmer for storing information of two programmer working at microsoft

# class Programmer:
#     def __init__(self,employee_name,company):
#         self.employee_name = employee_name
#         self.company = company
#
#     def get_info(self):
#         print(f'{self.employee_name} is working in {self.company}')
# x = Programmer("saiprasad","google")
# x.get_info()

#19 write a class calculator to finding square,cube and squareroot of a number
#
# class Calculator:
#     def __init__(self,n):
#         self.n = n
#
#     def square(self):
#         print(f"the square of {self.n}is:= {self.n**2}")
#
#     def cube(self):
#         print(f"the cube of {self.n} is:= {self.n**3}")
#
#     def square_root(self):
#         print(f"the square_root of {self.n} is:= {self.n ** 0.5}")
#
# x = Calculator(25)
# x.cube()
# x.square()
# x.square_root()

#20 create a class with a class attribute a; create an object from it and set a directory using object a=0
#does this change class attributes

# class Sample:
#     a = "ram"
#
# obj = Sample()
# obj.a = "shyam"
# Sample.a = "shyam"
# print(obj.a)
# print(Sample.a)

#21 wirte a class train which has methods to book ticket,get status(no.of seats)and get fair information of train running under indin railway
#
# class Train:
#     def __init__(self,name,fare,seats):
#         self.name = name
#         self .fare = fare
#         self.seats = seats
#
#     def get_status(self):
#         print("*********")
#         print(f"The name of train is {self.name} ")
#         print(f"The number of available seats are {self.seats}")
#         print("**********")
#     def fare_info(self):
#         print(f"the price of the ticket is {self.fare}")
#
#     def book_ticket(self):
#         if (self.seats>0):
#             print(f"your ticket is booked and seat no. is {self.seats}")
#             self.seats = self.seats-1
#
#         else:
#             print("sorry this train is full kindly try in Tatkal")
#
#     def cancel_ticket(self,seat_no):
#         pass
#
# intercity = Train("hutatma express",150,980)
# intercity.get_status()
# intercity.fare_info()
#intercity.book_ticket()

#22 create a class pets from class animals and further create class dog form pet,and add a method bark to a class dog
#
# class Animals:
#     animal = "mammal"
#     def __init__(self):
#         print("this is parent constructor class")
#
# class Pets(Animals):
#         colour = "white"
#
# class Dog(Pets):
#     def bark(self):
#         print("bhauo,bhauo")
#
# x = Dog()
# x.bark()




