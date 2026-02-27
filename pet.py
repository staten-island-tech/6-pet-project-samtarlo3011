import time
import random
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
health=50
pet.hp = health
pet.hungry = "low"
h=0
pet.clean = "clean" 
c=10
pet.energy = "high"
e=10
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
ag=0
pet.speed = sp
pet.strength = st
pet.size = si
pet.age = ag
a=0
name=input("""name your pet!
""")
""" print(pet.hp,pet.hungry,pet.clean,pet.energy,pet.gender,pet.species,pet.love,pet.speed,pet.strength,pet.size,pet.age) """
pets = []
pets.append(name)
def basic_action():
    global h
    global c
    global e
    global l 
    global sp
    global st
    global a
    global ag
    global health
    while pet.age<5:
        action=int(input("""what action would you like to perform?
    1.check pet hunger
    2.check pet energy level
    3.check pet affection level
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
    16.go to sleep for the night
    """))
        abcd=0
        if action == 1:
            print("hunger=")
            print(pet.hungry)
        elif action == 2:
            print("energy=")
            print(pet.energy)
        elif action == 3:
            print(pet.love)
            print("love=")
        elif action == 4:
            print("hp=")
            print(pet.hp)
        elif action == 5:
            print("cleanlieness=")
            print(pet.clean)
        elif action == 6:
            print("speed=")
            print(pet.speed)
        elif action == 7:
            print("strength=")
            print(pet.strength)
        elif action == 8:
            print("size=")
            print(pet.size)
        elif action == 9:
            print("age=")
            print(pet.age)
        elif action == 10:
            print("hunger decreased!")
            h=h-5
            e=e-1
            c=c-1
            l=l+2
        elif action == 11:
            print("affection increased!")
            l=l+5
            e=e-1
            h=h+1
            c=c-1
        elif action == 12:
            print("cleanlieness increased!")
            c=c+5
            e=e-1
            h=h+1
            l=l-2
        elif action == 13:
            print("speed increased!")
            sp=sp+5
            e=e-3
            h=h+2
            c=c-2
            l=l+1
        elif action == 14:
            print("strength increased!")
            st=st+5
            e=e-3
            h=h+2
            c=c-2
            l=l+1
        elif action == 15:
            "this is visiting the vet i need to figure out what to do about this"
        elif action == 16:
            print("Goodnight! (energy restored)")
            a=a+1
            e=e+5
            h=h+3
            c=c-1
        elif action == 17:
            a = int(input("enter here "))
        time.sleep(3)
        print (a)
        if a >= 365 and a < 730:
            ag=1
        elif a >= 730 and a < 1095:
            ag=2
        elif a >= 1095 and a <1460:
            ag=3
        elif a >= 1460 and a <1825:
            ag=4
        elif a >= 1825 and a <2190:
            ag=5
        print (ag)
        pet.age = ag
        if c <= 3:
            pet.clean = "low"
        elif c >3 and c <7:
            pet.clean = "medium"
        elif c <= 0:
            pet.clean = "critically low (stinky boy)(will start losing hp)"
            health=health-3
        elif c >=7:
            pet.clean = "high"
        elif c >10:
            pet.clean = "stunningly clean"
        if h <= 3 and h > 0:
            pet.hungry = "low"
        elif h >3 and h <7:
            pet.hungry = "medium"
        elif h <= 0:
            pet.hungry = "stuffed"
        elif h >=7 and h < 10:
            pet.hungry = "high"
        elif h >=10:
            pet.hungry = "starving (losing hp)"
            health=health-3
        pet.hp = health
        if e <= 3 and e > 0:
            pet.energy = "low"
        elif e >3 and e <7:
            pet.energy = "medium"
        elif e <= 0:
            pet.energy = "critically low (sleepy boy)(will start losing hp)"
            health=health-3
        elif e >=7 and e <10:
            pet.energy = "high"
        elif e >=10:
            pet.energy = "bright eyed and bushy tailed"
        if l <= 3 and l > 0:
            pet.love = "low"
        elif l >3 and l <7:
            pet.love = "medium"
        elif l <= 0:
            pet.love = "in love"
        elif l >=7 and l < 10:
            pet.love = "high"
        elif l >=10:
            pet.love = "hates you"
        pet.hp = health
def of_age():
    global name
    print("Congratulations!! You have successfully kept your pet",(name),"alive for five whole years! This means that you have unlocked some brand new activities. You can now access the shop to buy new pets. You can take your pets to shows to test thier strength and speed against others or you could force your pets to work in factories! The world is your oyster! Have fun!") 
    action=int(input("""what action would you like to perform?
    1.check pet hunger
    2.check pet energy level
    3.check pet affection level
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
    16.go to sleep for the night
    17.visit the shop
    18.go to a strength show
    19.go to a speed show
    
    """))
basic_action()
of_age()