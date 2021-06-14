f_name = input("What's your first name?: ")
l_name = input("What's your last_name?: ")
course = input("Name of your course?: ")
students = int(input("How many students are there in you class:? "))



print(f'My name is {f_name}, and my last name is {l_name}.\nI am participating in the course {course}.\nThere are {students} candidates taking the course ')

print("My name is", end= " ")
print(f_name, end= " ") 
print("with last name", end= " ") 
print(l_name, end= " ")
print("I am participating in the course", end= " ") 
print(course, end= ". ") 
print("There are", end= " ") 
print(students, end= " ") 
print("candidates taking the", end= " ") 
print(course, end= " ") 
print("course.")