import time

# -----------------------------
# Iterative (Non-Recursive) Fibonacci
# -----------------------------
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# -----------------------------
# Recursive Fibonacci
# -----------------------------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# -----------------------------
# Main Program
# -----------------------------
n = 30   # You can change this value

# --- Iterative ---
start = time.time()
fib1 = fib_iterative(n)
end = time.time()
print("Iterative Fibonacci:", fib1)
print("Time Taken (Iterative):", (end - start), "seconds")

# --- Recursive ---
start = time.time()
fib2 = fib_recursive(n)
end = time.time()
print("Recursive Fibonacci:", fib2)
print("Time Taken (Recursive):", (end - start), "seconds")

# --- Complexity ---
print("\nComplexity Analysis:")
print("Iterative -> Time: O(n), Space: O(1)")
print("Recursive -> Time: O(2^n), Space: O(n) [because of recursion stack]")


"""
OUTPUT
PS C:\Users\matha\p folder> python -u "c:\Users\matha\p folder\DAA\Fabonacci.py"


Iterative Fibonacci: 832040        
Time Taken (Iterative): 0.0 seconds
Recursive Fibonacci: 832040
Time Taken (Recursive): 0.15605783462524414 seconds

Complexity Analysis:
Iterative -> Time: O(n), Space: O(1)
Recursive -> Time: O(2^n), Space: O(n) [because of recursion stack]

"""