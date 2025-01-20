import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext

factorial_list = {0: 1, 1: 1}


def factorial(k):
    if k in factorial_list:
        return factorial_list[k]

    factorial_list[k] = factorial(k-1) * k
    return factorial_list[k]


def natural_number_serie_part(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = 0

    for k in range(k_start, k_end):
        partial_sum += Decimal(1) / Decimal(factorial(k))
        # print(factorial_list[k])
    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum


qres = Queue()

N = 1000
threads_count = 4

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")
#
# getcontext().prec = 100
#
start_time = time.time()
pool = multiprocessing.Pool(num_cores)
results = pool.starmap(natural_number_serie_part, [(N*k, N*(k+1)) for k in range(threads_count)])

for r in results:
    qres.put(r)

# thread_list = []
# for i in range(threads_count):
#     t = threading.Thread(target=natural_number_serie_part, args=(N*i, N*(i+1), qres))
#     thread_list.append(t)
#     t.start()

# for t in thread_list:
#     t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

# --------------Testing formula--------------#
# part1 = natural_number_serie_part(0, 100)
# part2 = natural_number_serie_part(100, 200)
# e_approx = part1 + part2
# -------------------------------------------#

e_approx = 0

while not qres.empty():
    e_approx += qres.get()

print(f"e approximation: {e_approx}")
# print(factorial_list[500])
# 2.718281828459045235360287471
# 2.718281828459045235360287471