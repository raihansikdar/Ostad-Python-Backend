print("Welcome to Calculator Project")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

option = int(input("Selection one option: "))

if option == 1:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter Second number: "))
    result = n1 + n2
    print("Addition result: {}".format(result))

elif option == 2:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter Second number: "))
    result = n1 - n2
    print("Subtraction result: {}".format(result))

elif option == 3:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter Second number: "))
    result = n1 * n2
    print("Multiplication result: {}".format(result))

elif option == 4:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter Second number: "))
    if(n2 == 0):
        print("Second number can't be 0")
    else:
        result = n1 / n2
        print("Division result: {}".format(result))

else:
    print("Invalid Option!")
 

