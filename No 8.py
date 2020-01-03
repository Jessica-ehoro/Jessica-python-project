celsius = float(input("enter temperature in celsius: "))
fah = (celsius * 9)/ 5 + 32
fahrenheit = float(input("enter tmperature in fahrenheit: "))
cel = (fahrenheit - 32) * 5 / 9
print('%.2f*C is %0.2f in Fahrenheit' %(celsius, fah))
print('%.2f*F is %0.2f in Celsius' %(fahrenheit, cel))
