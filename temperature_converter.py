# Temperature Conversion Program

# Get temperature and unit from user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C, F, or K): ").upper()

# Check the unit and convert accordingly
if unit == 'C':
    f = (temp * 9/5) + 32
    k = temp + 273.15
    print(f"{temp}°C is {f}°F and {k}K")
elif unit == 'F':
    c = (temp - 32) * 5/9
    k = c + 273.15
    print(f"{temp}°F is {c}°C and {k}K")
elif unit == 'K':
    c = temp - 273.15
    f = (c * 9/5) + 32
    print(f"{temp}K is {c}°C and {f}°F")
else:
    print("Invalid unit! Please enter C, F, or K.")