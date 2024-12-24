import math
nb_people = input("How many people need a ride ?")
nb_Ptf = input("How many people fit in one taxi?")
print("Number of taxis needed:",math.ceil(int(nb_people)/int(nb_Ptf))
)
