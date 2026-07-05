print("Welcome to your first python program")
name = "ujjwal"
age = 17
prodduct= 56.3
print("my name is ",name)
a= 2
b=5
sum= a + b
print(sum)
print(prodduct - age)
#we are getiing stared with python
a2= 5
b2= 2
print(a2*b2)
print(a2/b2)
print(a2-b2)
print (a2%b2)
print(a2**b2)
#relational
print(a == b)
print(a != b)
print(a >= b)
print(a<= b)
#assignment
num= 22
num= 20+num
print("num:",num)
num *= 5
print(num)
#logical 
print(not False)
print(not True)
print(not a2 >b2)
val1=True
val2=False
print("life is:", val1 and val2)
print("or operator:", val1 or val2)
#type casting
c=3.4
d= int("7")
print(c+d)
#input
who=input("who are you?")
print("Nice to meet you",who)
print(type(who),b)
agw= input("what is your age man? ")
print(agw,"? really?.....suspicious")

#programme1
print("lets get total of two numbers, Give me two")
number1= int(input("Whats the first number?: "))
number2= int(input("And whats the second one?: "))
sum= number1+number2
print("Here you go , its", sum )

#programme2
print("What if we just find the area of the rectangle")
print("Ready?")
length= int(input("whats the length?: "))
print("ohkkey so its", length)
breadth= int(input("Whats the breadth then?: "))
area= length*breadth
print("so", length, "is length and", breadth, "is breadth")
print("mhmm....so the area of the rectangle you have is", area," meter" )

#programme3
print("do you wanna know average of your subjects? if yes then go on")
marks1= int(input("so from first subject?: "))
print("ohkkey i see", marks1)
marks2= int(input("and the next subject goes here: "))
average= marks1+marks2
avg= average/2
print("so your average should be:", avg)

#programme4
print("lets get some percentage now")
salary1= int(input("whats the salary of person one? :"))
salary2= int(input("whats the salry of person 2?: "))
print("silly", salary2)
salary3= int(input("and person3?: "))
salary4= int(input("must be a fourth one right?: "))
totalsal= salary1+salary2+salary3+salary4
salary= input("which person's salary percentage you wanna know? ")
if salary=="person1": choosen_salary=salary1
elif salary=="person2": choosen_salary=salary2
elif salary=="person3": choosen_salary=salary3
elif salary=="person4": choosen_salary=salary4
else:
    print("invaild choice")
percent= choosen_salary / totalsal *100
print("there you go, the one you mentioned gets", percent, "percent of the total funds assigned")

#programme5
print("Getting area of some square is easy but lets still")
side=int(input("length of any one side?"))
areasquare= side*side
print("so the are of the square you have is", areasquare, "meters")