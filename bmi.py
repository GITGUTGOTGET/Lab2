def calculate_bmi():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    BMI = weight / (height / 100) ** 2

    print(f"You BMI is {BMI}")
    if BMI<18.5:
        print("UnderWeight")
    elif 18.5<BMI<25.0:
        print("NormalWeight")
    elif BMI>25.0:
        print("OverWeight")

calculate_bmi()

