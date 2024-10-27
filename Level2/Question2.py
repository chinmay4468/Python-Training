list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = [1, 2, 3, 4, 5]

unique = set(list1).union(set(list2))
print(unique)