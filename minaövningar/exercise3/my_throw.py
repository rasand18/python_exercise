import math

degrees  = float(input("Enter the degree: "))
velocity = float(input("Enter velocity: "))
throw_height = float(input("Enter throw_height: "))

angle_radians=math.radians(degrees)
throw_velocity = velocity/3.6
horz_velocity = velocity*math.cos(angle_radians)
verti_velocity = velocity*math.sin(angle_radians)
air_time = (verti_velocity+ math.sqrt(verti_velocity**2+2*9.81*throw_height))/9.81
throw_distance = horz_velocity*air_time 

print(f"The angle is {angle_radians}\n, the velocity: {throw_velocity}\n, the veolocity horz: {horz_velocity}\n, the velocity verti: {verti_velocity}\n, the air time: {air_time}\n and the throwing distance: {throw_distance}")
