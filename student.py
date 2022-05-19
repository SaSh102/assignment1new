name = input("enter name:")
family = input("enter family:")
a = float(input("enter corse number A:"))
b = float(input("enter corse number B:"))
c = float(input("enter corse number C:"))

ave = (a + b + c) / 3
if ave >= 17:
    result = "Great"
if ave < 12:
    result = "Fail"
else :
    result = "Normal"

print ("name is ", name, "family is", family, "average is ", result)