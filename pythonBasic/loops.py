obj = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in obj:
    print(i * 2)

for j in range(1, 6):  # 1,2,3,4,5
    print(j)

print("------brincando valores de 2 en 2--------")
for j in range(1, 6, 2):  # 1,2,3,4,5   (j=1;i<6; j+2)   +2
    print(j, "-", j * 3)

print("------while--------")
it = 10
while it > 1:
    print(it)
    it = it - 1
    if it == 9:
        continue
    if it == 3:
        break


