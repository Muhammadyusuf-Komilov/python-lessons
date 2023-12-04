# student = {
#   "ism":"Yahyobek",
#   'yosh':18,
#   "manzil":"Andijon",
#   "erkakmi":True,
# }
# x = student.get("ism")
# oqish = {"oqish":"kollej"}
# student.update(oqish)
# print(student)


# royxat = []
# def malumot():
#   ism = input("ismingizni kiriting")
#   royxat.append(ism)
#   savol()
# def savol():
#   sorov = int(input("Siz malumot kiritishni istaysizmi? 1/0"))
#   if sorov == 1:
#     malumot()
#   else:
#     print(royxat)
# savol()


moshinalar = {
  "nexia":"$15000",
  "matiz":"5000",
  "lacetti":"20000",
}
carlist = []
for car in moshinalar:
    carlist.append(car)
print(carlist)
moshin = input("mashina nomini kiriting")
x = moshinalar.get(moshin)
print(x)
