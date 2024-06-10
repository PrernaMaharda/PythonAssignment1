list1 = []
for i in range(1,11):
    n = int(input("Enter a number to add in list: "))
    list1.append(n)
print(list1)
n = int(input("Enter a number to count in list: "))
count = list1.count(n)
print(count)