list1 = []
for i in range(1,11):
    n = int(input("Enter a number to add in list: "))
    list1.append(n)
print(list1)
mini = min(list1)
maxi = max(list1)
print("Minimum value of list1=",mini)
print("Maximum value of list1=",maxi)