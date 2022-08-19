def sekans(arr: list):
    long = len(arr)
    k = long
    while k > 0:
        arr = list(reversed(arr[0:k])) + arr[k: long]
        k = k-1
        print(arr)
        print(3, "with the index of", arr.index(3))

    return arr


sekans([0, 1, 2, 3, 4])
