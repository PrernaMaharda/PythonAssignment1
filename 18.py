str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
str1 = sorted(str1.lower())
str2 = sorted(str2.lower())
print("String 1 after sorting",str1)
print("String 2 after sorting",str2)
if (str1 == str2):
    print("String is anagram")
else:
    print("String is not anagram")