age= int(input("Whats your age?: "))
if(age>=18):
    print("You are an adult and you can Vote!")
    print("and yes , you can drive too!")
if(age>=18):
    life= str(input("How's life going as an adult though?"))
    print("hmm....i seee")
elif(age<18):
    print("Nahh, this programme aint meant for you")
    print("You're Just a kid")

marks= int(input("Scores in Maths: "))
if(marks>=90):
    print("Grade A+")
elif(marks>80):
    print("Grade A")
elif(marks>=70):
    print("Grade B")
elif(marks>60):
    print("Grade C")     

#programme  
numm= int(input("gimme a number and i'll telll you if its even or odd: "))
rem= numm % 2
if(rem==0):
    print("the number is even for sure")
else: 
    print("the number is odd though....")

#programme
print("now i'll give you the greatest from three numbers you tell! ")
a= int(input("enter number1: "))
b= int(input("enter number2: "))
c= int(input("enter number3: "))
if(a>b>c):
    print(a,b,c)
elif(b>c>a):
    print(b,c,a)
elif(c>b>a):
    print(c,b,a)
elif(a>c>b):
    print(a,c,b)
elif(b>a>c):
    print(b,a,c)

# validation of username
user_name= input("Enter your username: ")
if len(user_name)>12:
    print("username is too long")
elif len(user_name)<6:
    print("username is too short")
elif type(user_name)==int:
    print("username cannot be a number")
elif user_name.isalpha()==False:
    print("username cannot contain symbols")
else:
    print(user_name, "is set to be your username")