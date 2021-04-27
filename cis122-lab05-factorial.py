'''
Author: Joseph Macalinao
CIS 122 Lab 5 Spring
Description: Create a factorial function using loops and conditionals
Credit: Lab
'''
import math
def factorial(num):
    '''
    This function will return the factorial of a number

    This function has argument num that will repeatedly multiply itself by its lower numbers and return that value

    arg:
    num(int) - the number that will be factorialized

    return: total(num multiplied by its lower numbers)
    '''

    # convert num to integer
    num = int(num)

    # check if num < 0
    if num < 0:
    #    #print error and return None
        print("error: must be greater than or equal to 0")
        return None

    # check if num is == 0
    if num == 0:

    #    # return 1
        return 1


    # check if num > 0
    else:
        total = 1
    #    # iterate from 1 to n
        for i in range(1, num + 1):
    #         # perform the intermeiary calculations
            total = total * i
    # return the total
        return total



def test_factorial(num, show = False):
    '''
    This function will return the factorial of a number

    This function has argument num that will repeatedly multiply itself by its lower numbers and return that value
    If you put show as true, it will also print out each iteration of the factorial process

    arg:
    num(int) - the number that will be factorialized
    show(boolean) - whether or not you want to see the iterations

    return: none
    '''
    errors = 0
    range_num = num + 1
    for i in range(num):
        result = factorial(i)

        solution = math.factorial(i)
        if show:
            print(f'{i}: {result} {solution}')
        if result != solution:
            errors += 1
            print('*', result, solution)



    print(f'Errors ({num}): {errors}')


#test_factorial(5, True)
fact = int(input("Enter factorial number: "))
print(factorial(fact))