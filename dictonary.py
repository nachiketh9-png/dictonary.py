student={
    "name":"omi",
    "age":22,
    "gender":"male"
}
student

print(student["name"])

student["age"]=24
student["age"]

student["gender"]="female"
student["gender"]

#del
del student["gender"]
student

for key,value in student.items():
  print(key,value)
