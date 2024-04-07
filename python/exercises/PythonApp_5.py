
# import random
# i=0
# s=0
# while(i<39):
#     n=random.randint(100, 999)
#     if(n%2==0):
#         print(n%10 + (n//10)%10 + n//100)
#     s=s+n
#     i+=1
# print(s/39)    
   
# while(n%2==0):
#     print(n)
#     n=random.randint(10, 99)
# print(n)    



# import random
# n=random.randint(10, 99)
# while(n%2==0):
#     print(n)
#     n=random.randint(10, 99)
# print(n)    

# #   q1 springA 2021
# z=0
# e=0
# for i in range(4):
#     num=int(input("Enter a number : "))
#     if(num>99 and num<1000):
#         print(num%10 + (num//10)%10 + num//100)
#     if(num%2==0):
#         z+=1
#     else:
#         e+=num
# print(z)
# print(e)
   


#   q1 summerA 2020
# num=int(input("Enter a number : "))
# c=0
# z=0
# p=0
# s=0
# while(num!=0):
#     c+=1
#     if(num%2==0):
#         z+=1
#     if(num>0):
#         p+=1
#         s+=num
#     num=int(input("Enter a number : "))
# print(c)    
# print(z)    
# print(s/p)  
   


# def Mul(a, b):
#     r=0
#     while(a>0):
#         r=r+b
#         a-=1
#     return r
# def Hezka(x, y):
#     t=1
#     while(y>0):
#         t=Mul(t,x)
#         y=y-1
#     return t

# print(Hezka(5,4))
# print(Hezka(10,3))
# print(Hezka(6,2))
# print(Hezka(7,1))




# def F(x):
#     r=0
#     i=1
#     #   1  -  2  +  3  -  4  +  5  -  6  +  7  =  4
#     while(i<x):
#         if(i%2==0):
#             r=r-i
#             print(i, " + ", end=" ")
#         else:
#             r=r+i
#             print(i, " - ", end=" ")
#         i+=1
#     if(x%2==0):
#         r=r-x
#     else:
#         r=r+x
#     print(x, " = ", r)
#     return r


# num=int(input("Enter a number : "))
# print(F(num))
# # #   1 - 2 + 3 - 4 + 5 = 3


# def F(x):
#     r=0
#     i=1
#     while(i<x):
#         r=r+i
#         i+=1
#     return r+i

# for i in range(3, 8):
#     print(F(i))



# def F(x):
#     y=x*x
#     return y

# r=F(3)
# print(r)
# print(F(8))



# import math
# def IsPrime(x):
#     if(x%2==0):
#         print("no")
#     else:
#         sqrtX=int(math.sqrt(x)) + 1
#         i=3
#         while(i<sqrtX):
#             if(x%i==0):
#                 print("no")
#                 break
#             i+=2
#         if(i>=sqrtX):
#             print("YES")
       
# IsPrime(100)        
# IsPrime(101)        
# IsPrime(49)        
# IsPrime(80)  

       

# import math
# def ShowDeviders(x):
#     sqrtX=int(math.sqrt(x))
#     for i in range(2, sqrtX, 1):
#         if(x%i==0):
#             print(i, "  ", x//i, end="  ")
#     if(sqrtX*sqrtX==x):
#         print(sqrtX)
#     else:
#         i+=1
#         if(x%i==0):
#             print(i, x//i)
#     print()

# ####    MAIN    ####

# num=int(input("Enter a number : "))
# ShowDeviders(num)


#   2   4   5   10
#   50  25  20  

# input_file=open(r"C:\Users\itzik\OneDrive\Desktop\programas python\Dear Prudence  The Beatles.txt", "r")
# text=input_file.readline()
# print(text)

# input_file=open(r"C:\Users\itzik\OneDrive\Desktop\programas python\Dear Prudence  The Beatles.txt", "r")
# for line in input_file:
#     print(line,end="")

# input_file=open(r"C:\Users\itzik\OneDrive\Desktop\programas python\Dear Prudence  The Beatles.txt", "a")
# input_file.write("123456")

# input_file=open(r"C:\Users\itzik\OneDrive\Desktop\programas python\Dear Prudence  The Beatles.txt", "r")
# for line in input_file:
#     print(line, end="")
   
# filename=r"C:\Users\itzik\OneDrive\Desktop\programas python\Dear Prudence  The Beatles.txt"
# with open(filename, 'r') as input_file:
#   for line in input_file:
#     print(line, end="")

# input_filec=r"C:\Users\itzik\OneDrive\Desktop\programas python\hola bebe .txt"
# input_filev=r"C:\Users\itzik\OneDrive\Desktop\programas python\vacio.txt"
# with open(input_filec,'r') as input_file:
#     with open(input_filev,'w') as copy_file:
#         for line in input_file:
#             copy_file.write(line)





    