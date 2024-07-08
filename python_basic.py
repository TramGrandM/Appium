import functools

number = [2, 4, 6]
double = [x * 2 for x in number]
print(double)

List = []
for x in "Huyen Tram !":
    List.append(x)
print(List)

numbers = list(map(lambda i: i * 10, [i for i in range(1, 6)]))
print(numbers)

square = [x ** 2 for x in range(1, 11)]
print(square)

lst = list(range(1, 11))
print(lst)

a = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(a(21))

my_list = [1, 2, 3, 4, 5, 10]

mlist = list(filter(lambda x: x % 3 == 0, my_list))
print(mlist)

print("Sum : ", end=" ")
print(functools.reduce(lambda c, b: c + b, my_list))
