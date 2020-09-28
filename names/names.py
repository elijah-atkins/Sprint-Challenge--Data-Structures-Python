import time
from binary_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#runtime: 5.643412828445435 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# imported binary tree from previous data project
# creating a new node named root with first item in names_1
#runtime: 0.08428812026977539 seconds
"""
root = BSTNode(names_1[0])
#insert all names into root node
for i in range(1, (len(names_1) - 1), 1):
    root.insert(names_1[i])

#compare names_1 and names_2
for name in names_2:
    if root.contains(name):
        duplicates.append(name)
"""
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
#runtime: 0.005338907241821289 seconds

seen = set()
#add all names in names_1 to a set
for name in names_1:
    seen.add(name)

#compare all the names in names_2 with the set with all of names_1
for name in names_2:
    if name in seen:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


#find all duplicates between list and within lists
"""
seen = set()
names_3 = names_1 + names_2
for name in names_3:
    if name in seen:
        if seen not in duplicates:
            duplicates.append(name)
    if name not in seen:
        seen.add(name)
"""