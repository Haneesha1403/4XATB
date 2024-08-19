#Create a program, take 2 inputs from user num1, num2 and give them max, pow,sub,add,mul, div and format your outpu with f{""}




num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
result= max((num1,num2))
print("Maximum of "f"{num1} and "f"{num2} is:", max(num1,num2))
print ("sum of "f"{num1} and "f"{num2} is:", num1+num2)
print ("Substraction of "f"{num1} and "f"{num2} is:", num1-num2)
print ("Multiplication of "f"{num1} and "f"{num2} is:", num1*num2)
print ("division of "f"{num1} and "f"{num2} is:", num1/num2)
print("power of "f"{num1} and "f"{num2} is:", pow(num1,num2))