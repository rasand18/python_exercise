

captured = ('pikachu','pidgey','abra','pidgey','eevee','pidgey')

#x = captured.count('pidgey')
#print(x)

#D

User_input  = input("Type a Pokémon name: ")

if (User_input in captured):
    print("The pokemon is captured")
else: 
    print("The pokemon dosent exist in Ash collection")

print(f'The total number of the pokemons that he catched is {len(captured)}')

my_set = set(captured)

print(f'The total number of unique pokemons is: {len(my_set)}')


