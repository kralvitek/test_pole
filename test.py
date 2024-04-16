print("-----------------")
print("                 ")
print("vítejte v pekárně")
print("                 ")
print("-----------------")


print("-------------------------------------")
print("                                     ")
print("Zde můžete vybírat zboží pomocí názvu")
print("                                     ")
print("-------------------------------------")

print("zde je naše zoboží:")
print("-------------------")

kosik =[]

zbozi = ["rohlik", "chleba","houska","donut","buchta"]
for x in zbozi:
  print(x)
print("------")

input("zadejte co chcete přidat do košíku:")

def rohlik():
       zbozi.remove("rohlik")
       kosik.append("rohlik")
def chleba():
       zbozi.remove("chleba")
       kosik.append("chleba")
def houska():
       zbozi.remove("houska")
       kosik.append("houska")
def donut():
       zbozi.remove("donut")
       kosik.append("donut")
def buchta():
       zbozi.remove("buchta")
       kosik.append("buchta")



        



for x in zbozi:
  print(x)



