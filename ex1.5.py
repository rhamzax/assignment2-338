import timeit

def func(n):
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)

def funcMemo(n, memo):
  if n == 0 or n == 1:
    return n
  if not n in memo:
    memo[n] = funcMemo(n-1, memo) + funcMemo(n-2, memo)
  return memo[n]

# Compare the time it takes to run func and funcMemo for n = 0, 1, 2, ..., 35
timeforfunc = []
timeforfuncMemo = []
for i in range(0, 36):
  timeforfunc.append(timeit.timeit(lambda: func(i), setup="from __main__ import func", number=1))
  timeforfuncMemo.append(timeit.timeit(lambda: funcMemo(i,{}), setup="from __main__ import funcMemo", number=1))

# Plot the results
import matplotlib.pyplot as plt

integers = [i for i in range(0, 36)]
plt.plot(integers, timeforfunc, label="func")
plt.plot(integers, timeforfuncMemo, label="funcMemo")
plt.legend()
plt.xlabel("Number of integers")
plt.ylabel("Time(s)")
plt.show()