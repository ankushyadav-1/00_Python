def even_ger(limit):
    for i in range(2, limit + 1, 2):
        yield i

limit = int(input("Enter number: "))

for num in even_ger(limit):
    print(num)