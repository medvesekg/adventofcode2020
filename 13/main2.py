import math

is_prime_cache = {}
prime_generator_cache = []

def prime_factors(number):
    prime_factors = []
    primes = generate_primes()
    prime = next(primes)
    while not is_prime(number):
        if number % prime == 0:
            prime_factors.append(prime)
            number //= prime
        else:
            prime = next(primes)
    prime_factors.append(number)
    return prime_factors

def prime_factors_by_power(number):
    by_power = {}
    for prime in prime_factors(number):
        if prime not in by_power:
            by_power[prime] = 0
        by_power[prime] += 1
    return by_power

def generate_primes():

    prime = 1

    for prime in prime_generator_cache:
        yield prime

    i = prime + 1
    while True:
        if is_prime(i):
            yield i
        i += 1


def is_prime(number):

    if number in is_prime_cache:
        return number

    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, math.ceil(number / 2), 2):
        if number % i == 0:
            return False

    if number not in is_prime_cache:
        is_prime_cache[number] = True

    return True


def least_common_multiple(numbers):
    highest_prime_factor_powers = {}
    for number in numbers:
        for prime, power in prime_factors_by_power(number).items():

            if prime not in highest_prime_factor_powers:
                highest_prime_factor_powers[prime] = power
            if highest_prime_factor_powers[prime] < power:
                highest_prime_factor_powers[prime] = power
    lcm = 1
    for number, power in highest_prime_factor_powers.items():
        lcm *= pow(number, power)
    return lcm

def greatest_common_divisor(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    return greatest_common_divisor(b, remainder)


def multiplier_offsets(number1, number2):
    multiple1 = number1
    multiple2 = number2
    offsets = []
    offset = None
    while offset != 0:
        while multiple2 < multiple1:
            multiple2 += number2

        offset = multiple2 - multiple1
        offsets.append(offset)
        multiple1 += number1

    return offsets

def prepare(numbers):
    origin = numbers[0]['num']
    arr = []
    for number in numbers[1:]:
        n = number['num']
        offset = number['offset']
        offsets = multiplier_offsets(origin, n)
        repeat = len(offsets)
        #factor = offsets.index(offset) + 1
        index = offsets.index(offset)
        arr.append({
            'offsets': offsets,
            #'factor': factor,
            'repeat': repeat,
            'index': index
        })
    return arr



with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


numbers = [{'num': int(id), 'offset': index if index < int(id) else index % int(id) } for (index, id) in enumerate(lines[1].split(',')) if id != 'x']

origin = numbers[0]['num']


p = prepare(numbers)

m_repeat = p[0]['repeat']
m_index = p[0]['index']


for item in p[1:]:
    offsets = item['offsets']
    repeat = item['repeat']
    index = item['index']

    i = 0
    hit = offsets[((i * m_repeat) + m_index) % repeat]
    while hit != offsets[index]:
        i += 1
        hit = offsets[((i * m_repeat) + m_index) % repeat]

    m_index = (i * m_repeat) + m_index
    m_repeat = least_common_multiple([m_repeat, repeat])

print((m_index + 1) * origin)

