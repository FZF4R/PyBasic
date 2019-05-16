def DaoNguoc():
    print("Nhập số nguyên: ")
    x=int(input());
    while x!=0:
        print(x%10,end ='');
        x=int(x/10);
DaoNguoc()    