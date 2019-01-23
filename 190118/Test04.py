numbers = [1,2,3,4,5]
result = []
"""
for i in numbers[::2]:
    i = i*2
    result.append(i)
"""
for i in numbers:
    if i % 2 == 1:
        i = i*2
        result.append(i)

print(result)