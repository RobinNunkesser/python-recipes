import time

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
t0 = time.time()
print(fib_efficient(34, d))
print(calls)
t1 = time.time() - t0
print("t =", t0, ":", t1, "s,")

calls = 0
t0 = time.time()
print(fib(34))
print(calls)
t1 = time.time() - t0
print("t =", t0, ":", t1, "s,")
