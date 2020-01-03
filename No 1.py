num1= int(input("enter the smaller range: "))
num2= int(input("enter the bigger range: "))

for i in range (num1,num2+1):
    if (i%7==0 and i%5==0):
        print(i)

        
