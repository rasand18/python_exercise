

def say_my_name():
    f_name = input("What's your first name?: ").capitalize()
    l_name = input("What's your last_name?: ").capitalize()
    course = input("Name of your course?: ").lower()
    students = int(input("How many students are there in you class:? "))
    
    print(f'My name is {f_name}, and my last name is {l_name}.\nI am participating in the course {course}.\nThere are {students} candidates taking the course ')
    


say_my_name()
""" Gives the user 4 inputs to enter, first_name, last_name, name of the couse they are attending and how many there are in their class. In the end it prints it all"""