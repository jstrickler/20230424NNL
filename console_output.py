import sys
print("Hello")
value = 5
color = "blue"
print(value, color) 
print(value, color, sep="/")
print("UH-OH", file=sys.stderr)

file_name = input("Please enter file name: ")
print("file_name: {}".format(file_name))


