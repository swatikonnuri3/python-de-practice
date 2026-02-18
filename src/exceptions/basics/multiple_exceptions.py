
try:
    numbers = [1, 2, 3]
    print(numbers[5])

except (IndexError, TypeError) as error:
    print("Error occurred:", error)