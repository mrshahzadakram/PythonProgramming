def calculate_unfairness(a, k):
    i = 0
    a.sort()
    n = len(a)
    m = a[n - 1]
    while i < n - k:
        if a[i + k - 1] - a[i] < m:
            m = a[i + k - 1] - a[i]
        i += 1
    return m


a = [25, 120, 350, 150, 123, 2500, 125, 35]
k = 3
print(calculate_unfairness(a, k))

arr = [1, 4, 7, 2]
k = 2
print(calculate_unfairness(arr, k))
