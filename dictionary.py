dic = {
    "key" : "value",
    "name" : "shardha"
}
print(dic)
#empty dictionary
null ={}
null["name"] = "harbans"
print(null)
#nested dictionary
student = {
    "name" : "harbans",
    "contact" :{
        1: 12345,
        2:155464,
        3:547542,
    }
}
print(student["contact"][2])
print(len(list(student.keys())))
print(student.values())
print(student.items())
print(student.get("name"))

