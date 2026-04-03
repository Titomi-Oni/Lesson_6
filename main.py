# 1) Ask the user to enter their height in centimeters and store it in `height`.
height = float (input("Enter your height in cm:"))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight = float (input("Enter your weight in kg:"))
# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.
BMI = weight/(height/100)**2
# 4) Print the BMI value.
print ("BMI value:",BMI)
# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Elif if BMI is 24.9 or less → print "healthy"
#    - Elif if BMI is 29.9 or less → print "over weight"
#    - Elif if BMI is 34.9 or less → print "severely over weight"
#    - Elif if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"
if BMI<=18.4:
    print ("Underweight")
elif BMI<=24.9:
    print ("Healthy")   
elif BMI<=29.9:
    print ("Overweight") 
elif BMI<=34.9:
    print ("Severely Overweight")
elif BMI<=39.9:
    print ("Obese")
else: 
    print ("Severely Obese")