# L- Local function-- names that listed within a function
lambda num: num**2

# E -Enclosing function locals -- names in the local scope of any and all enclosing functions(def of lambda), inner to outer

# Global(module) - names assigned at the top level of a module file or declared in the def with ib a file

# b- Built-in(Pyhton)- names pressigned in the built in namesd module. e.g len()

name = "IM A GLOBAL VARIABLE"  # global variable


def greet():
    # Enclosing
    name = "Sammy"

    def hello():
        # local variable
        name = "I'm Local"
        print("Hello "+name)
    hello()


# ---------------------------------------------------------
# ressigning global value to new local value
x = 50


def func(x):
    print(f"X is {x}")

    # local ressignerd to new value
    x = "New value"
    return x


print(x)  # This will print global
print(func(x))  # this is the ressigned value
