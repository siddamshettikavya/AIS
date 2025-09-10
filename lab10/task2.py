def find_common(a, b):
    set_b = set(b)
    res = []
    for item in a:
        if item in set_b:
            res.append(item)
    return res
print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(['a', 'b', 'c'], ['b', 'c', 'd']))
print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))
print(find_common(['x', 'y', 'z'], ['a', 'b', 'c']))




