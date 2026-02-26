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
h=0
pet.clean = "clean" 
c=10
pet.energy = "high"
e=10
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
l=0
sp = random.randint(1,10)
st = random.randint(1,10)
si = random.randint(1,10)
pet.speed = sp
pet.strength = st
pet.size = si
pet.age = 0
a=0
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
if action == 1:
    print(pet.hungry)
elif action == 2:
    print(pet.energy)
elif action == 3:
    print(pet.love)
elif action == 4:
    print(pet.hp)
elif action == 5:
    print(pet.clean)
elif action == 6:
    print(pet.speed)
elif action == 7:
    print(pet.strength)
elif action == 8:
    print(pet.size)
elif action == 9:
    print(pet.age)
elif action == 10:
    h=h+5
    e=e-1
elif action == 11:
    l=l+5
    e=e-1
elif action == 12:
    c=c+5
    e=e-1
elif action == 13:
    sp=sp+5
    e=e-3
elif action == 14:
    st=st+5
    e=e-3
elif action == 15:
    "this is visiting the vet i need to figure out what to do about this"
elif action == 16:
    a=a+1
    e=e+5