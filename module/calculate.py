'''
    Module program
'''

def addition(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def subtraction(number1, number2):
    result = 0
    if number1 > number2:
        result = number1-number2
    else:
        result = number2-number1
    return result