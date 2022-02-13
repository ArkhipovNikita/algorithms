from typing import List


def solve(shops: List[int], storages: List[int]) -> int:
    shops.sort()
    storages.sort()

    return sum(map(lambda e: abs(e[0] - e[1]), zip(shops, storages)))


f = open('/Users/arkhipov/Downloads/shops2.in', 'r')
f.readline()
shops_ = list(map(int, f.readline().strip(' \n').split(' ')))
storages_ = list(map(int, f.readline().strip(' \n').split(' ')))

print(solve(shops=shops_, storages=storages_))
