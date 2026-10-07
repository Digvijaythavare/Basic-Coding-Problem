nested_list = [[10, 20], [30, 40], [50, 60]]
flattened = []

for sublist in nested_list:

    for item in sublist:
        flattened.append(item)

print("Flattened List:", flattened)
