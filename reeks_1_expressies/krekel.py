aantal = int(input())

def berekenFahrenheit(aantal):
        fahrenheit = 50 + ((aantal - 40) / 4)
        return fahrenheit

def berekenCelsius(aantal):
        celsius = 10 + ((aantal - 40) / 7)
        return celsius

print(f'temperatuur (Fahrenheit): {berekenFahrenheit(aantal)}')
print(f'temperatuur (Celsius): {berekenCelsius(aantal)}')