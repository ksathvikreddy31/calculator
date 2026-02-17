import math

def scientific_calculator():
    while True:
        print("\n----- Scientific Calculator -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Log (base 10)")
        print("8. Sin")
        print("9. Cos")
        print("10. Tan")
        print("11. Factorial")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "12":
            print("Exiting Calculator...")
            break

        try:
            if choice in ["1","2","3","4","5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", a + b)
                elif choice == "2":
                    print("Result:", a - b)
                elif choice == "3":
                    print("Result:", a * b)
                elif choice == "4":
                    print("Result:", a / b)
                elif choice == "5":
                    print("Result:", math.pow(a, b))

            elif choice == "6":
                a = float(input("Enter number: "))
                print("Result:", math.sqrt(a))

            elif choice == "7":
                a = float(input("Enter number: "))
                print("Result:", math.log10(a))

            elif choice == "8":
                a = float(input("Enter angle in degrees: "))
                print("Result:", math.sin(math.radians(a)))

            elif choice == "9":
                a = float(input("Enter angle in degrees: "))
                print("Result:", math.cos(math.radians(a)))

            elif choice == "10":
                a = float(input("Enter angle in degrees: "))
                print("Result:", math.tan(math.radians(a)))

            elif choice == "11":
                a = int(input("Enter integer: "))
                print("Result:", math.factorial(a))

            else:
                print("Invalid Choice!")

        except Exception as e:
            print("Error:", e)

scientific_calculator()