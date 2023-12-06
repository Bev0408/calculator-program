# loops program
while True:
    # asks for user input
    try: # promts user to enter an integer if one isnt entered
        num1 = float(input("plaese enter a number: "))
        num2 = float(input("plaese enter another number: "))
    except ValueError:
        print("please enter a valid integer")

    operation = input("please enter one of the following operations \n+ - / *: ")

    if operation == "+":
        (print(num1 + num2))

    elif operation == "-":
        (print(num1 - num2))

    elif operation == "/":
        (print(num1 / num2))

    elif operation == "*":
        (print(num1 * num2))
    else:
        print("please use valid operator!")
    
    #ask user if they want to do another calculation
    complete_additional_calculation = input("do you want to complete another calculation? \n(yes/no): ").lower()

    if complete_additional_calculation != "yes":
        print("Have a nice day!")
        break #this will end the loop


  