import time;
def Picture():
    print("Name Picture: ")
    Pic=input()
    Pic=Pic + ' ' + time.asctime()
    return Pic
print(Picture())