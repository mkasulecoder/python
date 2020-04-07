# iteration/ going through something.
# my_iterable is the list to go through/ must be predefined.
# item_name can be any name you want to give to items reproduced.

#my_iterable = [1,2,3]
# for item_name in my_iterable:
# print(item_name)

my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]
for num in my_list:
    print(num)
    # num in this line can also be anything eg "hello" remember hello will be printed several times.
    print("hello")
    print()  # space

# check for even.
for num in my_list:
    if num % 2 == 0:
        print(num)
else:
    print("Odd number")
print(f"Odd Number: {num}")
print()

list_sum = 0
for num in my_list:
    list_sum = list_sum + num  # list_sum =+ num
    print(list_sum)  # indent will give sum of iterated numbers
print(list_sum)  # no indent will give last final sum
print()

# iterate through string
mystring = "Hello World"
for letter in mystring:
    print(letter)


# iterate through tup
tup = (1, 2, 3, 4, 5, 6)
for _ in tup:  # _ can be any name!
    print(_)
    print()

list1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
len(my_list)
print()

for item1 in list1:
    print(item1)
    print()

# tuple un-parking, USED SO MUCH IN PYTHON.
# give a name thats in form of tuple
for (a, b) in list1:  # also (for a,b in list1) is correct
    print(a)  # unparking tuple by index 0 (a)
    print()
    print(b)
print()

# Iterate through a dictionary
dict1 = {"k1": 1, "k2": 2, "k3": 3}
# to print keys by default
for keys in dict1:
    print(keys)
    print()

# to print both items use the .items() function.
for items in dict1.items():
    print(items)
    print()

# to print the last values use .values() function
for values in dict1.values():
    print(values)


# ive commented all the script to save memory
