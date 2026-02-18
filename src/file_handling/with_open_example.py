input_path = "../../data/sample.txt"
output_path = "../../data/write.txt"

# Reading using with open
with open(input_path, "r") as file:
    data = file.read()

print("Reading using with open():")
print(data)

# Writing using with open
with open(output_path, "w") as file:
    file.write("Written using with open()\n")
    file.write("No need to close file manually\n")

print("Writing completed using with open()")