text=input()

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())
 
# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())
 
# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())
 
# original string never changes
print("\nOriginal String")
print(text)

print(text.startswith('P'))
print(text.endswith('n'))
print(text.find('t'))
print(len(text))
print(min(text))
print(max(text))