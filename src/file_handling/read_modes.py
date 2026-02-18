file_path = "../../data/sample.txt"

# 1. Using read() - reads entire file
file = open(file_path, "r")
content = file.read()
print("Using read():\n", content)
file.close()

print("-" * 40)

# 2. Using readline() - reads one line
file = open(file_path, "r")
line = file.readline()
print("Using readline():\n", line)
file.close()

print("-" * 40)

# 3. Using readlines() - reads all lines into a list
file = open(file_path, "r")
lines = file.readlines()
print("Using readlines():")
for l in lines:
    print(l.strip())
file.close()