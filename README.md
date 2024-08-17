Temperature Conversion Program
Description
This program allows users to convert a temperature value between three different units: Celsius (C), Fahrenheit (F), and Kelvin (K). The user inputs the temperature value and its original unit, and the program calculates and displays the equivalent temperatures in the other two units.

Features
Celsius to Fahrenheit and Kelvin conversion
Fahrenheit to Celsius and Kelvin conversion
Kelvin to Celsius and Fahrenheit conversion
Simple user input and output
Validates user input for the temperature unit
How It Works
User Input:

The user is prompted to enter a temperature value.
The user is then asked to specify the original unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin).
Conversion Logic:

Based on the unit provided, the program performs the appropriate conversion using the following formulas:
Celsius to Fahrenheit: ( F = \frac{C \times 9}{5} + 32 )
Celsius to Kelvin: ( K = C + 273.15 )
Fahrenheit to Celsius: ( C = \frac{F - 32 \times 5}{9} )
Kelvin to Celsius: ( C = K - 273.15 )
Other conversions are derived from these primary formulas.
Output:

The program outputs the converted temperature values in Celsius, Fahrenheit, and Kelvin.
If an invalid unit is entered, the program returns an error message.
Usage
Prerequisites
Python 3.x
Running the Program
Clone or download the script.

Run the script using a Python interpreter:

python temperature_conversion.py
Follow the on-screen prompts to enter the temperature value and the unit.

The program will display the converted temperatures.

Example
If the user enters 100 for the temperature value and C for the unit:

Enter temperature value: 100
Enter original unit (C for Celsius, F for Fahrenheit, K for Kelvin): C
The program will output:

Converted Temperatures:
Celsius: 100.0
Fahrenheit: 212.0
Kelvin: 373.15
Error Handling
The program checks for invalid temperature units and returns an appropriate error message if the input does not match 'C', 'F', or 'K'.
Contributing
Feel free to fork this repository and submit pull requests. If you find any bugs or have suggestions for improvements, please create an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

This README file provides a comprehensive overview of the program, how it works, and how to use it. You can modify or expand upon this based on your specific requirements or additional features.
