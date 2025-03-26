def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:  # Fixed by Samar
        return 0
    elif n == 2:  # Fixed by Samar
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):  # Fixed by Samar
        a, b = b, a + b
    return b  # Fixed by Samar

n = 10
print(f"The {n}th Fibonacci number is: {fibonacci_iterative(n)}")



#edited by samar
