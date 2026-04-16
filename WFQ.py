

premium = []
standard = []
economy = []

with open("input queue-1.txt", "r") as file:
    content = file.read()
    passengers = content.split("\n")

for i in passengers:
    current = i
    if current[0] == "P":
        premium.append(current)
    elif current[0] == "S":
        standard.append(current)
    elif current[0] == "E":
        economy.append(current)

while premium or standard or economy:
    for i in range(3):
        if premium:
            print("\n",premium[0])
            premium.pop(0)
        else:
            break

    for i in range(2):
        if standard:
            print("\n",standard[0])
            standard.pop(0)
        else:
            break

    print("\n",economy[0])
    economy.pop(0)
