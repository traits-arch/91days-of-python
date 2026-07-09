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
    