# solution 1 with .items

a = {"Joey": "Rachel", "Monica": "Chandler", "Phoebe": "Ross"}

for key, value in a.items():
    print(key, "-", value)

# solution 2 with keys

for key in a:
    print(key, "~", a[key])

#solution 3 with keys
print()
for key in a.keys():
    print(key)
    print()
for i in a.values():
    print(i)