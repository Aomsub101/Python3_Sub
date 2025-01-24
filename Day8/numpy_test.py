import numpy as np
import time

N = 10000000

nums_list = [i for i in range(N)]

start = time.time()
sqr_list = [v**2 for v in nums_list]
end = time.time()
print(f"List comprehension time: {end - start}")

nums_array = np.array(nums_list)
print(nums_array.shape)

start = time.time()
nums_array *= 2
end = time.time()
print(f"Array time: {end - start}")
