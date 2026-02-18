try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)

except ValueError:
    print("Invalid input")

else:
    print("Execution successful")

finally:
    print("Program finished")