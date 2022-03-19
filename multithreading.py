'''Thread is separate flow of execution.
 Every thread has a task. It doesn't depend on another tasks'''
'''using multiple threads in program or process is called multithreading'''



'''the main application areas of mutithreading are:
multimedia graphics
animations
video games
web servers
application servers

nepal rastra bank:
    suppose three persons are using app of the bank.
     so there is multithreading since each person is using the application at the same 
    time and they are independent of each other.

'''
import time
import threading

def cal_square(numbers):
    print('Print the square numbers\n')

    for n in numbers:
        time.sleep(0.2)
        print(f'The square of the given number {n*n}')



def calc_cube(numbers):
    print("the cube of given numbers")

    for n in numbers:
        time.sleep(0.2)
        print(f'The Cube of the numbers are {n*n*n}\n')

input=[2,3,9,10] 
t=time.time()
t1=threading.Thread(target=cal_square,args=(input,))
t2=threading.Thread(target=calc_cube,args=(input,))

t1.start()
t2.start()
t1.join()
t2.join()
print(f'Done in: {time.time()-t}') 
'''it took 1.6034 seconds before multithreading and 0.802 after multithreading'''






