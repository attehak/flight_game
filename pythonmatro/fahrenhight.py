fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
##print("Lämpötila Celsius-asteina: " + str(celsius))
print(f"Lämpötila Celsius-asteina: {celsius:6.4f}")