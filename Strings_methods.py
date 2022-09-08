# working with strings and string methods
name1 = "Peter"
name2 = "paul"
fullname = name1 + " " +name2
#print(fullname)
# lenght of characters in a string
#print(len(fullname))

#multiline strings
content = "                  Today is a busy day. i had to go to the store to buy some oranges\
and i met a friend\
i had not seen in a long time                         "
#print(content)

#print(name1[3])

#slicing
#first 5 elements 
print(content[0:6])
# negative slicing
print(content[-5])
#slicing between two values
print(content[3:11])
print(content[:])
print(content[-8: -4])

king_name = "Mc Hammer"
#king_name[2] = 'r'

#help(str)

superman = "clark kent"
print(superman.upper())
print(len(superman))

# stripping white spaces
content_2 = content.rstrip()
print(content_2)

print(king_name.endswith('er'))
print(king_name.startswith('Mc'))





