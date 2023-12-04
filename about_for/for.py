fruits = ["apple","pear","pomegranate","grape"]
group = "The best 1" 

for juice in fruits:
  print("These fruits are delicious",juice.rstrip(),"Do you understand?")

for juice in fruits:
  print(f"Assalomu alaykum {juice.upper()}, welcome to our {group} group")

# if yani shart operatori
sorov = input("Bugun kitob oqidingmi? H/Y->")

if sorov == "H":
  print("Ha Hudoga shukur!!!")
elif sorov == "Y":
  print("Malades")
else:
  print("Ekranga qara")