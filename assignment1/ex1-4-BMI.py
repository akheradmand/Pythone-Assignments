print("Welcome user")
print("We want to calculate your BMI(Body Mass Index)")

weight= float(input("Please enter your weight(kg): "))
height= float(input("Please enter your height(m): "))

if weight<=0 or height<=0:
    print("Invalid input")
else:
    BMI=weight/height**2

    if BMI<18.5:
        print("you are Underweight")
    elif BMI>=18.5 and BMI<25:
        print("you are in Normal Weight")
    elif BMI>=25 and BMI<30:
        print("you are Overweight")
    elif BMI>=30 and BMI<35:
        print("you are Obecity")
    elif BMI>=35 and BMI<40:
        print("you are Extreme Obecity")