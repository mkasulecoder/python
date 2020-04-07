class Dog():
    # attributes
    # this is a method and not function cause its insuide a class
    def _init_(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots  # wil ne boolean

    #operations/Actions -- Methods
    def bark(self):  # use self to refer to the intance itself
        print("Woof! my name is {}".format(self.name))
    # run the method bark() to get results

    #my_dog = Dog(breed="Huskie", name="Max", spots=False)

    # print(my_dog.bark())


# circumference of a circle

class Circle():
    pi = 3.14
    # attributes

    def _init_(self, radius=1):
        self.radius = radius
    # method

    def get_circum(self):
        return 2 * self.pi * self.radius


# creating an instance for the class
my_circle = Circle()
# run/call the instance
my_circle.pi
# output will be 1 unless re written when creating the instance at my_circle = Circle(30) then radius wil be 30
my_circle.radius

# let s call the method on the instance
my_circle.get_circum()  # will give the 188.4
