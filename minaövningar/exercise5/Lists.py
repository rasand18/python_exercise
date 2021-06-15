#a
students = ['Rasmus','Susan','Fredrik','Aleksis','Tonje']
#b
print(students[2])
#c
print(students[2][0])
#d
students[2]='Ole'

#e
students[2] += ' Nordmann'
#f
students.append('Johan')
#g

students.insert(4,'Monty Python')
print(students)

#h
print(len(students))
students.remove('Ole Nordmann')
print(len(students))

#i
print(students.index('Monty Python'))

#j
print(students[0:3])

#k 
student_r = students[::-1]
print(student_r)

#i
students_even = students[::2]
print(students_even)

#m
students_odd = students[1::2]
print(students_odd)




