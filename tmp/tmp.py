import random

class Item(object):    
    def __init__(self, id, name, spec, place):
        self.id = id
        self.name = name
        self.spec = spec
        self.place = place

def db():
    names = []
    specs = []
    cities = []
    items = []
    diseases = []

    with open("tmp/names.txt", "r") as f:
        names_str = f.readlines()
        for name in names_str:
            names.append("Dr. " + name[:-1])

    with open("tmp/doc.txt", "r") as f:
        doc_str = f.readlines()
        for doc in doc_str:
            specs.append(doc[:-1])

    with open("tmp/diseases.txt", "r") as f:
        dis_str = f.readlines()
        for dis in dis_str:
            diseases.append(dis[:-1])

    with open("tmp/cities.txt", "r") as f:
        cities_str = f.readlines()
        for city in cities_str:
            cities.append(city.replace("\t", ",")[:-1])

    for i in range(len(names)):
        items.append(Item(i+1, names[i], random.choice(specs), random.choice(cities)))

    return names, specs, cities, items, diseases
