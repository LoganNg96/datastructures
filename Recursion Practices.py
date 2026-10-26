
def factorial(n):
    if n == 1:
        return 1
        # Base case: return what?

    # Recursive case: multiply n by the factorial of n - 1
    return n * factorial(n - 1) 


print(factorial(4))
