def count_digit_4(lst):
    count = 0
    for num in lst:
        count += str(num).count('4')
    return count

# Example list
numbers = [1234, 4567, 124, 845, 1404]

result = count_digit_4(numbers)
print(f"Number of occurrences of digit 4: {result}")
