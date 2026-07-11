def cal_avg(a,b,c):
    sum= a+b+c
    avg= sum/3
    print(avg)
    return(avg)

q= int(input("Give us your marks in sst: "))
w= int(input("Give us your marks in eng: "))
e= int(input("Give us your marks in pbi: "))

cal_avg(q,w,e)

cities= ['karachi','lahore','islamabad','quetta','peshawar']

def print_length(cities):
    for items in cities:
        print(items, end=" ")
print_length(cities)
    

# odd even checker
def odd_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")

num = int(input("Enter a number to check if its odd or even: "))
odd_even(num)

#recursion
def show(n):
    if n==0:
        return 
    print(n)
    show(n-1)

show(12)

# currency converter 
def currency_converter(amount, rate):
    converted_amount = round (amount * rate)
    return converted_amount

currency = input("Enter the currency you want to convert to (USD or  EUR): ")
amount = float(input("Enter the the amount you want to convert into INR: "))
if currency == "USD":
    rate= 95
elif currency == "EUR":
    rate= 108
print(f" {currency} is: {currency_converter(amount, rate)}")
print (" Remember \n This amount is a rounded off value \n An approximate value")

#call stack
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def calc_sum(n):
    if n==0:
        return 0 
    else:
        return n+ calc_sum(n-1)
    
sum= calc_sum(5)
print("The sum of numbers till n is : ",sum)
    
#proper calculator
import time
print("We will perform Calculations now")
time.sleep(2)
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return round(num1 / num2 )
    else:
        return "Invalid operator"
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("Result:", result)

#temperature converter
def temp_convt(temp, unit):
    if unit == "C" or unit == "c":
        return(temp * 9/5 + 32)
    elif unit == "F" or unit == "f":
        return (temp - 32) * 5/9
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

temp= float(input("Enter the temperature you have: "))
unit= input("And Whats the unit you want to convert into? (C or F): ")
final_temp= temp_convt(temp, unit)
print(f"Your temperature is: {round(final_temp, 2)} {unit.upper()}")