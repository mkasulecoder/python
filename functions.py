# functions are codes of block executed when called.
# they should be defined at begining
# they should be documented fpr future readers on pressing shift tab in parameter section.


def name_function():
    """  
    DOCSTRING INFO ABOUT FUNCTION
    OUTPUT: Hello..
    """


# print("Hello")  #print will always return a none type whenever you call a function by itself. so its better to use return function.
name_function()

# using a return key word


# 1
def say_hi(name="Name"):
    return "Hello "+name


result = say_hi("Jose")
print(result)

# 2


def add(n1, n2):
    return n1+n2


result = add(20, 30)
print(result)

# check if word exits on a sentence
# check if dof is in sentence


def dog_check(mystring):
    # don't need to use if statement case this is already an if statement
    return "dog" in mystring.lower()


print("dog" in "dog ran away")

# 3
# PIG LATIN. if word is vowel, then ay at the end else pick first letter add it to the end then add ay
# use "word" and "apple"


def pig_latin(word):
    first_letter = word[0]
    if first_letter in "aeoiu":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + word[0] + "ay"
    return pig_word


print(pig_latin("mark"))
