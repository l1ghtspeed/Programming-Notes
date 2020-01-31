import sys
import math

def cipher(text):
  text = text.replace(' ', '')
  l, n, m = len(text), 0, 0
  x, y = math.floor(math.sqrt(l)), math.ceil(math.sqrt(l))
  if x*y < l:
    n, m = y, y
  else:
    n, m = x, y
  
  matrix = [[None for _ in range(m)] for _ in range(n)]
  '''
  steps left:
   - fill in grid by iterating through string, using a bit of math to find row and column numbers
   - construct array of columns
   - concat columns
  '''
if __name__ == "__main__":
  file_name = sys.argv[1]
  f = open(file_name, 'r')
  print(cipher(f.readline().rstrip()))
  f.close()
