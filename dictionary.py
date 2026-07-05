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