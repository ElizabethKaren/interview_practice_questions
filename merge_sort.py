array = [38, 27, 43, 3, 9, 82, 10]

# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:  
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:   
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)

def merge_sort(array, left=0, right=len(array)-1):
    print(left, right)
    if left == right:
        return array 
    middle = int((left+right)/2)
    merge_sort(array, middle +1, right)
    merge_sort(array, left, middle)
    merge(array,left, middle,right)

#array = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(arr, 0, 6)
# merge_sort(arr, 4,6)
# merge_sort(arr, 4,5)

def merge(arr, start, mid, end):
    start2 = mid + 1
    if (arr[mid] <= arr[start2]): 
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]: 
            start += 1
        else: 
            value = arr[start2] 
            index = start2 
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while index != start: 
                arr[index] = arr[index - 1] 
                index -= 1 
            arr[start] = value 
            # Update all the pointers 
            start += 1 
            mid += 1 
            start2 += 1 
        


merge_sort(array)
print(array)