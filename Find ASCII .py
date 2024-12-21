char = list(str(input("Enter the Word: ")))
for i in range (len(char)):
    print("The ASCII value of '" + char[i] + "' is", ord(char[i]))