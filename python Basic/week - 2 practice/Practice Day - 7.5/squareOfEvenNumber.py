nums = [1, 2, 3, 4, 5, 6]
squareOfEvenNumbers = list(map(lambda x: x**2, list(filter(lambda x : x if x%2 == 0 else None,nums))))
print(squareOfEvenNumbers)