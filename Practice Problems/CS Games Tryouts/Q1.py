import sys

def sort_and_print(arr):
  arr.sort(reverse = True)
  for num in arr:
    print(num)

if __name__ == "__main__":
  file_name = sys.argv[1]
  f, arr = open(file_name, 'r'), []
  for line in f:
    arr.append(int(line.rstrip()))
  f.close()
  sort_and_print(arr[1:])