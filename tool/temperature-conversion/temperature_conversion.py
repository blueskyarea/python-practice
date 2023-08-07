def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    try:
        print("Temperature Conversion Tool")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("{} Celsius is {} Fahrenheit.".format(celsius, fahrenheit))
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("{} Fahrenheit is {} Celsius.".format(fahrenheit, celsius))
        elif choice == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print("{} Celsius is {} Kelvin.".format(celsius, kelvin))
        elif choice == 4:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print("{} Kelvin is {} Celsius.".format(kelvin, celsius))
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")
    except ValueError:
        print("Invalid input. Please input a valid number.")
