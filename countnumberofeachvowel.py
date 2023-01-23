# using Dictionary
# casefold and lower both function are same and gives lowercase letters
a = input("Enter a sentence here: ")

vowels = "aeiou"
a = a.casefold()     
print(a)

count = {}.fromkeys(vowels,0)
print(count)
print('')
for char in a:
    if char in count:
        count[char]+=1
print(count)
 

# using List and Dictionary comprehension

a = "Harry Potter and the Prisoner of the Azkaban"

vowels = "aeiou"
a = a.casefold()     
print(a)

count = {key:sum([1 for char in a if char == key])for key in vowels}
print(count)


