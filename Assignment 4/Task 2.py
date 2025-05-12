user_input = input("Enter some text to write to the file output.txt:")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
    print('Data successfully added to the file:output.txt')

additional_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
    print('Data successfully appended in the file:output.txt')

print("\nFinal contents of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
