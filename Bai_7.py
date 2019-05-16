print("Nhập email của bạn: ")
s=input()
def NameCheck(x):
    h=0
    p=s.lower()
    T=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','.','_']
    for i in range(0,x):
        if p[i] not in T:
            h=1
        else:
            if h!=0:
                return 0
    return 1
def DomainCheck(x):
    point=0
    if s[len(s)-1]=='.':
        return 0
    #print(x,len(s)-2)
    for i in range(x+1,(len(s)-1)):
        #print(i,s[i],s[i+1])
        if s[i]=='.':
            if (s[i+1]!='.'):
                point=point+1
            else:
                #print('1')
                return 0
    print(point)
    if 1<=point<=3:
        return 1
    elif point==4:
        for i in [(x+1)-(len(s)-1)]:
            if s[i]!='.' and s[i] not in['0'-'9']:
                #print('2')
                return 0
    else:
        #print('3')
        return 0
    return 1
def Checkmail():
    mark=s.rfind('@')
    #print(mark)
    if (DomainCheck(mark))==1 and (NameCheck(mark)==1):
        print("Tên người dùng: ",s[0:mark])
        print("Công ty: ",s[mark+1:len(s)])
    else: 
        print("Mail nhập vào không đúng")
    return 1
print(Checkmail())