# for i in range(6):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#          print('*',end=" ")
#     print()
#
# for i in range(6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# for i in range(6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end=" ")
#     print()
#
# for i in range(6,0,-1):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end=" ")
#     print()

#Q1) Write a Program To REVERSE content of the given String by using slice operator?

# a = "saiprasad"
# a = a[::-1]
# print(a)

#Q2) Write a Program To REVERSE content of the given String by using reversed() function?

# a = input("enter the content to be reversed:=")
# x = reversed(a)
# for i in x:
#     print(i,end="")

#Q3)Write a Program To REVERSE content of the given String by using while loop?

# str = input("enter the content to be reversed:=")
# n = len(str)-1
#
# while n>=0:
#     print(str[n],end="")
#     n-=1

#Q4) Write a Program To REVERSE order of words present in the given string?

# a = "python is very very easy to learn "
# x = a.split()
# x = x[::-1]
# a = " ".join(x)
# print(a)

#Q5) Write a Program To REVERSE internal content of each word?

# a = "saiprasad satish sonawane"
# x = a.split()
# b = []
# for i in x:
#     b.append(i[::-1])
# st = " ".join(b)
# print(st)

#Q6) Write a Program To REVERSE internal content of every second word present in the given string?
# a = input('enter any word:=')
# x = a.split()
# b =[]
# for i in range(len(x)):
#     if i%2==0:
#         b.append(x[i])
#     else:
#         b.append(x[i][::-1])
# result = " ".join(b)
# print(result)

#Q8) Write a program to merge characters of 2 strings into a single string by taking characters alternatively?

# s1 = "ravi"
# s2 = "teja"
# i,j = 0,0
# while i<len(s1) and j<len(s2):
#     print(s1[i]+s2[j],end="")
#     i+=1
#     j+=1

#If strings having different lengths:
# s1=input('Enter First String:')
# s2=input('Enter Second String:')
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#      if i<len(s1):
#          output=output+s1[i]
#          i=i+1
#      if j<len(s2):
#          output=output+s2[j]
#          j=j+1
# print(output)

#Q9) Assume input string contains only alphabet symbols and digits.
#Write a program to sort characters of the string, first alphabet
#symbols followed by digits?

# s='sf3loih2jdcx1hdus4owp'
# a =[]
# b = []
# for i in s:
#     if i.isalpha():
#         a.append(i)
#
#     else:
#         b.append(i)
#
# result = "".join(sorted(b)+sorted(a))
# print(result)

#Write a program for the following requirement?  input: a4b3c2 2 output: aaaabbbcc

# s=input('Enter Some String where alphabet symbol should be followed by digit:')
# result = ""
# for i in s:
#     if i.isalpha():
#         x = i
#     else:
#         d = int(i)
#         result = result+x*d
#
# output = "".join(sorted(result))
# print(output)

# Q14) Write a program to remove duplicate characters from the given
# input String?
# Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
# Output: AZBCDEF
# print(result)

# s = "AZZZBCDABBCDABBBBCCCCDDDDEEEEEF"
# a = []
# for i in s:
#     if i not in a:
#         a.append(i)
# print("".join(a))

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
#     print()
# for i in range(6,0-1):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
#     print()

# n = 3
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range( n ,0,-1):
#     print(" " * (n - i), end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
