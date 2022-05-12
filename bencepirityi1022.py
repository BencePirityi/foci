import random

meccsek = [["1. foduló", "2. foduló", "3. foduló", "4. foduló", "5. foduló"], [], []]

for i in range(5):
    random1 = random.randrange(0, 5)
    random2 = random.randrange(0, 5)
    meccsek[1].append(random1)
    meccsek[2].append(random2)

print("1. feladat - Eredmények:\n")
for i in range(len(meccsek[0])):
    print(f"{meccsek[0][i]}: {meccsek[1][i]}:{meccsek[2][i]}")

atlagosgol = (sum(meccsek[1]) + sum(meccsek[2])) / (len(meccsek[1]) + len(meccsek[2]))
print("\n2. feladat")
print(f"A meccseken átlagosan {atlagosgol} gól született.")

print("\n3. feladat")
if sum(meccsek[1]) > sum(meccsek[2]):
    print("A hazai csapat győzőtt többszőr.")
else:
    print("A vendég csapat győzött többszőr.")

print("\n4. feladat")
for i in range(len(meccsek[0])):
    if meccsek[1][i] == meccsek[2][i]:
        dontetlenmeccs = True
    else:
        dontetlenmeccs = False
if dontetlenmeccs:
    print("Volt döntetlen mérkőzés")
else:
    print("Nem volt döntetlen mérkőzés")

print("\n5. feladat - Hazai győzelmek:")
for i in range(len(meccsek[0])):
    if meccsek[1][i] > meccsek[2][i]:
        print(meccsek[0][i])