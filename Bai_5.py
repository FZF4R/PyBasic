import math
print("Nhập số N: ")
def CheckNT(x):
    if x==1:
        return 0
    else:
        for i in range(2,int(math.sqrt(x))):
            if x%i==0:
                return 0
    return 1
def CheckN(x):
    i=1
    A=[0]
    while (x!=0):
        A.append(x%10)
        x=int(x/10)
        i=i+1
    i=i-1
    for j in range(1,int(i/2)):
        if(A[j]!=A[i-j+1]):
            return 0
    return 1
def Test():
    x=int(input())
    if (CheckN(x)==1) and (CheckNT(x)==1):
        print("Số nhập vào là số Palindrome")
    else:
        print("Số nhập vào không phải số Palindrome")
Test()