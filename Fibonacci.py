def total_rabbit_pairs(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return total_rabbit_pairs(n - 1, k) + k * total_rabbit_pairs(n - 2, k)

# Test the function with n=40 and k=5
n = 33
k = 5
print(total_rabbit_pairs(n, k))
