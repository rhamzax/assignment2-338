import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
  if low < high:
    pi = func2(arr, low, high)
    func1(arr, low, pi-1)
    func1(arr, pi + 1, high)

def func2(array, start, end):
  p = array[start]
  low = start + 1
  high = end
  while True:
    while low <= high and array[high] >= p:
      high = high - 1
    while low <= high and array[low] <= p:
      low = low + 1
    if low <= high:
      array[low], array[high] = array[high], array[low]
    else:
      break
  array[start], array[high] = array[high], array[start]
  return high

#import data
import urllib
import json
with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json') as url:
    data_url = json.load(url)


import timeit
timeforsort = []

for i in range(0, len(data_url)):
  timeforsort.append(timeit.timeit(lambda: func1(data_url[i], 0, len(data_url[i])-1), setup="from __main__ import func1", number=1))

import matplotlib.pyplot as plt
indexs = [i for i in range(0, len(data_url))]
plt.plot(indexs, timeforsort, label="func1")
plt.legend()
plt.xlabel("Index number")
plt.ylabel("Time(s)")
plt.show()