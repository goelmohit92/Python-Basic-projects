# using String function and for loop

a = "Harry Potter and the Goblet of Fire"

w = a.split()
print(w)

for i in range(len(w)):
    w[i] = w[i].lower()

print(w)
print('')

w.sort()
print(w)

for i in w:
    print(i)


