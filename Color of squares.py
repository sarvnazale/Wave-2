letter = input("Enter the letter of the column: ")
number = int(input("Enter the number of the row: "))
oddcolumns = ['a', 'c', 'e', 'g']
evencolumns = ['b', 'd', 'f', 'h']
if (number % 2 == 1) and letter in oddcolumns:
    print("The square is black.")
elif (number % 2 == 0) and letter in evencolumns:
    print("The square is black.")
else:
    print("The square is white.")