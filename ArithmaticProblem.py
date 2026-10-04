def multiplication_or_sum(a, b):
    product = a * b

    if product >= 1000:
        return product
    else:
        return a + b

result1 = multiplication_or_sum(20, 30)
print("The result is", result1)

# Testing Case 2
result2 = multiplication_or_sum(40, 388)
print("The result is", result2)

