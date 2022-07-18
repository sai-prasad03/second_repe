# def decor(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return x+5
#     return inner
#
# @decor
# @decor2
# def num():
#     return 5
#
# print(num())


# def myfun():
#     yield "a"
#     yield "b"
#
# m = myfun()
# print(m)
#print(next(m))

# s = "abcbbcca"
# d = {}
# for i in s:
#     if i in d.keys():
#         d[i] = d[i]+1
#
#     else:
#         d[i] = 1
# for k,v in d.items():
#     print(f'{v} times {k}')
#
# print(d)
# from datetime import date
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def FromBirthyear(cls,name,year):
#         return cls(name,date.today().year-year)
#
#     @staticmethod
#     def isadult(age):
#         return age>18
#
# person1 = Person("saiprasad",29)
# person2 = Person.FromBirthyear("sai",1993)
# print(person1.age)
# print(person2.age)
# print(Person.isadult(29))