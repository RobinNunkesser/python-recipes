calls = 0

def	fib(n):
    global calls
    calls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def	fib_efficient(n, d):
    global calls
    calls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return	ans

calls = 0
d = {1:1, 2:2}
print(fib_efficient(34, d))
print(calls)

calls = 0
print(fib(34))
print(calls)