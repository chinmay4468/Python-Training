with open('C:/Users/Chinmay/Desktop/Python Training/Level3/doc.txt', 'r') as file:
    content = file.read()  
    words = content.split()  
    even_length_words = [word for word in words if len(word) % 2 == 0]

print(" ".join(even_length_words))
