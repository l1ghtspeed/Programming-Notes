import operator
def maxOccur(s):
  d = {}
  for char in s:
    if char not in d:
      d[char] = 0
    d[char] += 1
  return max(d.iteritems(), key=operator.itemgetter(1))[0]

print(maxOccur('hello world'))