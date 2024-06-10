punctuation = '''!()#{}$%&*@_,./<>?;':"'''
str1 = input("Enter a string: ")
str2 = ""
for char in str1:
    if char not in punctuation:
        str2 += char
print(str2)
