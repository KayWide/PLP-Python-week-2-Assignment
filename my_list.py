#create empty list
my_list = []

#append 10, 20, 30, 40 to mylist
my_list.extend([10, 20, 30, 40])
print(my_list)

#insert 15 at the second position
my_list.insert(1, 15)
print(my_list)

#extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

#remove last element
my_list.remove(70)
print(my_list)

#sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of 30 in my_list
num = 30
index = my_list.index(num)
print("The index of", num, "is", index)
