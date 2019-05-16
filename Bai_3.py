def Chia():
    print("Nhập số chia, số bị chia trên 2 dòng: ")
    a=int(input())
    b=int(input())
    try :
        Result=a/b
        print('Kết quả: ',Result)
    except ZeroDivisionError:
        print('Không thể chia cho 0')
Chia();