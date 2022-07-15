def concatenate(*args):
    result = ''
    for item in args:
        result += item
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))