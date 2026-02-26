class pet:
    def __init__(self, hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name):
        self.hp = hp 
        self.hungry = hungry
        self.clean = clean
        self.energy = energy
        self.gender = gender
        self.species = species
        self.love = love
        self.production = production
        self.speed = speed
        self.strength = strength
        self.size = size 
        self.age = age 
        self.name = name
pet.hp = 100
pet.hungry = "low"
pet.clean = "clean" 
pet.energy = "high"
import random
g=random.randint(1,2)
if g == 1:
    pet.gender = "male"
else:
    pet.gender = "female"
want = int(input("""would you like a " 
"1:Dog"
"2:Cat"
"3:Frog"
"4:Lizard"
"5:Bird
"""))
if want == 1:
    pet.species = "Dog"
elif want == 2:
    pet.species = "Cat"
elif want == 3:
    pet.species = "Frog"
elif want == 4:
    pet.species = "Lizard"
elif want == 5:
    pet.species = "Bird"
pet.love = 0
sp = random.randint(1,10)
st = random.randint(1,10)
si = random.randint(1,10)
pet.speed = sp
pet.strength = st
pet.size = si
pet.age = 0
name=input("""name your pet!
""")
""" print(pet.hp,pet.hungry,pet.clean,pet.energy,pet.gender,pet.species,pet.love,pet.speed,pet.strength,pet.size,pet.age) """
pets = []
pets.append(name)
if  pet.age<5:
    action=int(input("""what action would you like to perform?
1.check pet hunger
2.check pet energy level
3.check pet love level
4.check pet hp
5.check pet cleanlieness
6.check pet speed
7.check pet strength
8.check pet size
9.check pet age
10.feed pet
11.pet pet
12.bathe pet
13.train pet speed
14.train pet strength
15.visit the vet
16.go to sleep for the night"""))
