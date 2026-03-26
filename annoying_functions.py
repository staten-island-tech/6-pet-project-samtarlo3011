import time
import random
pets=[]
petsN=[]
class store:
    def __init__(self,speed,strength,size,gender,species):
        self.speed=speed
        self.strength=strength
        self.size=size
        self.gender=gender
        self.species=species
    def storepets():
        speed = random.randint(1,10)
        strength = random.randint(1,10)
        size = random.randint(1,10)
        g=random.randint(1,2)
        if g == 1:
            gender = "male"
        else:
            gender = "female"
        want = random.randint(1,5)
        if want == 1:
            species = "Dog"
        elif want == 2:
            species = "Cat"
        elif want == 3:
            species = "Frog"
        elif want == 4:
            species = "Lizard"
        elif want == 5:
            species = "Bird"
        return(store(speed,strength,size,gender,species))
class pet:
    def __init__(self, hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag,):
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
        self.money = money
        self.h=h
        self.c=c
        self.e=e
        self.l=l
        self.a=a
        self.ag=ag
    def New_Pet(gender,species,speed,strength,size):
        global pets
        global petsN
        h=0
        c=10
        e=10
        l=0
        if speed == 0:
            speed = random.randint(1,10)
            strength = random.randint(1,10)
            size = random.randint(1,10)
        a=0
        ag=0
        if gender == 0:
            g=random.randint(1,2)
            if g == 1:
                gender = "male"
            else:
                gender = "female"
        if species == 0:
            want = int(input("""would you like a " 
            "1:Dog"
            "2:Cat"
            "3:Frog"
            "4:Lizard"
            "5:Bird
            """))
            if want == 1:
                species = "Dog"
            elif want == 2:
                species = "Cat"
            elif want == 3:
                species = "Frog"
            elif want == 4:
                species = "Lizard"
            elif want == 5:
                species = "Bird"
        money=100
        hp=50
        hungry="low"
        clean="clean"
        energy="high"
        love=0
        age=ag
        production=0
        name=input("""name your pet!
""")
        petsN.append(name)
        pets.append(pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag))
        return pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag)
    
    def petstore():
        store1=store.storepets()
        store2=store.storepets()
        store3=store.storepets()
        store4=store.storepets()
        store5=store.storepets()
        storelist = [
        {"id" :1, "species" : store1.species,"strength" : store1.strength,"speed" : store1.speed,"size" : store1.size,"gender" : store1.gender,},
        {"id" :2, "species" : store2.species,"strength" : store2.strength,"speed" : store2.speed,"size" : store2.size,"gender" : store2.gender,},
        {"id" :3, "species" : store3.species,"strength" : store3.strength,"speed" : store3.speed,"size" : store3.size,"gender" : store3.gender,},
        {"id" :4, "species" : store4.species,"strength" : store4.strength,"speed" : store4.speed,"size" : store4.size,"gender" : store4.gender,},
        {"id" :5, "species" : store5.species,"strength" : store5.strength,"speed" : store5.speed,"size" : store5.size,"gender" : store5.gender,},
        ]
        for i in storelist:
            print("id:",i["id"],",","species:",i["species"],",","strength:",i["strength"],",","speed:",i["speed"],",","gender:",i["gender"])
        want=int(input("enter the id of what pet you would like to buy. If no pet is wanted enter 6: "))
        if want in range(1,7):
            if want == 6:
                print("return")
            for i in storelist:
                if want == i["id"]:
                    print("congrats on purchasing a new", i["species"], "thatll be $20!")
                    newP=pet.New_Pet(i["gender"],i["species"],i["speed"],i["strength"],i["size"])
        else:
            print("please enter a valid id")
def choose_petO():
    print("Congratulations!! You have successfully kept your pet",(pet1.name),"alive for five whole years! This means that you have unlocked some brand new activities. You can now access the shop to buy new pets. You can take your pets to competitions to test thier strength and speed against others or you could force your pets to work in factories! The world is your oyster! Have fun!") 
    for i in range(95):
        choice= input("which pet would you like to access? ")
        if choice not in petsN:
            print("no pet found")
            choose_petO()
        else:
            for i in pets:
                if choice == i.name:
                    i.of_age()          

pet1 = pet.New_Pet(0,0,0,0,0)
pet.petstore()
print(pets,petsN)
choose_petO()
