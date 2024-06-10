list1 = []
for i in range(1,11):
    n = int(input("Enter a number to add in list: "))
    list1.append(n)
print(list1)
sum = 0
for i in list1:
    sum = sum + i
print(sum)