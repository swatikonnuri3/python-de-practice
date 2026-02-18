# 1. Write mode ("w") – overwrites file
file = open("../../data/write.txt", "w")
file.write("This is write mode\n")
file.write("Old content is overwritten\n")
file.close()

print("Data written using write mode")

# 2. Append mode ("a") – adds content
file = open("../../data/append.txt", "a")
file.write("This line is appended\n")
file.write("Append mode does not delete old data\n")
file.close()

print("Data written using append mode")