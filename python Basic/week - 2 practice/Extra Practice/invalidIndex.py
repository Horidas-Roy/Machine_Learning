numbers = [12,32,74,87,98]

try:
    index = int(input())
    print(f"Value at index({index}): {numbers[index]}")
except IndexError:
    print("Invallid index...!")
except ValueError:
    print("Value Error")