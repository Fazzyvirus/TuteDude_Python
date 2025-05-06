#Task 1: Read a File and Handle Errors
try:
    file = open('sample.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print("The File sample.txt not found")
finally:
    print()

#Task 2: Write and Append Data to a File
try:
    file = open('output.txt', 'w')
    userInput = input("Enter some text: ")
    inserted = file.write(userInput)
    print('Data successfully written to output.txt')
    file.close()

    file = open('output.txt', 'a')
    userInput = input("Enter Additional text: ")
    append = file.write(userInput)
    print('Data successfully Appended')
    file.close()

    print('Final content of output.txt: ')
    file = open('output.txt', 'r')
    print(file.read())
    file.close()
except FileExistsError:
    print("The File output.txt not found")
finally:
    print()
