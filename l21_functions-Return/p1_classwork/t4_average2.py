def average(values):
    import statistics
    if len(values) == 0:
        return 0
    else:
        return statistics.mean(values)
