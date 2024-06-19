#string functions

name = "sai venkat"

print(len(name))  #length
print(name.endswith("venkat"))  #chencks end word
print(name.startswith("sai"))   #checks starting word
print(name.capitalize())  #capitalize starting letter
 
#len(): Returns the length of a string.

text = "Hello, World!"
print(len(text))  # Output: 13

#str.lower(): Converts all characters in the string to lowercase.
text = "Hello, World!"
print(text.lower())  # Output: hello, world!

#str.upper(): Converts all characters in the string to uppercase.

text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!

#str.capitalize(): Capitalizes the first character of the string

text = "hello, world!"
print(text.capitalize())  # Output: Hello, world!


#str.title(): Capitalizes the first character of each word in the string.

text = "hello, world!"
print(text.title())  # Output: Hello, World!


#str.strip(): Removes any leading and trailing whitespace.
text = "  Hello, World!  "
print(text.strip())  # Output: Hello, World!


#str.replace(old, new): Replaces all occurrences of a substring with another substring.

text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: Hello, Python!


#str.split(separator): Splits the string into a list of substrings based on a separator.

text = "Hello, World!"
print(text.split(", "))  # Output: ['Hello', 'World!']


#str.join(iterable): Joins elements of an iterable with the string as a separator.

words = ["Hello", "World"]
print(", ".join(words))  # Output: Hello, World


#str.find(sub): Returns the lowest index in the string where substring sub is found. Returns -1 if not found.

text = "Hello, World!"
print(text.find("World"))  # Output: 7


#str.count(sub): Returns the number of occurrences of substring sub in the string.

text = "Hello, World! Hello again!"
print(text.count("Hello"))  # Output: 2
