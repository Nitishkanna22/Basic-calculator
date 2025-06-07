def addition():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    if a.isdigit() and b.isdigit():
        result = float(a)+float(b)
        print(f"The result is {result}")

    else:
        print("Enter only integer value")
        return 0 


def subtraction():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    if a.isdigit() and b.isdigit():
        result = float(a)-float(b)
        print(f"The result is {result}")

    else:
        print("Enter only integer value")
        return 0
    

def multiplication():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    if a.isdigit() and b.isdigit():
        result = float(a)*float(b)
        print(f"The result is {result}")

    else:
        print("Enter only integer value")
        return 0


def division():
    a = input("Enter the first number: ")
    b= input("Enter the second number: ")

    if a.isdigit() and b.isdigit():
        if float(a) and float(b) == 0:
            print("The result is undefined")
            return 0
        
        elif float(a) == 0:
            print("The result is 0")
            return 0
        
        elif float(b) == 0:
            print("The result is 0")
            return 0
        
        elif float (a) and float (b) > 0:
            result = float(a)/float(b)
            print(f"The result is {result:.2f}")

    else:
        print("Enter only integer value")
        return 0


is_running = True

while is_running:
    print("\n***********************************************")
    print("Welcome to the modern calculator sectors!!!")
    print("***********************************************\n")
    print("Please enter the number to excute the respective operation")
    print("1. Addition")
    print("2. Subraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit the calculator")

    option = input("Enter the operation to be executed (1-5): ")

    if option == '1':
        addition()
    elif option == '2':
        subtraction()
    elif option == '3':
        multiplication()
    elif option == '4':
        division()
    elif option == '5':
        is_running = False
        print("Thank you using the application!!")
    else:
        print("Please enter a valid option")
        print("1 for addition")
        print("2 for subraction")
        print("3 for multiplication")
        print("4 for division")
        print("5 to exit the calculator")
