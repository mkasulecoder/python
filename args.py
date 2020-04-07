# args and kwargs are used to parse in several arguements in parameters.

# 1 WITHOUT ARGS

# prints or returns 5% of the sum of numbers a and b


def my_func(a, b):
    # always list it as tuple so that first number is a and last is b
    return sum((a, b))*0.05


print(my_func(20, 80))

# 2
# returns the sum of two or more numbers


# always give the last number assigned to 0 just in case enters only 3 parameters/variables.
def my_func1(a, b, c, d=0):
    return sum((a, b, c)) * 0.05


print(my_func1(30, 30, 30))

# 3 ARGS    (THE RETURN TUPLES)
# using args helps save the trouble of pre figuring out how many entries the user will enter
# we there use an asterisk * and ignore setting parameters = 0 e.g. c=0,d=0


def my_func2(*args):
    return sum(args) * 0.05


print(my_func2(20, 60, 20, 40))

# 4
# **KWRGS (KEYWORDS) THEY RETURN A DICTIONARY


def my_func3(**kwargs):
    if "fruit" in kwargs:
        print("my fav fruit is {}".format(kwargs["fruit"]))
    else:
        print("i dont see any")


print(my_func3(fruit="apple", veggie="broccoli"))
