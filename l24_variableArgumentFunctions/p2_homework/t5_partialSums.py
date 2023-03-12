def partial_sums(*nums):
    import itertools
    sneedlist = list(itertools.accumulate(nums))
    sneedlist.insert(0, 0)
    return sneedlist
