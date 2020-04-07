# while loopa will iterate whenever the condition is true
# while boolean_condition:
# do_something
# else:
# do something different.
x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1  # same as x = x+1
else:
    print("X is not less than 5")

 # Break , continue and pass statements
 # Break: breaks out of a closest enclosing loop
 # continue: goes to the top of the closeest enclosing loop
 # pass: does nothing at all. Its used to hold onto a script before testing not to return an error.

 # PASS
x = [1, 2, 3]
for item in x:
    # haven't decided yet what to print yet from these items but want to end script for future use
    pass
print("End of script for now, will return later")

# CONTINUE - USED TO SKIP AN ITEM IN SEQUENCE
name = "mark"
for letter in name:
    if letter == "a":  # skip letter and return to loop sequence.
        continue
    print(letter)
    print()

# BREAK
name1 = "kasule"
for letter in name1:
    if letter == "u":
        break
    print(letter)

# while and break
numb1 = 0
while numb1 < 6:
    if numb1 == 5:
        break
    print(numb1)
    numb1 += 1
