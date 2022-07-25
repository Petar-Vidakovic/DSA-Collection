# CA4

def convertNumToBaseArr(num, base):
    results = []
    while True:
        results.append(num % base)
        if num < base:
            break
        num //= base
    return results[::-1]


def converter(age, base):
    global resInts
    resList = convertNumToBaseArr(age, base)
    result = [str(k) for k in resList]

    # check if items is too high 1B, 1C, etc
    for item in resList:
        if item > 9:
            return False
    resStr = "".join(result)
    resInts = int(resStr)
    return resInts


def bSearch(age, target):
    l, r = 10, age
    decimalResults = []
    while l < r:
        mid = (r + l) // 2
        result = converter(age, mid)

        if result == target:
            return result, mid  # return True
        elif not result:
            r = mid             # reduce ceiling
        elif result > target:
            l = mid             # raise floor
        elif result < target:
            r = mid

        if result:
            # append decimal results and sort for closest to target
            decimalResults.append((result, mid))
            # print(lst)
            if len(decimalResults) > 10:
                decimalResults.sort()
                return decimalResults[0]
    return False


# age, target
result = bSearch(2016, 100)
print(result)

# l = 10
# r = 31
# 31+10//2 == 21 (mid)
# check age with base 21 (too high)
# new ceiling
# r = 21, l = 10
# (21+10)//2 = 15 (22, decimal > )
# new floor, answer must be between 15 and 21
# r = 21, l = 15
# (21 + 15)// 2 = 18
# check age with base 18 (too high)
# new ceiling
# r = 18, l = 15
# (18+15)//2 == 16
# check age with base 16 (correct)
