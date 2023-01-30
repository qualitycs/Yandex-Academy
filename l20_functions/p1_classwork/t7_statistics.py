def print_statistics(arr):
    import statistics
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
    else:
        print(len(arr))
        print(statistics.mean(arr))
        print(min(arr))
        print(max(arr))
        print(statistics.median(arr))
