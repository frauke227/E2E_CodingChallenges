# Division
# Create a function that calculated the result of a division of 2 numbers, e.g. divide(4,2) returns 2.0.

def division(x, y=0):
    if y == 0:
        return f'This is not possible'
    else:
        result = float(x/y)
        return round(result, 2)


print(division(4, 0))
