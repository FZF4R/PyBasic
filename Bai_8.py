print("Nhập mật khẩu: ")
Password=input()
def CheckPass():
    if len(Password)>12 or len(Password)<6:
        return "Mật khẩu không hợp lệ"
    else:
        x=y=z=t=0
        for c in Password:
            if c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                x=1
            elif c in ['0','1','2','3','4','5','6','7','8','9']:
                y=1
            elif c in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                z=1
            elif c in ['$','#','@']:
                t=1
        if x*y*z*t==1:
            return "Mật khẩu hợp lệ"
        else:
            return "Mật khẩu không hợp lê"
print(CheckPass())