text = str(input(" ")).split()
list_of_char = {}
for index , char in enumerate(text):
    if char.istitle():
        list_of_char[index] = char
for index , char in list_of_char.items():
    print(f" {index} : {char} ")

    
#enumerate() is a built-in Python function that allows you to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of each element.

#enumerate() returns an iterator that yields pairs of (index, value), where index is the index of the element in the iterable and value is the corresponding element itself.