try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")