items = ["apple", "mango", "banana", "mango", "orange"]

unique_item = set()

for i in items:
    if i in unique_item:
        print("value repeted: ", i)
        break
    unique_item.add(i)