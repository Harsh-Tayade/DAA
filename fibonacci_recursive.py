def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(fibonacci(i))
