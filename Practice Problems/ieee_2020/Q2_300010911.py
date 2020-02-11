def is_palindromic(s):
  for i in range(len(s)//2):
    if s[i] != s[~i]:
      return False
  return True

def lps(s):
  ans = (0, '')
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      if is_palindromic(s[i:j]):
        if ans[0] < j - i:
          ans = (j-i, s[i:j])
  return ans[1]

print(lps('abbccddcc'))