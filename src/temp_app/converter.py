def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_rankine(celsius):
    kelvin = celsius + 273.15
    return kelvin * 9/5

def rankine_to_celsius(rankine):
    kelvin = rankine * 5/9
    return kelvin - 273.15

if __name__ == "__main__":
    print("Temperature Converter Tests")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"0°C = {celsius_to_kelvin(0)}K")
    print(f"0°C = {celsius_to_rankine(0)}°R")
    print(f"491.67°R = {rankine_to_celsius(491.67)}°C")
