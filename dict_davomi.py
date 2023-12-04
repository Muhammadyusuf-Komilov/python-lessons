def sora ():
  a = float(input("a sonini kiriting->"))
  b = float(input("b sonini kiriting->"))
  sorov = int(input("qoshish=1,ayirish=2,bolish=3,kopaytirish=4->"))
  if sorov == 1:
      qoshish(a,b)
  elif sorov == 2:
      ayirish(a,b)
  elif sorov == 3:
      bolish(a,b)
  elif sorov == 4:
      kopaytirish(a,b)  
  else:
      print("siz yuqoridagi raqamlarni tanlamadingiz!!!")
      sora()
def qoshish(a,b):
    print(a+b)
    sora()
def ayirish(a,b):
    print(a-b)
    sora()
def kopaytirish(a,b):
    print(a*b)
    sora()
def bolish(a,b):
    print(a/b)
    sora()



sora()