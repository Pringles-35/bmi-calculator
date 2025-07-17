#BMI CALCULATOR
print("BMI calculator")
while True:
 question=input("Do you want to check your BMI?:")

 
 if question.lower()=="no":
    print("goodbye!")
    break

 elif question=="yes":
    

  weight=float(input("Enter your weight in kg:"))
  height=float(input("Enter your height in m:"))

  BMI=weight/(height**2)
  BMI=round(BMI,2)
  output= f"Your BMI is:{BMI}"

  print(output)

  if BMI<18.5:
             print("you are underweight")
  elif 18.5 <=BMI <24.9:
             print("normal weight")
  elif 25 <= BMI <29.9:
             print("overweight")
  else:
    print("fattie")

 else:
    print("please answer yes or no")
    
