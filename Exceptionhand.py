def calsi():
    try:
        results = []
        while True:
            n1 = int(input("Enter the first number: "))
            n2 = int(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            

            if operator == "+":
                result = n1 + n2
            elif operator == "-":
                # print("Result:", n1 - n2)
                result = n1 - n2
            elif operator == "*":
                # print("Result:", n1 * n2)
                result = n1 * n2
            elif operator == "/":
                if n2 != 0:
                    # print("Result:", n1 / n2)
                    result = n1 / n2
                else:
                    print("Error: Division by zero is not allowed.")

            else:
                print("Invalid operator. Please enter one of +, -, *, /")
                continue  # Ask agai


            # print("Result history: ", result)
            results.append(result)

            # Ask usery if they want to continue
            user_input = input("Do you want to continue? (y/n): ").lower()
            if user_input == 'n':
                print("Thanks for using the calculator.")
                print("The result history is: ",results)
                
                with open("file.txt", "w") as file:
                    file.write(str(results))

                break
    
    except ValueError:
        print("Invalid input. Please enter integer values.")

calsi()

