moshin = {"bmw","mers","gelik","audi"}
print(type(moshin))
moshin.add("nexia")
print(moshin)
moshin.add("matiz")
print(moshin)
moshin1 = {"tico","jiguli","volgo"}
moshin.update(moshin1)
print(moshin)
moshin2 = {"lada","velik"}
moshin.update(moshin2)
print(moshin)
Umumiy = moshin.union(moshin1,moshin2)
print(Umumiy)