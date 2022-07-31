import time
from unittest import result



def time_at(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"The time taken by {function.__name__} is {end - start} milliseconds")

        return result
    return wrapper



@time_at
def calculate_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


if __name__ == '__main__':
    print(calculate_square([1, 2, 3]))


