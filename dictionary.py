#dictionary , anything can be added and replaced or updated execpt tuples
info= {
    "name" : "kailash",
    "class" : "12",
    "roll no" : "24",
    "session": "2026-27",
    "is_student" : True,
    "subjects": ["physics","maths","chemistry","english"]
}

print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
info["name"]= "Ravi" #gets overwrited
print(info)
print(info.keys())
print(info.values())
null={}

null["namee"]= ["Ajit"]
print(null)

students={
    "ajit" :  { 
        "pass":"",
        "chem":78,
        "phy":92,
        "maths":86,
    }#nested
}
print(students)
print(students["ajit"])#to get the nested list
print(list(info.keys()))#to get the list of the keys only
print(len(students))
print(len(null and info))
print(len(list(students.values())))

print(info.items())#ot gett the list of items in a dict
pairs = list(info.items())
print(pairs[1])# to get the value a single item

print(info.get("subject")) #returns none (subjects✔️)
#print(info["subject"]) # while this returns an error

#update
info.update({"city":"Punjab", "age":"18"})# new key & Value is added

#using dict as a recordbook for a showroom
import time
print("All your information is stored here")
time.sleep(1)
records = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "owner": "Patel Mukherjee",
  "mode of payment": "Cash"
}
ask= str(input("What are you looking for?: "))
if ask in records:
  print("Yes, ", ask ," is one of the keys in the record book")
  print("its here as",records[ask])
elif type(ask)!=str:
  print("Invaild input")
else:
  print("No, ", ask ," doesnt exist in the record book")
age= int(input("What age are you btw?: "))
old= 'ohh, so u must be in highschool?' if age<18 and age>14 else  'Ohh, u must be in college then?'
print(old)
inquirer= str(input("Can we ask who's the person to inquire for the records?: "))
records["Inquiry"]= inquirer

menu = {
   "pizza": 150,
   "burger": 100,
   "pasta": 120,
   "soda": 50,
   "fries": 80,
   "salad": 90,
   "noodles":110,
   "ice cream": 70
}
order = []
total = 0
print("--Welcome to our restaurant! Here's our menu:--")
for key, value in menu.items():
    print(f"{key:10} : Rp {value:.2f}")
print("-------------------------------")
while True:
    item = input(str("Select the item you want to order (or type 'done' to finish): ").lower())
    if item == 'done':
        break
    elif item in menu and item not in order:
        order.append(item)
        total += menu[item]
        print(f"{item} added to your order. Current total: Rp {total:.2f}")
    elif item in order:
        print(f"{item} is already in your order. Please select a different item.")
    else:
        print(f"{item} is not on the menu. Please select a valid item.")
print("-------------------------------")
if order:
    print("Your order summary:")
    for item in order:
        print(f"{item:10} : Rp {menu[item]:.2f}")
    print(f"Total amount to pay: Rp {total:.2f}")