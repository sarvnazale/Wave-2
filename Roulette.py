from random import randrange

#number 0 is represented by 0, 1-36 are represented by their own value, 00 is represented by 38
number = randrange(0, 38)

#list of numbers on red spaces
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

#display output and amount to pay
if number == 38:
    print("Pay 00.")
elif number == 0:
    print("Pay 0.")
else: 
    print("The spin resulted in %d..." % number)
    print("Pay %d" % number)

#display color bet
if number in red: 
    print("Pay Red")
elif number == 38 or number == 0:
    pass
else:
    print("Pay Black")

#display odd or even
if number == 0 or number == 38: 
    pass
elif number % 2 == 0: 
    print("Pay Even")
else:
    print("Pay Odd")

#display range 
if 1 <= number <= 18:
    print("Pay 1 to 18")
elif 18 < number <= 36: 
    print("Pay 19 to 36")

