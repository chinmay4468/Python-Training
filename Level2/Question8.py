string = "Hello, World!"
vowel = "aeiou"
count = 0
for i in string:
    if i.isalpha():
        if i in vowel:
            count+=1
print(count)