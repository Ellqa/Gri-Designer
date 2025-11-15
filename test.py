from math import isqrt

def prime_power_factorization(n: int):
    """
    Return a list of (prime, exponent) for n >= 2.
    Example: 360 -> [(2, 3), (3, 2), (5, 1)]
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an integer >= 2")

    factors = []

    # factor out 2s
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    if a:
        factors.append((2, a))

    # factor odd primes up to sqrt(n)
    p = 3
    while p <= isqrt(n):
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        if a:
            factors.append((p, a))
        p += 2

    # any leftover n is prime
    if n > 1:
        factors.append((n, 1))

    return factors

def format_as_product(factors):
    """
    Turn [(p,a), ...] into a string like '2^3 * 3^2 * 5'.
    """
    parts = []
    for p, a in factors:
        parts.append(f"{p}^{a}" if a > 1 else f"{p}")
    return " * ".join(parts)

# --- examples ---
# nums = [360, 999983, 2*3*3*7*7*7, 10**12]  # try a few
# for n in nums:
#     f = prime_power_factorization(n)
#     print(n, "->", f, "->", format_as_product(f))


def get_prime_factors_by_input():
    a = input("Enter a number: ")
    b = prime_power_factorization(int(a))
    print(a, "->", b, "->", format_as_product(b))


get_prime_factors_by_input()
#### ---------------------------------------------------------------

def find_common_prime_factors(x, y):
    """
    input: x(int), y(int)
    output: common_prime_factors(list of int)
    """
    x_factors = prime_power_factorization(x)
    y_factors = prime_power_factorization(y)
    common_prime_factors = []
    y_prime_factors = []
    for y_factor in y_factors:
        y_prime_factors.append(y_factor[0])
    for x_factor in x_factors:
        if x_factor[0] in y_prime_factors:
            common_prime_factors.append(x_factor[0])
    return common_prime_factors


# a = find_common_prime_factors(1280, 2560)
# print(a)

def find_module(common_prime_factors):
    m = input(print(f'Choose one module from the following lists: {common_prime_factors}'))
    if int(m) in common_prime_factors:
        print(f'Set module to {m} pt')
        return int(m)
    else:
        print("Invalid input")
        return find_module(common_prime_factors)

# find_module(a)


def find_grid_size(x,y,module):
    x_factors = prime_power_factorization(x)
    y_factors = prime_power_factorization(y)

    x_x_factor = []
    y_y_factor = []
    for x_factor in x_factors:
        x_x_factor.append(x_factor[0])
    for y_factor in y_factors:
        y_y_factor.append(y_factor[0])
    if module not in x_x_factor and module not in y_y_factor:
        print("Invalid module")
        return find_grid_size(x,y,module)
    else:
        return module

def align_to_grid(x, y, module, l, r, t, b, c_spacing, r_spacing):
    """
    input: x(int), y(int), left margin(int), right margin(int), top margin(int), bottom margin(int), column spacing(int), row spacing(int).
    output: 
        possible grid size, rows and columns.
    """
    return 0

def find_column_number(y, t, b, c_spacing, grid_size):
    column_number = []
    for c in range(1, 31):
        if (y - t - b - (c - 1) * c_spacing) % (grid_size * c) == 0:
            column_number.append(c)
    return column_number

a = find_column_number(1224, 24, 24, 24, 24)
print(a)



