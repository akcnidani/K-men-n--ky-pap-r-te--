import random

# Uvítání
print("Vítej v hře Kámen nůžky papír teď!")
print("------------------------------------")
print("V této hře budeš hrát proti počítači, ")
print("který si náhodně vygeneruje kámen, ")
print("nůžky nebo papír.")
print("------------------------------------")

volbaPocitac = random.randint(0, 2)
volbaHrac = 0


# 0 = kámen
# 1 = nůžky
# 2 = papír

def vyber():
    global volbaHrac
    print("Napiš 0 pokud chceš kámen")
    print("Napiš 1 pokud chceš nůžky")
    print("Napiš 2 pokud chceš papír")
    volbaHrac = int(input("Vyber si kámen, nůžky nebo papír: "))


vyber()

while True:
    if volbaHrac == 0:
        print("Vybral sis kámen!")
        if volbaHrac == volbaPocitac:
            print("Je to kámen | kámen!")
            print("Remíza!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 1:
            print("Je to kámen | nůžky!")
            print("Bod pro tebe!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 2:
            print("Je to kámen | papír!")
            print("Bod pro počítače!")
            volbaPocitac = random.randint(0, 2)
            vyber()

    if volbaHrac == 1:
        print("Vybral sis nůžky!")
        if volbaPocitac == 0:
            print("Je to nůžky | kámen!")
            print("Bod pro počítače!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 1:
            print("Je to nůžky | nůžky!")
            print("Remíza!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 2:
            print("Je to nůžky | papír!")
            print("Bod pro tebe!!")
            volbaPocitac = random.randint(0, 2)
            vyber()

    if volbaHrac == 2:
        print("Vybral sis papír!")
        if volbaPocitac == 0:
            print("Je to papír | kámen!")
            print("Bod pro tebe!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 1:
            print("Je to papír | nůžky!")
            print("Bod pro počítače!")
            volbaPocitac = random.randint(0, 2)
            vyber()
        if volbaPocitac == 2:
            print("Je to papír | papír!")
            print("Remíza!")
            volbaPocitac = random.randint(0, 2)
            vyber()
