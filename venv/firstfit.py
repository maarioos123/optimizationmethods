import random


class Item:
    def __init__(self, idd, weight, assignbin):
        self.idd = idd
        self.weight = weight
        self.assgnbin = assignbin

    def getweight(self):
        return self.weight

class Bin:
    def __init__(self, idd, items, total_load, capacity):
        self.idd = idd
        self.items = items
        self.total_load = total_load
        self.capacity = capacity


q = 500

items=[]
for i in range(100000):
    weight = random.randint(20, 50)
    items.append(Item(i,weight,0))

items.sort(key=lambda x:x.weight)
Bins = []
Bins.append(Bin(0,[],0,q))
counter = 0
for i in items:
    if Bins[counter].capacity-Bins[counter].total_load - i.weight >0:
        Bins[counter].items.append(i)
        Bins[counter].total_load += i.weight
        i.assgnbin = Bins[counter]
    else:
        counter+=1
        Bins.append(Bin(counter,[],0,q))

