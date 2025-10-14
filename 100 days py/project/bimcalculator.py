weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Convert height to meters
height_m = height / 100

# Calculate BMI
BMI = weight / (height_m ** 2)  

print("Your BMI is : ", round(BMI, 2)) #here is 2 means  ensures that the BMI value is displayed with two digits after the decimal point. 