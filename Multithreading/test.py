#find out the largest number in the list
#without using in built function
# a = [10,5,15,35,80,5]
# largest = 0
# for i in a:
#     if i >largest:
#         largest = i
# print(largest)

#with using inbuilt function

# a = [10,50,3,0,45,25]
# a.sort()
# print('the largest number in list',a[-1])



# find out the second largest number in the list
# a = [10,500,25,15,1500,12,2000,15,25]
# largest = 0
# for i in a:
#     if i>largest:
#         largest = i
# second_largest = 0
# for i in a:
#     if i!=largest and i>second_largest:
#         second_largest = i
# print(second_largest)

# a = [10,20,50,80,25]
# a.sort()
# print("the second largest number in the list",a[-2])


#Python program to interchange first and last elements in a list

# list = [10,20,30,40,50,60,70,80,90]
# list[0],list[8] = list[8],list[0]
# print(list)

#[25]Python program to print even numbers in a list

#by using list comprehension
# lst = [1,2,3,4,5,6,7,8,9]
# even_no = [x for x in lst if x%2==0]
# print(even_no)
# by using lambda function
# lst = [1,2,3,4,5,6,7,8,9]
# even_no = list(filter(lambda x:x%2==0,lst))
# print(even_no)

#using for loop
# lst = [1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if i%2==0:
#         print(i,end=" ")

#using while loop
# lst = [1,2,3,4,5,6,7,8,9]
# i = 0
# while i <= len(lst):
#     print(i,end=" ")
#     i+=2

#[27] Python program to print all even numbers in a range
# lst = [x for x in range(20) if x%2==0]
# print(lst)

#[28] Python program to print all odd numbers in a range

# lst = [x for x in range(20) if x%2==1 ]
# print(lst)

#[29] Python program to count Even and Odd numbers in a List
#lst = [1,2,3,4,5,6,7,8,9]
# even = [x for x in lst if x%2 ==0]
# odd = [x for x in lst if x%2 ==1]
# print("even numbers in list",len(even))
# print("odd numbers in list",len(odd))

# [30] Python program to print positive numbers in list
# lst = [-20,30,-10,-5,22,15,25,30,-8]
# positive_number = [x for x in lst if x>=0]
# print(positive_number)

#[31] Python program to print negative numbers in a list
# lst = [-20,30,-10,-5,22,15,25,30,-8]
# Negative_number = [x for x in lst if x<=0]
# print(Negative_number)

#[32] Python program to print all positive numbers in a range

# list = [x for x in range(-10,10) if x>=0]
# print(list)

#[33] Python program to print all negative numbers in a range

# list = [x for x in range(-10,10) if x<=0]
# print(list)

#[35] Remove multiple elements from a list in Python
# lst = [ 10,20,3,5,65,7]
# a = lst[1:4]
# print(a)

#[36]Python | Remove empty tuples from a list

#lst = [( ),10,20,30,40,50]
# lst.remove(lst[0])
# print(lst)

# lst = [10,20,30,(),40,50]
# for i in lst:
#     if type(i) is int:
#         print(i, end = " ")

#[37] Python | Program to print duplicates from a list of integers

# lst = [1,5,6,4,5,15,87,5,6,9]
# new = []
# for a in lst:
#     n = lst.count(a)
#     if n > 1:
#        #if new.count(a) == 0:
#              new.append(a)
#
# print(new)

#[39] Python | Sort the values of first list using second list

# def sort_list(list1, list2):
#     pairs = zip(list2, list1)
#
#     z = [x for x in sorted(pairs)]
#
#     return z
#
# x=["h","l","r","a","u"]
# y=[ 2,  4,  0,  1, 3]
#
# a =(sort_list(x,y))
# print(a)

#[40]Python program to check if a string is palindrome or not Reverse words in a given String in

# s = input("enter the string to check whether it is palindrome or not:-")
# if s == s[::-1]:
#     print("given string is palindrome")
#
# else:
#     print("given string is not palindrome")

#[41] Python Ways to remove i’th character from string

# s = "saiprasad"
#
# for i in s:
#     if i == "r":
#         continue
#     else:
#         print(i,end="")

#[42] Python | Check if a Substring is Present in a Given String Find length of a string in python (4ways)
#way1
# s = "saiprasad"
# print(s.startswith("sai"))

#way2
# s = "hello good morning"
# if "good" in s:
#     print("present")
# else:
#     print("absent")

#way3
# s = "saiprasad"
#print(s.endswith("sad"))

#[43] Python program to print even length words in a string

# str = "brainwaorks"
# for i in range(len(str)):
#     if i%2 == 0:
#         print(str[i],end=" ")

# str = "my names is sai"
# a = str.split()
# print(str)
# even = [a[x] for x in range(len(a)) if x%2 ==0]
# print(" ".join(even))

#[44] Python | Program to accept the strings which contains all vowels

# str = input("enter the string:-")
# v = "aeiou"
# t = set(str).intersection(v)
# if t == set(v):
#     print("string is acceptable")
# else:
#     print("vowels not present")

# vowel = set("aeiou")
# str = input("enter string ")
# s = []
# for i in str:
#     if i in vowel:
#         s.append(i)
# if len(s)==len(vowel):
#     print("accept")
#
# else:
#     print("reject")

#[45] Count the Number of matching characters in a pair of string
# import re
# str1 = input("enter string:=")
# str2 = input("enter second string:=")
# count =0
# for x in str1:
#     x = re.search(x,str2)
#     count=count+1
# print(count)

#method 2

# def count(str1,str2):
#     set_str1 = set(str1)
#     set_str2 = set(str2)
#     match_char = set_str1&(set_str2)
#     print(len(match_char))
#
# str1 = input("enter first string:=")
# str2 = input("enter second string:=")
#
# count(str1,str2)



#[46] Python program to count number of
# vowels using sets in given string Remove all duplicates from
#a given string in Python

# str = input("eneter string")
# str2 = set(str)
# count = 0
# for i in str2:
#     if i in "aeiou":
#         count+= 1
#
# print(count)
# print(str2)

# [48] Python program for removing i-th character from a string

# def Remove(str,i):
#     a = str[:i]
#     b = str[i+1:]
#     print(a+b)
#
# Remove("saiprasad",3)

#method2

# str = input("enter string:=")
# i = int(input("enter the i th character to remove from the string "))
# for x in range(len(str)):
#     if x ==i:
#       str = str.replace(str[x],"")
# print(str)

#[49]Python program to split and join a string

# str = input("enter string:-")
# x = str.split(" ")
# print(x)
# y = " ".join(x)
# print(y)

#[50]Check if a given string is binary string or not

# str = input("enter string:-")
# for i in str:
#     if i not in "01":
#         print("no")
#         break
# else:
#         print("yes")

#[51] Find all close matches of input string from a list

# str = input("enter string :-")
# match_str = input("enter string to check :-")
# for i in str:
#     if str.startswith(match_str):
#         print(i,end= "")
#     else:
#         print("match not found")
import difflib
str = ["sai","saiprasad","lion","li"]
x = difflib.get_close_matches('l',str,2)
print(x)




#[52] Python program to find uncommon words from two Strings

# str = set(input("entee first string:-"))
# str2 = set(input("enter second string:-"))
#
# uncommon_words = str.difference(str2)
# print(uncommon_words)

#[53] Swap commas and dots in a String

# def Replace(str):
#     str = str.replace(', ', 'temp')
#     str = str.replace('.', ', ')
#     str = str.replace('temp', '.')
#     return str
#
#
# string = "14, 625, 498.002"
# print(Replace(string))

#[54] Permutation of a given string using inbuilt function

# from itertools import permutations
#
# def show(str):
#     a = permutations(str)
#     for i in a:
#         x = ''.join(i)
#         print(x,end=" ")
#
# name = input("enter the string want to permut:-")
# show(name)


