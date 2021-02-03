# Moving Average

# Moving Average Using Numpy 
import numpy as np

def mov_avg(a,k):
    cum_sum=np.cumsum(a,dtype=float)
    cum_sum[k:] = cum_sum[k:] - cum_sum[:-k]
    return cum_sum[k-1:]/k

a=[3,5,7,2,8,10,11,65,72,81,99,100,150]
k=3  # Moving average with k=3
result = mov_avg(a,k)
print(result)


# Moving Average using while loop
a=[3,5,7,2,8,10,11,65,72,81,99,100,150]
k = 3

i = 0
moving_averages = []

while i < len(a) - k + 1:

    get_current = a[i : i + k]
    window_average = sum(get_current) / k
    moving_averages.append(window_average)

    i += 1

print(moving_averages)