punish_t = "I WILL NOT TEACH OTHERS TO FLY\n"
number_of_repitions = 9

punish_t2 = punish_t.replace("NOT","")
print((punish_t2 + "\n")*number_of_repitions)


findword=("WILL")
print(f"The word {findword}, occurs {(punish_t2*number_of_repitions).count(findword)} times")








