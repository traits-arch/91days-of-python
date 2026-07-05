# set have no repeated values and elements are immutable 
#cannot store lists or dict in them
collection= {1,2,5,3,8, "Hello", "World", 2.99, 5}
print(type(collection))
print(collection)
print(len(collection))# double values get ignored
coll= set() # important to create an empty set
coll.add(21)
coll.add(34)
coll.add(59)#add an el
print(coll)
coll.remove(34)#remove an element
print(coll)
print(len(coll))
coll.pop()
print(coll)
coll.clear()#empties the set
print(coll)

set1= {1,2,3,2,1}
set2= {2,3,4,5,1}

print(set1.union(set2))#gives unique
print(set1.intersection(set2))#gives common

#programme 1
dictt= {
    "table": "a peice of furniture" "list of facts & figures",
    "cat": "a small animal"
}
print(dictt)

#prorgramme 2
set_sub= {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(set_sub), "Classrooms are needed")

sub_marks= {}
sub= str(input("Enter Subject: "))
marks= int(input("Enter Marks: "))
sub_marks.update({sub:marks})
print(sub_marks)
sub2= str(input("Enter Subject: "))
marks2= int(input("Enter Marks: "))
sub_marks.update({sub2:marks2})
print(sub_marks)
sub3= str(input("Enter Subject: "))
marks3= int(input("Enter Marks: "))
sub_marks.update({sub3:marks3})
print(sub_marks)

#p3
set2= {2,4,7,5,3,'7.0'}
print(set2)


