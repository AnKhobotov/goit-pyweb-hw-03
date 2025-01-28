from time import time, ctime
from multiprocessing import Pool, Process, current_process, cpu_count
import sys

def factorize(*number):
    b = time()
    num_lists = []

    for n in number:
        num_lists.append(deviders(n))

    c = time()
    print(num_lists,c-b,  1)
    return num_lists

def deviders(num):
    name = current_process().name
    print(f"Start process {name}: {ctime()}")
    num_list = []
    r = (round((num/2)))
    for i in range(1,r+1):
        if num % i == 0:
            num_list.append(i)
    num_list.append(num)
    print(f"End work process {name}: {ctime()}")
    return num_list

def callback(num_list):
    print(f"Result in callback: {num_list}")
    

if __name__ == "__main__":
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    process = []
    nums=(128, 255, 99999, 10651060)
    print(f"Count CPU: {cpu_count()}")
    
    
    with Pool(cpu_count()) as p:
        b = time()
        p.map_async(
            deviders,
            nums,
            callback=callback,
        )
        p.close()  
        p.join()  
        
        c = time()
    print(process, c-b,3)