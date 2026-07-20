#class
class student:
      def __init__(self):
            print(self)
      name= "Omar Pal"

#object
s1= student()
print(s1)

class std: 
      def __init__(self, name, marks, year):
            self.name = name 
            self.marks = marks 
            self.year = year 

std1= std("karan",88,2025)
print("Name is: ", std1.name, "\nMarks: ", std1.marks, "\nYear: ",std1.year)    
std2= std("raj",92,2025)
print("Name is: ", std2.name, "\nMarks: ", std2.marks, "\nYear: ",std2.year)          