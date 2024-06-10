n = int(input("Enter a number: "))
num1 = 0
num2 = 1
print(0)
print(1)
next_number = num2
count = 1
while (count <= n):
    print(next_number)
    num1 , num2 = num2 , next_number
    next_number = next_number + num1
    count +=1
