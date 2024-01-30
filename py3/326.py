def isPowerOfThree(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return isPowerOfThree(n / 3)
