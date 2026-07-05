for i in range (2, 100, 2):
    print(i)

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
                   