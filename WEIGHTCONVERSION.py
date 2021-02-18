weight=int(input("enter your weight lbs(l) or in kgs(k) = "))
unit=input('weihtt in lbs(L) or kilogram(K)')
if unit.upper() == "L":
    x=weight/1.45
    print("SO WEIGHT IN kg is = ",x)
elif unit.upper()=="K":
    y=weight*1.45
    print("so weight in lbs is =",y)
