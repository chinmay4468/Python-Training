str = input("Enter the string")
alp = 0
num = 0
for i in str:
    if i.isalpha():
        alp +=1
    elif i.isdigit():
        num+=1
    else:
        continue

print(f"Aplhabets:{alp} & Numbers {num}")