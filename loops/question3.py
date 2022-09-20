
num = int(input("Enter a number: "))

remainder = 0
reverse_number = ""

while num > 0:
    remainder = num % 10
    reverse_number = reverse_number + str(remainder)
    num = int(num / 10)

print(reverse_number)

