friends = {"Rachel": "Ross", "Monica": "Chandeler", "Phoebe": "Joey"}

print(friends)

# solution1 with .items

for key, value in friends.items():
    print(key, "-", value)
print()
# solution2 with keys

for key in friends:
    print(key, "-", friends[key])
print()

#solution3 with keys and values

for j in friends.keys():
    print(j)

for i in friends.values():
    print(i)