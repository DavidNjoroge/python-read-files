handle = open('test.txt','r')

# Counter for the loop
counter = 0
# Read the text file
data = handle.read()

# Read the first line
# data = handle.readline()

# Read multiple lines returns a list
# data = handle.readlines()

# loops through the list and counts Python
for word in data.split():
    if word == ",":
        counter += 1

# Print the data
# print(data)

# Print length of data
# print(len(data))

# Print counter
print(counter)

handle.close()
