def print_kwargs(**kwargs):
    for key, Value in kwargs.items():
        print(f"{key}: {Value}")

print_kwargs(Name1 = "ankush", Name2 = "No Name")
print_kwargs(Name1 = "ankush")
print_kwargs(Name1 = "ankush", Name2 = "No Name", Name3 = "No name 2")
