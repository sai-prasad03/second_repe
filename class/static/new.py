# n = int(input('enter number to check whether is armstrong number or not:='))
# s = n
# b = len(str(n))
# sum = 0
# while n!=0:
#     r = n%10
#     sum+=r**b
#     n = n//10
# if s ==sum:
#     print("the given number is armstrong number")
# else:
#     print("the given number is not armstrong number")

# n = int(input('enter number :='))
# fact =1
# for i in range(1,1+n):
#     fact = fact*i
# print(fact)
#
# def fact(n):
#     if n ==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
#print(fact(5))


# lower = 1
# upper = 100
# print("prime no. between",lower,"and",upper)
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i) ==0:
#                 break
#         else:
#             print(num)


# s = "saiprasad"
# d = {}
# for i in s:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for k,v in d.items():
#     print(f"{v} times {k}")

# def fib(n):
#     if n<0:
#         print("please provide positive number")
#     elif n ==0:
#         return 0
#     elif n == 1 or n ==0:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# a = fib(9)
# print(a)

# lst = [10,45,15,25,60,55]
# largest = lst[0]
# for i in lst:
#     if i <largest:
#         largest = i
# print(largest)
# second_largest = 0
# for i in lst:
#     if i!= largest and i >second_largest:
#         second_largest = i
#   print(second_largest)








