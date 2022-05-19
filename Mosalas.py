a = int(input("enter size A as num:"))
b = int(input("enter size B as num:"))
c = int(input("enter size C as num:"))

if ((a<=(b+c)) and (b<=(a+c)) and (c<=(a+b))):
    result = "mosalas ghabele ejra ast."
else:
    result = "error"
print ("result is:",result)