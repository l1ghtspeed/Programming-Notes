'''
Problem:

Given a rotated, sorted array (shifted a certain number of times), 
find the index of a given number in that array.

Think about since it's sorted we can do binary search, but first we must find
the number of shifts we have to offset by.

'''


def search(arr, l, h, key): 
    if l > h: 
        return -1
      
    mid = (l + h) // 2
    if arr[mid] == key: 
        return mid 
  
    # If arr[l...mid] is sorted  
    if arr[l] <= arr[mid]: 
  
        # As this subarray is sorted, we can quickly 
        # check if key lies in half or other half  
        if key >= arr[l] and key <= arr[mid]: 
            return search(arr, l, mid-1, key) 
        return search(arr, mid+1, h, key) 
  
    # If arr[l..mid] is not sorted, then arr[mid... r] 
    # must be sorted 
    if key >= arr[mid] and key <= arr[h]: 
        return search(a, mid+1, h, key) 
    return search(arr, l, mid-1, key) 

print(search([2, 3, 4, 5, 6, 1], 0, 5, 5))