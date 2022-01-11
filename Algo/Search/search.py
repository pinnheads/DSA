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


if __name__ == "__main__":
    print(linear_search(20, [10, 20, 30, 40, 50]))