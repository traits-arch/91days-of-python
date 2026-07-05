marks= [7, 64, 33, 95, 76]
print(marks)
print(marks[0])
print(marks[1])

#in python, it is possible to store different types of data in one list
student = ["karan", 95.4, 17, "delhi"]
print(student)
string= "flower"
print(string[0])
#here string[0] = y ❌ not possible
#but 
student[0]= "arjun"
print(student) #thats possible now
print(marks[4:])
print(marks[-3:-1])

#list methods (lists are mutable)
list= [3,5,8,2,7]
list.append(6)#add an element
print(list)

list.sort()#sort the contents (done in ascending acc to size)
print(list)

list.sort(reverse=True)# sort in descending
print(list)

listabc= ["arbeteer","betteer","vollar"]
listabc.sort()
print(listabc)#sort acc to alphabet (in ascending)
listabc.sort(reverse=True)
print(listabc)#reverse sorting

#reversing a list overall
list.reverse()
print(list)

#insert an element
list2= [2,3,6,8,5]
list2.insert(1,4)# replace the index element (index-num,the element to replace with)
print(list2)

#remove
#it will remove the first labelled element
list3= [9,5,2,8,4]
list3.remove(2)
print(list3)
#pop (remove an element with thee given index)
list3.pop(3)
print(list3)


#tuples (they are immutable)
tup= (53,22,76,43,)
#tup[0]= 39 (it isnt vaild)
print(tup[0])
tup= ()
print(tup)
tup2= (1,) # comma is neccary if using a single element
print(type(tup2))
tup3= (2,97,4,33)
print(tup3 [1:3])#slicing in tuple
tup4= (3,5,8,1,8,6,)
print(tup4.index(5)) 
print(tup4.count(8))

#programme 1
print("I wanna know more about you...\n  what are some movies you like?")
fav1= str(input("Name of the movie1: "))
fav2= str(input("and movie2: "))
fav3= str(input("last one pls: "))
list5= [fav1,fav2,fav3]
print(list5)

#programme2
movies=[]
print("once again please")
mov1= str(input("enter you fav this time: "))
mov2= str(input("next fav: "))
mov3= str(input("last one: "))
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
movies.sort()
print("Here are they in one place: ",movies)

#programme3
tester=[1,2,3,2,1]
testercopy = tester.copy()
testercopy.reverse()
print(tester.reverse)
if(testercopy == tester):
    print("its a palindrome")
else:
    print("this aint a palindrome dumbo")
    #[1,2,3,2,1] gives its a palindrome while [1,2,3,4,1] doesnt

#programme4
grades= ["A","C","B","A","B","D","A","C"]
sorted_grades=sorted(grades)
grades.count("A")
print(grades.count("A"))
print(sorted_grades)