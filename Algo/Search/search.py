def linear_search(val, arr):
    '''
    Linear Search Method to search for a element when the element to search and
    a list are given.

    params:
        Array/List - List of elements to search from
        Value - Element to be searched

    returns:
        Index of the element found else -1
    '''
    for index in range(0, len(arr)):
        if arr[index] == val:
            return index
    return -1


def binary_search(val, arr):
    '''
    Binary Search Method to search for a element when the element to search and
    a list are given.

    params:
        Array/List - Sorted List of elements to search from
        Value - Element to be searched

    returns:
        Index of the element found else -1
    '''
    if arr != sorted(arr):
        raise ValueError("Not a sorted list")
    
    beg, end = 0, len(arr) - 1

    while beg <= end:
        mid = (beg+end) // 2

        if arr[mid] == val:
            return mid

        elif arr[mid] >= val:
            end = mid - 1
        
        else:
            beg = mid + 1
        
    return -1


if __name__ == "__main__":
    print(f"Linear search {linear_search(22, [21, 22, 23, 25, 27, 29])}")
    print(f"Binary search: Sorted List {binary_search(22, [21, 22, 23, 24, 25, 26])}")
    print(f"Binary search: Unsorted List {binary_search(22, [21, 22, 23, 24, 26, 25])}")
