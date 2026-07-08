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
