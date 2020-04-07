# USING THE TRY>>EXCEPT>>ELSE METHOD.
try:
    # code we want to attempt to execute
    # may or may not have an error
    acct_balance = 100 - "200"
except:
    # the code that wil run after noticing an error in try bloc
    print("Hey, it looks like you've got insufficient money on your acct!")
else:
    # code that will run after the try block has been corrected/ will run only when there is no error
    print("Purchase successfull. Goodbye")
    print(acct_balance)

# USING THE TRY>>ELSE>>FINALLY METHOD
# finally is used to run the both except and finally inbuilt keywords.
# "r" =short for read only mode
# "w" = used on a write only file

try:
    # OS command used to open a file then read it "r" or use "w" for writing intention.
    f = open("testfile", "w")
    # OS command used to write in a block of code. This will return an error because initially we intend to just read and write, we could use f.read to ignore error
    f.write("write a test line")
except:
    print("\n")
    print("This is the exception block output Including all other errors e.g. OSError, IOError, TypeError")
finally:
    print("\n")
    print("Finally will always run regardless of errors existence in exception block of code")
    print("\n")

try:
    result = int(input("Enter your age: "))
except:
    print("You didn't enter age in numbers")
finally:
    print("End of try/except/finally code of block")


# using while loop to keep asking user incase they entered a wrong input.
while True:
    try:
        result = int(input("Please enter a number: "))
    except:
        print("Whoops thats not a number!")
        continue
    else:
        print("Thats correct, Thank you!")
        break
    # you can continue touse finally but for a better relevance in real world situations, neglect it cz it wil re write irrelevant out.
    finally:
        print("Let's try again!")
