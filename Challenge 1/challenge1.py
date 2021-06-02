# If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and you get 23. Find the sum of all the numbers between 1 and 1000 that are multiples of 3 or 5. Please upload your code and the output from your calculations

# Different possible solutions:
# 1
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

# 2 (as a function that we can test)


def multiples_sum(min, max):
    total = 0
    for i in range(min, max):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(multiples_sum(1, 1000))

# Short solution
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
