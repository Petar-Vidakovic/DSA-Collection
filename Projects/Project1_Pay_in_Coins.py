import sys
from timeit import default_timer as timer


def getCoinsEtc(values):
    amount = 0          # target amount
    terms = 0           # terms per sum
    coins = []          # list of coin denominations (1 + primes up to and including amount)

    # generating data from the txt
    if len(values) == 1:
        amount = int(values[0])
        terms = [x for x in range(1, int(amount) + 1)]
        coins = [x for x in range(2, int(values[0]) + 1) if all(x % y != 0 for y in range(2, x))]
        coins.insert(0, 1)
        if int(values[0]) not in coins:
            coins.append(int(values[0]))

    if len(values) == 2:
        amount = int(values[0])
        terms = [int(values[1])]
        coins = [x for x in range(2, int(values[0]) + 1) if all(x % y != 0 for y in range(2, x))]
        coins.insert(0, 1)
        if values[0] not in coins:
            coins.append(int(values[0]))

    if len(values) == 3:
        amount = int(values[0])
        terms = [x for x in range(int(values[1]), int(values[2]) + 1)]
        coins = [x for x in range(2, int(values[0]) + 1) if all(x % y != 0 for y in range(2, x))]
        coins.insert(0, 1)
        if values[0] not in coins:
            coins.append(int(values[0]))

    # returns
    return amount, terms, coins


def getSubsetBoundByTerms(coins, amount, terms):
    comboSumToAmount = set()

    def checkSubsetSum(subset):
        for coin in coins:
            if sum(subset + [coin]) < amount and len(subset) < terms:
                checkSubsetSum(subset + [coin])
            elif sum(subset + [coin]) == amount and len(subset) == terms-1:
                comboSumToAmount.add(tuple(sorted(subset + [coin])))

    checkSubsetSum([])
    return comboSumToAmount


# if sys.argv[0] != "input.txt":
#     print("Bad file name, input -> python3 s5240487_Pay_in_Coins input.txt")
#     quit()

# get the lines from the input files
with open("input.txt", "r", encoding='utf-8') as fd:
    lines = fd.readlines()

problemContainer = {}
n = 0
for i in range(len(lines)):
    problemContainer[f"line {n}"] = lines[i].split()
    n += 1

# loop through the lines in dict
for lineN in range(len(problemContainer)):
    uniqueSetStorage = []
    amount, coinsToUse, coins = getCoinsEtc(problemContainer[f'line {lineN}'])

    # little cheats to exclude coins that don't get used
    if 1 not in coinsToUse and int(amount) in coins:
        coins.remove(int(amount))
    # removing coins off the back if they don't need to be used anymore
    # if int(amount) - coins[-1] < int(coinsToUse[0]) and int(amount) - coins[-1] != 0:
    #     coins.remove(coins[-1])

    print(f'line:{lineN}\n'
          f'Amount: {amount}\n'
          f'Terms:{coinsToUse}\n'
          f'Coins: {coins}')

    # work done in here
    start = timer()
    for terms in coinsToUse:
        subSets = (getSubsetBoundByTerms(coins, int(amount), int(terms)))
        print(subSets)
        uniqueSetStorage.append(subSets)

    flattenList = [item for sublist in uniqueSetStorage for item in sublist]
    print(f'{amount} can be made up {len(flattenList)} ways using {coinsToUse} terms')
    stop = timer()
    print(f'found in {stop - start:0.5f} seconds\n')

