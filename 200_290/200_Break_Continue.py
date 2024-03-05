print("'break' beendet die Schleife")
print("'continue' startet eine neue Iteration")

print("break in for-schleife")
for i in range(5):
    if i == 3:
        break
    print(i)

print("continue in for-schleife")
for i in range(5):
    if i == 3:
        continue
    print(i)



print("break in while-Schleife")
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1


print("continue in while-Schleife")
i = 0
while i < 5:
    if i == 3:
        continue
    print(i)
    i += 1



print("break im enhanced for loop")
liste = [4, 5, 6]
for element in liste:
    if element == 5:
        break
    print(element)


print("continue im enhanced for loop")
liste = [4, 5, 6]
for element in liste:
    if element == 5:
        continue
    print(element)

print("Break im nested Loop")
outer = 0
inner = 0
while outer < 5:
    print("outer =", outer)
    while inner < 5:
        print("inner =", inner)
        inner += 1
        break
    outer += 1
    inner = 0
