# lists recognized by square brackets
# its an ordered collection
listA = ["mark", 1, 2.34]
print(listA)
# replacing first item of index
listA[1] = "Kasule"  # replaced item
listA.insert(2, "Lwanga")       # added item with position 2
listA.append("Didas")  # adds items at the end
print(listA)

# tuple recognized by round bracket.
# Immutable.
# cant change items in tuple
tuple1 = ("mark", 1, 2.34)
print(tuple1)
# Trying replacing will bring error,
#tuple[2] = "chef"
# print(tuple)

# set recognized by det key word
# its an un-ordered collection/ no repeation.
set1 = set(["mark", 1, 2.34])
print(set1)
# elements added with .add method
set1.add(2)
print(set1)

# Dictionary recognized by curly brackets
# made up of a pair key values.
# First key(s0) item is immutable
# if first key is string, then quote it.
# Second value(s) is mutable/ can be changed.
dict1 = {1: "Mark", 2: "Michael", 3: "Josephine"}
print(dict1)
dict2 = {"x": 1, "y": 2, "z": 3}
print(dict2)
# elements added
dict1[4] = "Dennis"
print(dict1)

dict2["w"] = 4
print(dict2)
