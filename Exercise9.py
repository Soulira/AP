

cities = []

while True :
    city = input("Enter the city name (To stop just tab):")
    if city:
         cities.append(city)
    else:
        break     

cities.sort(key=len)

for city in cities:
    print("The city"+city+"has ",len(city)," letters, so its population is",len(city)*100000)