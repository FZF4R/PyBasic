print("Nhập số N: ")
T=1
def Giaithua(x):
    if x==1:
        return 1
    else:
        return T*Giaithua(x-1)*x
x=int(input())
print(Giaithua(x))