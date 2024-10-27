def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("Yes, the strings are anagrams.")
else:
    print("No, the strings are not anagrams.")
