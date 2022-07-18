# s = "geeksforgeek"
# d = {}
# for i in s:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for k,v in d.items():
#     print(f"{v} times {k}")
#
# t=[50,80,10,60]
# # print("minimum",min(t))
# largest=0
# for i in t:
#     if i > largest:
#         largest=i
# print(largest)
# minimum=0
# for i in t:
#     if i!=largest and i<minimum:
#         minimum=i
# print(minimum)
#
# t="akshay"
# d={}
# for i in t:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for k,v in d.items():
#     print("{}={} times".format(k,v))

# for i in range(1,10):
#     if i >1:
#         for j in range(2,i):
#             if (i%j ==0):
#                 break
#         else:
#             print(i)


#
# def fib(n):
#     if n ==0:
#         return 0
#     elif n ==1:
#         return 1
#

#     else:
#         return fib(n-1)+fib(n-2)
#
# a = fib(9)
# print(a)

# a = [10,5,15,2,60,55]
# smallest = a[0]
# for i in range(len(a)):
#     if a[i] < smallest:
#         smallest = a[i]
# print(smallest)

# a = [20,10,15,5,25]
# b = []
# n = len(a)
# small = a[0]
# for i in range(n):
#     for j in range(i+1,n):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
#
# print(a)
