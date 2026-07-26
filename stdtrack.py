stds= {
    
}
colour="red"
def std_add(Name):
            global stds
            Grade = input("Class: ")
            roll_no= input("Roll no: ")
            Session= input("Session: ")
            stds= {Name:{"class: ": Grade,
                          "roll no: ": roll_no,
                          "session: ": Session}}
            English=int(input("Enter Marks in English: "))
            Physics=int(input("Enter Marks in Physics: "))
            Chemistry=int(input("Enter Marks in Chemistry: "))
            Maths=int(input("Enter Marks in Maths: "))
            Biology=(input("Enter Marks in Biology: "))
            Computer_Science=int(input("Enter Marks in Computer Science: "))
            Marks={"English: ":English,
                   "Physics: ":Physics,
                   "Chemistry: ":Chemistry,
                   "Maths: ":Maths,
                   "Biology: ":Biology,
                   "Computer Science: ":Computer_Science,}
            stds[Name]["Marks"]=Marks             
import time
time.sleep(1)
print("-----Welcome to Student Dashboard-----")      
time.sleep(1)                       
print("Choose one of the options: ")
print("1. Add a Student\n2. Check Average\n3. Find a student\n4. Show All\n5. Find the topper\n6. Exit")
option=int(input("Choose one(1-6): "))
if option==1:
       name=input("Enter the name of the student: ") 
       std_add(name)     
elif option==2:
        pass                        
elif option==3:
        pass
elif option==4:
        pass
elif option==5:
        pass
elif option==6:
        pass
else:
        print("Invaild input, Please choose between (1-6)")
                    
print(stds)                              
                                
            