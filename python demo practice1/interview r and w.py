# with open('test.txt',"w") as f:
#     f.write()
#
# with open('test.txt',"r")

# list=[1,2,3,4]
# list[0]=100


# # fibonacci series
# #0,1,1,2,3,5
# #a,b,c
# #  a,b,c
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
#
# fib(10)

# # factorial
# # 5! = 5*4*3*2*1
#
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# x=int(input('enter the value'))
# result=fact(x)
# print(result)


# recursion

# import sys
# sys.setrecursionlimit()
# sys.getrecursionlimit()
#
# i=0
# def greet():
#     global i
#     print('hello',i)
#     i+=1
#     greet()  #recursion
#
# greet()

# # factorial using recursion
#
# def fact(n):
#         if n==0:
#                 return 1
#         return n * fact(n-1) #
#
# result = fact(5)
#
# print(result)

















# def add(x,y):
#     return x+y
#
#
# add= lambda x,y:x+y
# print(add(10,2))