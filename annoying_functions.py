import time
import random
pets=[]
petsN=[]
storeW = 0
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
    def New_Pet(store):
        global pets
        global petsN
        h=0
        c=10
        e=10
        l=0
        sp = random.randint(1,10)
        st = random.randint(1,10)
        si = random.randint(1,10)
        a=0
        ag=0
        g=random.randint(1,2)
        if g == 1:
            gender = "male"
        else:
            gender = "female"
        if store == 1:
            want = random.randint(1,5)
        else:
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
        speed=sp
        strength=st
        size=si
        age=ag
        production=0
        name=input("""name your pet!
""")
        petsN.append(name)
        pets.append(pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag))
        return pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag)
    def petstore():
        storeW=1
        store1=pet.New_Pet(1)
        store2=pet.New_Pet(1)
        store3=pet.New_Pet(1)
        store4=pet.New_Pet(1)
        store5=pet.New_Pet(1)
        store = [
        {"id" :1, "species" : store1.species,"strength" : store1.strength,"speed" : store1.speed,"gender" : store1.gender,},
        {"id" :2, "species" : store2.species,"strength" : store2.strength,"speed" : store2.speed,"gender" : store2.gender,},
        {"id" :3, "species" : store3.species,"strength" : store3.strength,"speed" : store3.speed,"gender" : store3.gender,},
        {"id" :4, "species" : store4.species,"strength" : store4.strength,"speed" : store4.speed,"gender" : store4.gender,},
        {"id" :5, "species" : store5.species,"strength" : store5.strength,"speed" : store5.speed,"gender" : store5.gender,},
        ]
        for i in store:
            print("id:",i["id"],",","species:",i["species"],",","strength:",i["strength"],",","speed:",i["speed"],",","gender:",i["gender"])
        want=int(input("enter the id of what pet you would like to buy. If no pet is wanted enter 6: "))
        if want in range(1,7):
            if want == 6:
                print("return")
            for i in store:
                if want == i["id"]:
                    print("congrats on purchasing a new", i["species"], "thatll be $20!")
                    name=input("Now, name your new pet: " )
                    petsN.append(name)
                    print([i])
                    pets.append(store[[i][0]["id"]])
        else:
            print("please enter a valid id")
            

pet1 = pet.New_Pet(0)
pet.petstore()
print(pets,petsN)


