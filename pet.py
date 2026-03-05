
import time
import random

class pet:
    def __init__(self, hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money):
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
    def New_Pet():
        global pets
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
        health=50
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
        health=100
        hp=health
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
        pets=[]
        pets.append(name)
        return pet(hungry, clean, energy, gender, species, hp, love, production, speed, strength, size, age,name,money)
    def basic_action():
        while pet1.age<5:
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
                print(pet1.hungry)
            elif action == 2:
                print("energy=")
                print(pet1.energy)
            elif action == 3:
                print(pet1.love)
                print("love=")
            elif action == 4:
                print("hp=")
                print(pet1.hp)
            elif action == 5:
                print("cleanlieness=")
                print(pet1.clean)
            elif action == 6:
                print("speed=")
                print(pet1.speed)
            elif action == 7:
                print("strength=")
                print(pet1.strength)
            elif action == 8:
                print("size=")
                print(pet1.size)
            elif action == 9:
                print("age=")
                print(pet1.age)
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
                print("this is visiting the vet i need to figure out what to do about this")
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
            pet1.age = ag
            if c <= 3:
                pet1.clean = "low"
            elif c >3 and c <7:
                pet1.clean = "medium"
            elif c <= 0:
                pet1.clean = "critically low (will start losing hp)"
                health=health-3
            elif c >=7:
                pet1.clean = "high"
            elif c >10:
                pet1.clean = "stunningly clean"
            if h <= 3 and h > 0:
                pet1.hungry = "low"
            elif h >3 and h <7:
                pet1.hungry = "medium"
            elif h <= 0:
                pet1.hungry = "stuffed"
            elif h >=7 and h < 10:
                pet1.hungry = "high"
            elif h >=10:
                pet1.hungry = "starving (losing hp)"
                health=health-3
            pet1.hp = health
            if e <= 3 and e > 0:
                pet1.energy = "low"
            elif e >3 and e <7:
                pet1.energy = "medium"
            elif e <= 0:
                pet1.energy = "critically low (sleepy boy)(will start losing hp)"
                health=health-3
            elif e >=7 and e <10:
                pet1.energy = "high"
            elif e >=10:
                pet1.energy = "bright eyed and bushy tailed"
            if l <= 3 and l > 0:
                pet1.love = "low"
            elif l >3 and l <7:
                pet1.love = "medium"
            elif l <= 0:
                pet1.love = "in love"
            elif l >=7 and l < 10:
                pet1.love = "high"
            elif l >=10:
                pet1.love = "hates you"
            pet1.hp = health
            if pet1.hp == 0:
                print("oh no... died")
    def of_age():
        global pets 
        global name
        global h
        global c
        global e
        global l 
        global sp
        global st
        global a
        global ag
        global health
        global m 
        print("Congratulations!! You have successfully kept your pet",(name),"alive for five whole years! This means that you have unlocked some brand new activities. You can now access the shop to buy new pets. You can take your pets to competitions to test thier strength and speed against others or you could force your pets to work in factories! The world is your oyster! Have fun!") 
        days=0
        for i in range (95):
            for i in pets:
                  x=input("which pet would you like to access")
                  if x == i:
                        whichpet = 
            while days < 365:
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
                        print("hunger=")
                        print(pet1.hungry)
                elif action == 2:
                        print("energy=")
                        print(pet1.energy)
                elif action == 3:
                        print(pet1.love)
                        print("love=")
                elif action == 4:
                        print("hp=")
                        print(pet1.hp)
                elif action == 5:
                        print("cleanlieness=")
                        print(pet1.clean)
                elif action == 6:
                        print("speed=")
                        print(pet1.speed)
                elif action == 7:
                        print("strength=")
                        print(pet1.strength)
                elif action == 8:
                        print("size=")
                        print(pet1.size)
                elif action == 9:
                        print("age=")
                        print(pet1.age)
                elif action == 11:
                        print("hunger decreased!")
                        h=h-5
                        e=e-1
                        c=c-1
                        l=l+2
                elif action == 12:
                        print("affection increased!")
                        l=l+5
                        e=e-1
                        h=h+1
                        c=c-1
                elif action == 13:
                        print("cleanlieness increased!")
                        c=c+5
                        e=e-1
                        h=h+1
                        l=l-2
                elif action == 14:
                        print("speed increased!")
                        sp=sp+5
                        e=e-3
                        h=h+2
                        c=c-2
                        l=l+1
                elif action == 15:
                        print("strength increased!")
                        st=st+5
                        e=e-3
                        h=h+2
                        c=c-2
                        l=l+1
                elif action == 16:
                        print("this is visiting the vet i need to figure out what to do about this")
                elif action == 21:
                        print("Goodnight! (energy restored)")
                        a=a+1
                        e=e+5
                        h=h+3
                        c=c-1
                        days = days+1
                elif action == 19:
                    e1 = random.randint(sp-20,sp+20)
                    e2 = random.randint(sp-20,sp+20)
                    e3 = random.randint(sp-20,sp+20)
                    e4 = random.randint(sp-20,sp+20)
                    e5 = random.randint(sp-20,sp+20)
                    list=[e1,e2,e3,e4,e5,sp]
                    standings=sorted(list)
                    if standings[-1] is sp:
                            print ("you win congrats")
                            m=m+15
                    elif standings[-1] is sp and standings[-1] == standings[-2]:
                            print("Its a tie!")
                    else:
                            print("You lose haha")
                            m=m-15
                elif action == 18:
                    e1 = random.randint(st-20,st+20)
                    e2 = random.randint(st-20,st+20)
                    e3 = random.randint(st-20,st+20)
                    e4 = random.randint(st-20,st+20)
                    e5 = random.randint(st-20,st+20)
                    list=[e1,e2,e3,e4,e5,st]
                    standings=sorted(list)
                    if standings[-1] is st:
                            print ("you win congrats")
                            m=m+15
                    elif standings[-1] is st and standings[-1] == standings[-2]:
                            print("Its a tie!")
                    else:
                            print("You lose haha")
                            m=m-15
                time.sleep(3)
                pet1.age = ag
                if c <= 3:
                        pet1.clean = "low"
                elif c >3 and c <7:
                        pet1.clean = "medium"
                elif c <= 0:
                        pet1.clean = "critically low (will start losing hp)"
                        health=health-3
                elif c >=7:
                        pet1.clean = "high"
                elif c >10:
                        pet1.clean = "stunningly clean"
                if h <= 3 and h > 0:
                        pet1.hungry = "low"
                elif h >3 and h <7:
                        pet1.hungry = "medium"
                elif h <= 0:
                        pet1.hungry = "stuffed"
                elif h >=7 and h < 10:
                        pet1.hungry = "high"
                elif h >=10:
                        pet1.hungry = "starving (losing hp)"
                        health=health-3
                pet1.hp = health
                if e <= 3 and e > 0:
                        pet1.energy = "low"
                elif e >3 and e <7:
                        pet1.energy = "medium"
                elif e <= 0:
                        pet1.energy = "critically low (sleepy boy)(will start losing hp)"
                        health=health-3
                elif e >=7 and e <10:
                        pet1.energy = "high"
                elif e >=10:
                        pet1.energy = "bright eyed and bushy tailed"
                if l <= 3 and l > 0:
                        pet1.love = "low"
                elif l >3 and l <7:
                        pet1.love = "medium"
                elif l <= 0:
                        pet1.love = "in love"
                elif l >=7 and l < 10:
                        pet1.love = "high"
                elif l >=10:
                        pet1.love = "hates you"
                pet1.hp = health
            if days == 365:
                ag=ag+1
                pet1.age=ag
        pet1.money = m 
pet1=pet.New_Pet()