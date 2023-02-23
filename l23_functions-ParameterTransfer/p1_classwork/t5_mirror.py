def mirror(arr):
    arr[:] = arr + arr[::-1]
    return arr
