# solution 1 using | operator

dict1 = {"JOhn": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}

print(dict1 | dict2)

# solution using ** operator

dict1 = {"JOhn": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}

print({**dict1, **dict2})

# using copy() and update() methods

dict1 = {"JOhn": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)
