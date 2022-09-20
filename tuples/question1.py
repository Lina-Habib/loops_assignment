tuple1 = (10, 20, 30, 40, 50)

index = len(tuple1)-1
new_tuple = list()

while index > -1:
    new_tuple.append(tuple1[index])
    index -= 1

new_tuple = tuple(new_tuple)

print(new_tuple)