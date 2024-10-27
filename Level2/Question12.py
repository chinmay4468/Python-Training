Chance = 3
username = input("Enter the username")
password = input("Enter the password")
retype = input("Retype the password")
match = False
if password == retype:
    match = True
else: 
    while (Chance>0):
        retype = input("Retype the password")
        if retype == password:
            print("Password match")
            break
        else:
            Chance-=1
    else:
        print("No more chance left")

