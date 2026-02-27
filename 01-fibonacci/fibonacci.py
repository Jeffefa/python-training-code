
def get_fibonacci(n):
    if n < 0:
        raise ValueError("Number must be greater than or equal to 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        c = None
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return c

def get_fibonacci_v2(n):
    """
    This is a recursive solution to the Fibonacci sequence. 
    It is not efficient for large values of n, as it will have a time complexity of O(2^n).
    """
    if n < 0:
        raise ValueError("Number must be greater than or equal to 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci_v2(n - 1) + get_fibonacci_v2(n - 2)

if __name__ == "__main__":
    n = int(input('Enter a number: ').strip())
    res = get_fibonacci(n)
    print(f'The Fibonacci sequence of f({n}) is {res}')