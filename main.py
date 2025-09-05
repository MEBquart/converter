"This is converter "

#convert v value to f
def convertCtoF():
    C= float(input("Ievadi C:"))
    F = (C * 9/5) +32
    print(F)

#convert kms to miles
def convertKilometrstoMiles():
    kms = float(input("ievadi attālumu:"))
    if kms>0:
        miles = round(kms/1.6, 2)
    else:
        print("Vērtība nederīga!")
    print(f"Rezultāts ir:{miles}")

convertKilometrstoMiles()