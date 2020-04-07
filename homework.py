# function that computes c=volume of a sphere given its radius


def vol(rad):
    return (4/3)*(3.14)*(rad**3)

# write a function that checks whether a number is in a given range(inclusive of high or low)


num = 2
low = 1
high = 10


def range_check(num, low, high):
    if num in range(low, high):
        print("%s is in the range" % str(num))
    else:
        print("Its outside the range")

# check for boolean


def range_bool(num, low, high):
    return num in range(low, high)
