def seq(s):
  if not s or len(s) < 2:
    return ''
  ans, prev_y, prev_x = '', (ord(s[0]) - 97)//5, (ord(s[0]) - 97) % 5
  for char in s[1:]:
    y, x = (ord(char) - 97)//5, (ord(char) - 97) % 5
    v, h = 'up, ', 'left, '
    if x - prev_x > 0:
      h = 'right, '
    if y - prev_y > 0:
      v = 'down, '
    for i in range(abs(prev_x-x)):
      ans += h
    for j in range(abs(prev_y-y)):
      ans += v
    prev_y, prev_x = y, x
  return ans[:-2]

print(seq('hello'))