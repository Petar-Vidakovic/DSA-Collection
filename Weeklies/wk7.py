# ca5 Social Distance
import math


def distanceFormula(x1, x2, y1, y2):
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return d


def findSmallestDist(locations):
    locations.sort()
    dist = distanceFormula(locations[-2][0], locations[-1][0], locations[-2][1], locations[-1][1])
    return locations[-2], locations[-1]


def main():
    pairs = []
    locations = [(0, 0), (3, 2), (4, 1)]                # out:13
    # locations = [(1, 1), (5, 5), (2, 2), (4, 4)]      # out:8
    # locations = [(-1, 3), (3, 4), (-2, -1)]           # out: 17

    locations.sort()
    print(f'locations:{locations}')
    a, b = findSmallestDist(locations)
    pairs.append((a, b))
    locations.remove(a), locations.remove(b)

    r = distanceFormula(locations[-1][0], pairs[0][0][0], locations[-1][1], pairs[0][0][1])
    print(f'Social distance factor:{r ** 2:0.0f}')


if __name__ == '__main__':
    main()
