def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
<<<<<<< Updated upstream
=======

def is_power_of_5(number):
    if number == 1:
        return True
    elif number < 1:
        return False
    else:
        while number % 5 == 0:
            number /= 5
        return number == 1

def is_power_of_two(num):
    return (num & (num - 1)) == 0 and num != 0
>>>>>>> Stashed changes
