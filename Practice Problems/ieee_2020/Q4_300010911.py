def sum(n):
  ans, arr = 0, [0 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      arr[j] += i
      if arr[j] == n:
        ans += 1
  return ans

print(sum(15))