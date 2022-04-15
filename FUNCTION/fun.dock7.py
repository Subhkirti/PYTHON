def calculate(bmi):
    if bmi<=18.5:
        return "Underweight"
    if bmi<=25.0:
        return "Normal"
    if bmi<=30.0:
        return "overweight"
    if bmi>30:
        return "obese"
bmi=int(input("enter:"))
print(calculate(bmi))


