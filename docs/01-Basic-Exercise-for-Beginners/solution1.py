def multiplication_or_sum (number1,number2):
    # calculate product of two number
    product = number1 * number2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
    # product is greater than 1000 calculate sum
        return number1 + number2
    
# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)