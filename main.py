from curses.ascii import isalpha, isblank

## Gathering input from user
print("Inches to centimetres Converter by S-Tolba")
number_in_inch = input("Inch = ")

## Checks if value is a letter or word
if isalpha(number_in_inch) == True:
    print("Error: This value is NOT a number!")
    print("Exiting...")
    exit();

## Conversion
number_in_cm = float(number_in_inch)*2.54 ## 1 in = 2.54 cm

## Final Result
print(f"{number_in_inch} inches is {number_in_cm} centimetres")

## By: S-Tolba
