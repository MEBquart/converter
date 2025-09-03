"This is converter "

#convert v value to f
def convertCtoF():
    C= float(input("Ievadi C:"))
    F = (C * 9/5) +32
    print(F)

def convertFtoC():
    F= float(input("Ievadi C:"))
    C= (F - 32) * 5/9
    print(C)
