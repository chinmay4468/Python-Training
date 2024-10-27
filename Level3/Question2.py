with open('C:/Users/Chinmay/Desktop/Python Training/Level3/doc.txt', 'r') as file:
    line_count = sum(1 for line in file)

print("Number of lines:", line_count)