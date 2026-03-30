sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def makerecipt():
    recipt = {"price":0}
    for i in sushi_orders:
        recipt["price"] = recipt["price"]+i["price"]
        if i["name"] not in recipt:
            recipt[i["name"]] = 1
        elif i["name"] in recipt:
            recipt[i["name"]]+=1
    print(recipt)
makerecipt()