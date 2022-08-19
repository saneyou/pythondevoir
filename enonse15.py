def findBetween(a: str):
    a1 = a.rsplit('hidden')[1]
    a2 = a1.rsplit('endpass')[0]
    return a2

print(findBetween("yon fraz ki ant hidden ki probablement se yon fraz ak endpass ki ka yon fraz tou"))