def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with three different pieces of named data
print_info(name="Digvijay", age=21, city="Latur")
