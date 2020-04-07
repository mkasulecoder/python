# range: used to list numbers except the last one. e.g  range(0, 10) or range (10)
# step size: used to skip number by 2 (will return even numbers) e.g range(0,10,2) 2 is step size
from random import randint
from random import shuffle
for num in range(0, 10):  # or range(10)
    print(num)

# step size
for numb1 in range(0, 10, 2):
    print(numb1)

# enumerate: unparks a sequence into a tuple like form with both index and values
word = "enumerate"
for items in enumerate(word):
    print(items)  # or
    print("\n")
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

# zip functions: used to pairs up index and values into a tuple from diff lists
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
for items in zip(list1, list2):
    print(items)
    print("\n")
# zip function on un even items will only match the indexws that match and wil ignore the rest.
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["x", "y", "z"]
for un_even_items in zip(list1, list2):
    print(un_even_items)
    print("\n")

# unpark tuple
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["x", "y", "z"]
for x, y in zip(list1, list2):  # x = index, y = values
    print(y)
    print("\n")

# IN OPERATOR: use to check if elememt exists in a sequence
x in [1, 2, 3, 4, 5]  # will return False

2 in [1, 2, 3, 4]  # will return True

# a in "world"  # will return False

"mykey" in {"mykey", 256}  # will return true from dictionary

dict = {"mykey": 256}
256 in dict.values()  # will return true cause of the value matches
256 in dict.keys()  # False cause 256 is not a key nut value.

# MAX AND MIN: checks max(s) and min(s)
list1 = [1, 2, 3, 4, 5]
print(max(list1))
print("\n")
print(min(list1))

# RANDOM FUNCTION: USED TO IMPORT FUNCTIONS FROM RANDOM LIBRARY
list4 = [1, 2, 3, 4, 5, 6]
shuffle(list4)  # works in place and not kept in memory so will not show in output

# RANDINT: use to grab a random integer from lower int to higher
list4 = [1, 2, 3, 4, 5]
rand_num = randint(1, 5)
print("")
print(rand_num)

# INPUT FUNCTION: used to accept inputs from user but only accepts strings.
# however you can cast/ change str to int.
result = input("Enter you name: ")
