from typing import List


def arrange_gas_stations(n: int, s: int, v: int, gas_stations: List[int]) -> int:
    res = []
    current_v = v
    stops = [0]
    stops.extend(gas_stations)
    stops.append(s)

    for i in range(1, len(stops) - 1):
        current_v -= (stops[i] - stops[i - 1])
        if current_v - (stops[i + 1] - stops[i]) < 0:
            current_v = v
            res.append(stops[i])

    return len(res)
