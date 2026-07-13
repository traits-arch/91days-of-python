str1 ='its a string......, not the next line '
str2= "anotherstring"
str3= """yepp , this too"""
str4= "heloo everyone \n its the next line"
print(str1)
print(str4)
str5= str1+str4
print(str5)

len1=len(str2)
print(len1)
len2=len(str5)
print(len2)

str6= "index building"
index= str6[0]
print(index)
print(str6[0:6])
print(str6[6:len2])#fill to the length
print(str6[:6])#fill what comes before that
print(str6[6:])#fill to the end 
 
#slicing:works with negatives too
str7= "Apple"
print(str7[-3:-1])#runs as number line does 

#String Function 
string= "studying python in vs"
#if they end with something
print(string.endswith("ege"))
print(string.endswith("vs"))
#capitalize first letter of a word 
print(string.capitalize())#only creates new one
print(string)
string= string.capitalize() #now they hold the same value
print(string)
#replace
string2= "it is reilly fun"
print(string2.replace("i", "a"))# ("old", "new")
#find
string3= "its cool again"
print(string3.find("cool"))
print(string3.find("cell"))#doesn't exist so it assigns it to -1
#negative indexes never really exist until we assign them
#count
print(string3.count("cool"))

#progrmme 1
user_name= str(input("Whats your first name?: "))
print("ohh so you name is of", len(user_name), " letters")

#programme2
symbols_write= str(input("so put some dollar symbols and let me guess how many they are: "))
print("so there's", symbols_write.count("$"), "number of dollars")