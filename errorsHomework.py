try:
    for i in ["a", "b", "c"]:
        print(i**2)
except:
    print("Opps, you can't square strings")
    print("\n")

try:
    x = 5
    y = 0
    print(x/y)
except:
    print("\n")
    print("Zero Division Error!")
finally:
    print("Thank You!")  # advisable to use a general statement


def ask_input():
    while True:
        try:
            n = int(input("Enter an interger: "))  # ask user ofr input
        except:
            # msg output incase an error exists
            print("Opps, you didn't enter an integer! \n")
            continue
        else:
            print("Thats correct, thank you")   #msg when input is correct.
            break
    # display the input and get it ready for squaring. remember to get out of while loop by indenting back to same level with while
    print("Your number is: ")
    print(n**2)
