first_name = 'rasmus'.capitalize()
last_name = 'andreasson'.capitalize()
course = 'Telia data engineer'.lower()
students = '12'
punish = "I will not teach others to fly\n"
numberoft = 9
count = 0
new_punish = punish.replace("will not",'will')
counts = 0

#print(f'My name is {first_name}, with last name {last_name}.\nI am participating in the course {course}.\nThere are {students} candidates taking the course ')


#while (count<9):
    #count = count + 1
    #print(new_punish)
   # if new_punish.find("will"):
        #counts=counts+1
#print(counts)

#print(punish*numberoft)
findword=("will")
print(f"The word {findword}, occurs {(new_punish*numberoft).count(findword)} times")








