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
    def __init__(self, hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag,ill):
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
        self.ill=ill
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
        money=10000000
        hp=50
        ill=1
        hungry="low"
        clean="clean"
        energy="high"
        love=0
        age=ag
        production=0
        name=input("""name your pet!
""")
        petsN.append(name)
        pets.append(pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag,ill))  
        return pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money,h,c,e,l,a,ag,ill)
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
    def sickness(self):
        if self.ill == 1:
            x = random.randint(1,5)
            if self.clean == "critically low (risk of illness VERY high)":
                if x > 1:
                    self.ill = 1
            elif self.clean == "low":
                if x > 2:
                    self.ill = 1
            elif self.clean == "medium":
                if x > 3:
                    self.ill = 1
            elif self.clean == "high":
                if x > 4:
                    self.ill = 1
            elif self.clean == "stunningly clean":
                if x > 5:
                    self.ill = 1
            if self.ill == 1:
                sick = random.randint(1,5)
                print(sick,self.ill)
                if sick == 1:
                    self.ill = "itchy skin"
                    print("work")
                elif sick == 2:
                    self.ill = "bad teeth"
                    print("work")
                elif sick == 3:
                    self.ill = "diabetes"
                    print("work")
                elif sick == 4:
                    self.ill = "gassy (this is a real medical emergency that actual pets can have and it could be fatal. you learn something new every day)"
                    print("work")
                elif sick == 5:
                    self.ill = "rabies"
                    print("work")
                print(self.ill)
    def die(self):
        if self.hungry == "starving (losing hp)" or self.energy == "critically low (sleepy boy)(will start losing hp)" :
            self.hp-=3
        if self.ill == "itchy skin":
            self.hp -= 5
        elif self.ill == "bad teeth":
            self.hp -= 10
        elif self.ill == "diabetes":
            self.hp -= 15
        elif self.ill == "gassy (this is a real medical emergency that actual pets can have and it could be fatal. you learn something new every day)":
            self.hp -= 20
        elif self.ill == "rabies":
            self.hp -= 25
        if self.hp <= 0:
              print("Whoopsies, dead")
    def vet(self):
        print("welcome to the vet, a checkup is $90")
        if self.money < 90:
            print("it looks like you dont have enough *cough* broke boy *cough*. Come back when you get yo money up")
        else:
            self.money -= 90
            print ("okay we'll check up on", self.name)
            time.sleep(2)
            if self.ill == "no":
                print("your pet is healthy as can be! Thier current health is", self.hp, ". We can heal them 10hp for $100, or you can go home")
                heal = int(input("""
1.heal 
2.leave"""))
                if heal == 1:
                    if self.money < 100:
                        print("you have no money")
                        self.of_age()
                    else:
                        print("pet healed")
                        self.hp+=10
                        self.money-=100
                        self.of_age()
                if heal == 2:
                    self.of_age()
            else:
                print("unfortunately your pet has", self.ill, "and is losing hp. We can cure them for:")
                if self.ill == "itchy skin":
                    print("$150")
                    y=150
                elif self.ill == "bad teeth":
                    print("$200")
                    y=200
                elif self.ill == "diabetes":
                    print("$250")
                    y=250
                elif self.ill == "gassy (this is a real medical emergency that actual pets can have and it could be fatal. you learn something new every day)":
                    print("$300")
                    y=300
                elif self.ill == "rabies":
                    print("$400")
                    y=400
                x=int(input("""
Would you like the cure?
1.yes
2.no"""))
                if x == 1:
                    if self.money < y:
                        print("you have no money")
                        self.of_age()
                    else:
                        print("pet healed")
                        self.ill == "no"
                        self.money-=y
                        self.of_age()
                elif x == 2:
                    print("okay see you later!")
                    self.of_age()
pet1 = pet.New_Pet(0,0,0,0,0)
pet1.sickness()
pet1.vet()