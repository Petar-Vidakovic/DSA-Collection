import itertools
import math
import time

# function that finds all prime factors of a given number
def prime_factors(n):
    factors = set()  # using a set to remove duplicates
    # for even numbers
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    # for odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i

    # if n is prime
    if n > 2:
        factors.add(n)
    return list(factors)


# function that returns all combinations of a given list
def find_combinations(nums):
    return itertools.chain.from_iterable(itertools.combinations(nums, n) for n in range(1, len(nums) + 1))


def find_coprimes(i, range_upper):
    factors = prime_factors(i)
    # if there are more than one prime factors of a given number
    if len(factors) > 1:
        common_factors = 0
        # get all combinations of the prime factors
        for combination in find_combinations(factors):
            # find the product of the combination
            product = math.prod(combination)
            # if the length of the combination is even then subtract
            if len(combination) % 2 == 0:
                common_factors -= range_upper // product
            # if odd then add
            else:
                common_factors += range_upper // product
        # else only one prime factor exists
        return range_upper - common_factors
    # else only one prime factor exists
    else:
        return range_upper - (range_upper // factors[0])


def main():
    line_1 = input('Line 1: ').split()
    line_2 = input('Line 2: ').split()
    start_time = time.time()
    total = 0
    lower = int(line_2[0])
    upper = int(line_2[1])

    # loop through first interval
    for i in range(int(line_1[0]), int(line_1[1]) + 1):
        # if i is 1 then just add the length of the second interval to total
        # as all numbers are relatively prime with 1
        if i == 1:
            total += upper - lower + 1
        else:
            # if the lower bound is greater than 1, find the difference between 1 and lower, and lower and upper
            if lower > 1:
                total += (find_coprimes(i, upper) - find_coprimes(i, lower - 1))
            # otherwise just find the total co-primes of the range
            else:
                total += find_coprimes(i, upper)
    print('Output:', total)
    print('Execution time: %s seconds\n' % ('{:.4f}'.format(time.time() - start_time)))


if __name__ == "__main__":
    main()
