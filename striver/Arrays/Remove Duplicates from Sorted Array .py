def removeDuplicates(arr,n):
    # First pointer.
    i = 0

    # Second pointer traversing from 1 to n.
    for j in range(1, n):
        # If not duplicates increment first pointer and check again.
        if (arr[j] != arr[j-1]):
            arr[i] = arr[j]
            i += 1
    
    # Return length == (index of first pointer when second reaches end) + 1.
    return i + 1
        