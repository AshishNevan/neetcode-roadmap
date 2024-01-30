memo = [-1] * 100
memo[0], memo[1] = 0, 1


def nth_fibonacci(n: int) -> int:
    if n <= 1:
        memo[n] = n
        return n
    if memo[n] != -1:
        return memo[n]
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


print(nth_fibonacci(10))
print(memo)
