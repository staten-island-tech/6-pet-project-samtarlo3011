
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
    def basic_action(self):
        while self.age<5:
            self.ch_stats()
            self.die()
            self.older()
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
            if action == 1:
                self.c_hung()
            elif action == 2:
                self.c_ene()
            elif action == 3:
                self.c_love()
            elif action == 4:
                self.c_hp()
            elif action == 5:
                self.c_clean()
            elif action == 6:
                self.c_speed()
            elif action == 7:
                self.c_strength()
            elif action == 8:
                self.c_size()
            elif action == 9:
                self.c_age()
            elif action == 10:
                self.feed()
            elif action == 11:
                self.pet()
            elif action == 12:
                self.bathe()
            elif action == 13:
                self.t_sp()
            elif action == 14:
                self.t_st()
            elif action == 15:
                print("this is visiting the vet i need to figure out what to do about this")
            elif action == 16:
                self.sleep()
            elif action == 18:
                a = int(input("enter here "))
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
                self.age = ag
            time.sleep(3)
    def of_age(self):
        self.ch_stats()
        self.die()
        self.older()
        time.sleep(3)
        action=int(input("""
what action would you like to perform?
1.check pet hunger
2.check pet energy level
3.check pet affection level
4.check pet hp
5.check pet cleanlieness
6.check pet speed
7.check pet strength
8.check pet size
9.check pet age
10.check wallet
11.feed pet
12.pet pet
13.bathe pet
14.train pet speed
15.train pet strength
16.visit the vet
17.visit the shop
18.go to a strength competition
19.go to a speed competiton
20.send them to the assembly line
21.go to sleep for the night
                """))
        if action == 1:
            self.c_hung()
            self.of_age()
        elif action == 2:
            self.c_ene()
            self.of_age()
        elif action == 3:
            self.c_love()
            self.of_age()
        elif action == 4:
            self.c_hp()
            self.of_age()
        elif action == 5:
            self.c_clean()
            self.of_age()
        elif action == 6:
            self.c_speed()
            self.of_age()
        elif action == 7:
            self.c_strength()
            self.of_age()
        elif action == 8:
            self.c_size()
            self.of_age()
        elif action == 9:
            self.c_age()
            self.of_age()
        elif action == 10:
            self.c_wallet()
            self.of_age()
        elif action == 11:
            self.feed()
            self.of_age()
        elif action == 12:
            self.pet()
            self.of_age()
        elif action == 13:
            self.bathe()
            self.of_age()
        elif action == 14:
            self.t_sp()
            self.of_age()
        elif action == 15:
            self.t_st()
            self.of_age()
        elif action == 16:
            print("vet idk")
            self.of_age()
        elif action == 17:
            pet.petstore()
            self.of_age()
        elif action == 18:
            self.st_comp()
            self.of_age()
        elif action == 19:
            self.sp_comp()
            self.of_age()
        elif action == 20:
            print("factory idk")
            self.of_age()
        elif action == 21:
            self.sleep()
        else:
            print ("no such action found")
    def die(self):
        if self.hungry == "starving (losing)" or self.energy == "critically low (sleepy boy)(will start losing hp)" or self.clean == "critically low (will start losing hp)":
            self.hp-=3
        if self.hp == 0:
              print("Whoopsies, dead")
    def c_hung(self):
          print ("hunger=",self.hungry)
    def c_ene(self):
          print("energy=",self.energy)
    def c_love(self):
          print("affection=", self.love)
    def c_hp(self):
          print("health=", self.hp)
    def c_clean(self):
          print("cleanlieness=",self.clean)
    def c_speed(self):
          print("speed=",self.speed)
    def c_strength(self):
          print("strength=",self.strength)
    def c_size(self):
          print ("size=",self.size)
    def c_age(self):
          print("age=",self.age)
    def c_wallet(self):
          print("money=",self.money)
    def feed(self):
        print("hunger decreased!")
        self.h=self.h-5
        self.e=self.e-1
        self.c=self.c-1
        self.l=self.l+2
    def pet(self):
        print("affection increased!")
        self.l=self.l+5
        self.e=self.e-1
        self.h=self.h+1
        self.c=self.c-1
    def ch_stats(self):
        if self.h <= 3 and self.h > 0:
            self.hungry = "low"
        elif self.h >3 and self.h <7:
            self.hungry = "medium"
        elif self.h <= 0:
            self.hungry = "stuffed"
        elif self.h >=7 and self.h < 10:
            self.hungry = "high"
        elif self.h >=10:
            self.hungry = "starving (losing hp)"
            health=health-3
        if self.c <= 3:
            self.clean = "low"
        elif self.c >3 and self.c <7:
            self.clean = "medium"
        elif self.c <= 0:
            self.clean = "critically low (will start losing hp)"
            health=health-3
        elif self.c >=7:
            self.clean = "high"
        elif self.c >10:
            self.clean = "stunningly clean"
        if self.e <= 3 and self.e > 0:
            self.energy = "low"
        elif self.e >3 and self.e <7:
            self.energy = "medium"
        elif self.e <= 0:
            self.energy = "critically low (sleepy boy)(will start losing hp)"
            health=health-3
        elif self.e >=7 and self.e <10:
            self.energy = "high"
        elif self.e >=10:
            self.energy = "bright eyed and bushy tailed"
        if self.l <= 3 and self.l > 0:
            self.love = "low"
        elif self.l >3 and self.l <7:
            self.love = "medium"
        elif self.l <= 0:
            self.love = "in love"
        elif self.l >=7 and self.l < 10:
            self.love = "high"
        elif self.l >=10:
            self.love = "hates you"
    def bathe(self):
        print("cleanlieness increased!")
        self.c=self.c+5
        self.e=self.e-1
        self.h=self.h+1
        self.l=self.l-2
    def t_sp(self):
        print("speed increased!")
        self.speed=self.speed+5
        self.e=self.e-3
        self.h=self.h+2
        self.c=self.c-2
        self.l=self.l+1
    def t_st(self):
        print("strength increased!")
        self.strength=self.strength+5
        self.e=self.e-3
        self.h=self.h+2
        self.c=self.c-2
        self.l=self.l+1
    def sleep(self):
        print("Goodnight! (energy restored)")
        self.a=self.a+1
        self.e=self.e+5
        self.h=self.h+3
        self.c=self.c-1
    def st_comp(self):
        e1 = random.randint(self.strength-20,self.strength+20)
        e2 = random.randint(self.strength-20,self.strength+20)
        e3 = random.randint(self.strength-20,self.strength+20)
        e4 = random.randint(self.strength-20,self.strength+20)
        e5 = random.randint(self.strength-20,self.strength+20)
        list=[e1,e2,e3,e4,e5,self.strength]
        standings=sorted(list)
        if standings[-1] is self.strength:
            print ("you win congrats")
            m=m+15
        elif standings[-1] is self.strength and standings[-1] == standings[-2]:
            print("Its a tie!")
        else:
            print("You lose haha")
            m=m-15
    def sp_comp(self):
        e1 = random.randint(self.speed-20,self.speed+20)
        e2 = random.randint(self.speed-20,self.speed+20)
        e3 = random.randint(self.speed-20,self.speed+20)
        e4 = random.randint(self.speed-20,self.speed+20)
        e5 = random.randint(self.speed-20,self.speed+20)
        list=[e1,e2,e3,e4,e5,self.speed]
        standings=sorted(list)
        if standings[-1] is self.speed:
            print ("you win congrats")
            m=m+15
        elif standings[-1] is self.speed and standings[-1] == standings[-2]:
            print("Its a tie!")
        else:
            print("You lose haha")
            m=m-15
    def older(self):
        if self.a == 360:
            self.ag+=1
            self.a=0
    def stats(self):
        self.die()
        self.age()
        self.ch_stats()
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
            print("id:",i["id"],",","species:",i["species"],",","strength:",i["strength"],",","speed:",i["speed"],",","size:",i["size"],",","gender:",i["gender"])
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
                    print(petsN,pets)

pet1=pet.New_Pet(0,0,0,0,0)
while pet1.age < 5:
    pet1.basic_action()
choose_petO()
