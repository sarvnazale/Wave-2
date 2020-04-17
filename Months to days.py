month = input("What month is it? ")

if month == "April" or "June" or "September" or "November":
    print(month, "has 30 days.")
elif month == "Febraury":
    print(month, "has 28 or 29 days.")
else:
    print(month, "has 31 days.")
