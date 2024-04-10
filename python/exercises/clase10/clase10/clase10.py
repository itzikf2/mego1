# def mirror (m):
#     left=0
#     right=0
#     while(left<right):
#         ezer=m[left]
#         m[left]=m[right]
#         m[right]=ezer
#         right-=1
#         left+=1
        
# a=[1,2,3,4,5,6,7]
# print(a)
# mirror(a)

# a=[10,20,31,40,57,62,70,89,77]
# right=len(a)-1
# left=0
# while(left<len(a) and a[left]%2==0):
#     left+=1
# if(left<len(a)-1):
#     while(right>=left and a[right]%2==1):
#         right-=1
#     while(left<right):
#         if(a[right]%2==0 and a[left]%2==1):
#             ezer=a[right]
#             a[right]=a[left]
#             a[left]=ezer
#             right-=1
#             left+=1
#         else:
#             if(a[right]%2==1):
#                 a[right]-=1
#             if(a[left]%2==0):
#                 (a[left])+=1
                
# a=[
#     [1,4,4,6,5,7], 
#     [4,3,6,9,9,9],
#     [3,6,5,7,9,1],
#     [9,3,7,5,7,1],
#     [5,3,6,8,7,6] 
#  ]
# for c in range(len(a[0])):
#     max=a[0][c]
#     for r in range(1,len(a)):
#         if(a[r][c] > max):
#             max=a[r][c]
#     print(max)
# m=0
# for r in range(len(a)-1):
#     for c in range(len(a)[0]-1):
#         if(a[r][c]==a[r][c+1]):
#             m+=1
#         if(a[r][c]==a[r+1][c]):
#            m+=1
# for r in range (len(a)-1):
#     if(a[r][len(a)-1]==a[r+1][len(a)-1]):
#         m+=1
# for c in range (len(a[0])-1):


import random
def BinariSearch(a):
    low=0
    up=len(a)-1
    while(low<=up):
        mid=(low+up)//2
        if(x==a[mid]):
            return mid
        if(x<a[mid]):
            up=mid-1
        else:
            low=mid+1
    return -1
   
a=[0]*10000
a[0]=2
for i in range(1,len(a)):
    a[i]=a[i-1]+random.randint(1,6)
print(a)    
x=int(input("Enter a number : "))
print(BinariSearch(a)) 
