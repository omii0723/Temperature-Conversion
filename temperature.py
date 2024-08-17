def convert_temperature(value, unit):
    if unit.upper() == 'C':
        celsius = value
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
    elif unit.upper() == 'F':
        fahrenheit = value
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
    elif unit.upper() == 'K':
        kelvin = value
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
    else:
        return "Invalid unit entered."

    return celsius, fahrenheit, kelvin

# Input from the user
value = float(input("Enter temperature value: "))
unit = input("Enter original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")

# Convert the temperature
celsius, fahrenheit, kelvin = convert_temperature(value, unit)

# Display the results
print("\nConverted Temperatures:")
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")
