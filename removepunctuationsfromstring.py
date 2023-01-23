# Solution using for loop
# punc = punctuation

punc =  '''()[]{}!@#$%^&*_+-=\|""';:<>?/.,'''

string = input("Enter anything here: ")

empty_srt = ""

for i in string:
    if i not in punc:
        empty_srt = empty_srt + i

print(empty_srt)
