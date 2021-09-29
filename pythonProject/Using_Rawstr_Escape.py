s = 'Hello\nWorld'  # \n acts as special character(newline character)
print(s)
raw_s = r'Hello\nWorld'  # here newline character is a part of the string
print(raw_s)
raw_s1 = r'it\'s raining'
print(raw_s1)
raw_s2 = R'My name is "Priyanka"'
print(raw_s2)
# print the above lines without raw string (Using Escape character)
raw_s3 = 'Hello\\nWorld'
print(raw_s3)  # this output is same as raw_s output
s4 = 'It\'s raining!'
print(s4)  # same as saw_s1, but in raw string the backslash is included as string character
s5 = 'My name is "Priyanka"'
print(s5)
s6 = "My name is \"Priyanka\""
print(s6)

