import time
kms_covered= 1
while kms_covered<= 3:
    time.sleep(1)
    kms_covered+= 1
    print("race is due")
else:
     print("race is over")

#programme 1
count= 0
while count<=119:
     time.sleep(1)
     count+=1
     print("counting.....",count)
else:
     print("counting is done")
     #count to 1000

#programme 2
down= 60
while down>=1:
     time.sleep(1)
     down-=1
     print('countdown before the world ends...',down)

print('boooom...booom')

#programme3
#to get tables of any number till 10 mulltiples

n= int(input('Gimme a number , you wanna know table of: '))
count=0
while count<=9:
     count+=1
     print(n*count)

#programme4
num_list=[]
print("Now we're going to get some squares")
nl= int(input("Find out squares from: "))
ml= int(input("Till Number: "))
while nl<=ml:
     nl+=1
     num_list.append(nl*nl)
else: print("invaild choice")
print(num_list) #gives a list of squares till

#programme 5
nums = num_list
x = int(input("What Square?: "))
idx = 0
while idx < len(nums)-1:
    print('finding number...', x," at index ",idx)
    if(nums[idx] == x ):
        print('found at index', idx)
        break # stop the loop
    else:
        print('Not Found')
    idx += 1
prop= str(input('Wanna know if these nums are squares/odd or even? (yes or no?): '))
for el in num_list:
        print(el,'is a square')
        if el%2==0:
            print(el,'is also even')
        if el%2!=0 :
            print('but',el,'is not even, its actually odd')
 
#programme 6
#Day = str(input("What day is it?"))
#days= ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
#while Day == days.index[0,1,2,3,4,5,6]:
 #    if(days==days.index(4,5)):
  #        continue #skips the indexes
   #  print('Shitty Workday ')
#else:
 #    print("Yay! Weekends")
   
   
#programme7
i=0
while i<7:
    print('not enough')
    if(i>=4 and i<6):
        print(i,'is mid')
        i+=1
        if(i==6):
         print("i is",i,", Criteria Met")
        continue       # if the criteria is met, it will return to initial line
    print(i,' is still small') #missed if continue is met
    i+=1 #missed

#programme 8 
Days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
xc=1
while xc<2:
    print(' How Weeks are like:')
    var= str(input('What day is it?: '))
    if(var=='Monday' or var=='Tuesday' or var=='Wednesday' or var=='Thursday'):
        print(var,", Shitty Weekday")
        break
    if(var=='Friday'):
       print(var,'huh?....weekend is near')
       break
    if(var=='Saturday' or var=='Sunday'):
       print(var,"Yay!....Finally Weekend")
       print("uhh....but Monday will come again")
       break
    xc+=1    
    if (input!=str) :
      print('invaild output')

for i in range (2, 100, 2):
    print(i)
    #can be used for tables again 
for b in range (7, 70, 7): 
    print(b)  # will print the table of seven
    # range ("to begin with", "to end with", "keep gap of")
#programme 9
for c in range(100, 1, 1):
    print(c)

#using shortcuts 
num = int(input("Enter a number to check if its positive or negative: "))
print ("Postive number" if num>0 else "Negative number")

# minimum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
min_num = a if a < b else b
print("The minimum number is:", min_num)

#programme9
password= "rajatpawar@1977"
attempts= 3
print("Morning Rajat")
time.sleep(1)
print("-----Welcome To The Admin Page-----")
time.sleep(1)
print(" *You have three attempts to log in* ")
time.sleep(1)
while attempts>0:
  print("--------")
  guess= input("Enter Password: ")
  if guess == password:
        print("......")
        time.sleep(1)
        print("((Rajat, You're in))")
        break
  else:
        attempts-=1
        print("Wrong password, You have ",attempts," attempts left to log in")
if attempts==0:
     time.sleep(1)
     print("....too many failed attempts,\n please try again later")

