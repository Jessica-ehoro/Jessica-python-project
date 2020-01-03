for integers in range(51):
    if integers % 3 == 0 and integers % 5 == 0:
        print("fizzbuzz")
        continue
    elif integers % 3 == 0:
        print("fizz")
        continue
    elif integers % 5 == 0:
        print("buzz")
        continue
    print(integers)
     
