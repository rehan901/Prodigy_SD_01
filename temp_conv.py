unit = input("Choose the unit to convert in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C" or "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is : {temp}F")
elif unit == "F" or "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is : {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement.")