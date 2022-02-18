# 3. Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

year = input("Enter a year : ")


if len(year) == 4:
    if (int(year) % 100 == 0):
        if (int(year) % 400 == 0):
            print("Given number is a leap year")
        else:
            print("Given number is not a leap year")
    elif (int(year) % 4 == 0):
        print("Given number is a leap year")
    else:
        print("Given number is not a leap year")
else:
    year = int(input("Enter any year from 1000: "))
