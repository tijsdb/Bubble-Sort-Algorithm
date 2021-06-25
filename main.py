array = input("List of numbers: ")
array = array.split()

length = len(array)
length -= 1

for x in range(length):
    for y in range(length):
        if array[length - y] < array[length - y - 1]:
            a = array[length - y]
            b = array[length - y - 1]

            array[length - y] = b
            array[length - y - 1] = a

print(array)
