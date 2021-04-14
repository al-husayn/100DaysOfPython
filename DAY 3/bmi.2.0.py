# Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f" Your BMI is {bmi} and You are Underweight")
elif bmi < 25:
    print(f" Your BMI is {bmi} and You are normal weight")
elif bmi  < 30:
    print(f" Your BMI is {bmi} and You are Over weight")
elif bmi  < 35:
    print(f" Your BMI is {bmi} and You are Obese")
else:
    print(f" Your BMI is {bmi} and You are clinically Obese")


