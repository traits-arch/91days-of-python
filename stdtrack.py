stds= {
    
}
import time
colour="red"
def std_add(Name):
            global stds
            Grade = input("Class: ")
            roll_no= input("Roll no: ")
            Session= input("Session: ")
            stds= {Name:{"Class: ": Grade,
                          "roll no: ": roll_no,
                          "session: ": Session}}
            try: English=int(input("Enter Marks in English: "))
            except ValueError:
              print("INVALID INPUT")
            try: Physics=int(input("Enter Marks in Physics: "))
            except ValueError:
                           print("INVALID INPUT")
            try: Chemistry=int(input("Enter Marks in Chemistry: "))
            except ValueError:
                          print("INVALID INPUT")
            Maths=int(input("Enter Marks in Maths(press enter for N/A): "))
            if Maths == "":
                    Maths=="N/A"
            Biology=(input("Enter Marks in Biology(press enter for N/A): "))
            if Biology == "":
                                Biology=="N/A"
            try: Computer_Science=int(input("Enter Marks in Computer Science: "))
            except ValueError:
                          print("INVALID INPUT")
            Marks={"English: ":English,
                   "Physics: ":Physics,
                   "Chemistry: ":Chemistry,
                   "Maths: ":Maths,
                   "Biology: ":Biology,
                   "Computer Science: ":Computer_Science,}
            stds[Name]["Marks"]=Marks             
def std_avg(Student):
        for Student in stds:
                pass

        

def dash():
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
                Student = str(input("Name of the student: "))
                std_avg(Student)
                pass                        
        elif option==3:
                Student = str(input("Name of the student: "))
                if Student in stds:
                        print("Student is Found in ",)
                        print(Student)
                        

        
                        pass
        elif option==4:
                pass
        elif option==5:
                pass
        elif option==6:
                pass
        else:
                print("Invaild input, Please choose between (1-6)")
dash()                   
print(stds)  
sarg=input("(a) Repeat or (b) Exit")  
if sarg=="a":
        dash() 
else:
        pass 
