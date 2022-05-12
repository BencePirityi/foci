meccsek = [["1. foduló", "2. foduló", "3. foduló", "4. foduló", "5. foduló"], [3, 2, 0, 2, 3], [0, 0, 1, 0, 3]]

print("1. feladat - Eredmények:\n")
for i in range(len(meccsek[0])):
    print(f"{meccsek[0][i]}: {meccsek[1][i]}:{meccsek[2][i]}")
