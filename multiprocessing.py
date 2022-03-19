
import time

import multiprocessing
def calc_square(numbers):
    print("Print the squares of the numbers")
    for n in numbers:
        print(f'Square of the number is :{n*n}')


def calc_cube(numbers):
    print("The cubes of the numbers is:")
    for n in numbers:
        print(f"Cube:{n*n*n}")


if __name__=='__main__':
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    p2=multiprocessing.Process(target=calc_cube,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done !")