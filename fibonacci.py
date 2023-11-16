def fibonacci(n):
    fib = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

if __name__ == "__main__":
    num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(fibonacci(i))
