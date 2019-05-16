print("Nhập dữ liệu: ")
def strnumber(x):
    for character in x:
        if character not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 0
    return 1
def Check():
    #t=y.find('int') 
    x=input();
    if strnumber(x)==1:
        if (x[len(x)-1] in ['0', '2', '4', '6', '8']):
            print("Đây là một số chẵn")
        else:
            print("Đây là một số lẻ")
    else: print("Không phải số nguyên")
Check()