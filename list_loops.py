songs = ["ROCKSTAR", "Do It", "For The Night"]

# print first and last element of songs list
print(songs[0])
print(songs[2])

# print using slice
print(songs[1:])

# update laste element in songs list
songs[2] = "Man on the Moon"

# add 3 songs to songs list
songs.extend(["Maan", "New York Soul", "Above the Storm"])

# delete second song in list
del songs[1]

for song in songs:
    print(song)

for i in range(len(songs)):
    print(songs[i])


animals = ["Cat", "Dog", "Turtle"]

# add another animal to list
animals.append("Giraffe")

# print 3rd animal of list
print(animals[2])

# delete first animal
del animals[0]

# print animals list with for loop
for animal in animals:
    print(animal)