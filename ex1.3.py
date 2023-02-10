def funcMemo(n, memo):
  if n == 0 or n == 1:
    return n
  if not n in memo:
    memo[n] = funcMemo(n-1, memo) + funcMemo(n-2, memo)
  return memo[n]
