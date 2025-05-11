#Task 1: Create a Dictionary of Student Marks
directory = {'Alpha':45, 'Bravo':55, 'Charlie':79, 'Daniel':92, 'Emmy':99}
name = input("Enter a name: ")
if name in directory:
    marks = directory[name]
    print("{}'s marks: {}.".format(name, marks))
else:
    print("{} doesn't exist.".format(name))

#Task 2: Demonstrate List Slicing
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
list_slice = list[0:5]
print(list_slice)
reversed_list = list_slice[::-1]
print(reversed_list)