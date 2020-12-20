import time
import sys
from memory_profiler import profile

sys.setrecursionlimit(100000)


@profile
def print_and_time(l, a):
    print("------------------------------")
    print("Executing %s(%s)" % (l.__name__, a))
    time_1 = time.time()
    res = l(a)
    print("Execution time: %s seconds" % (time.time() - time_1))
    print("Result: %s" % (res))
    print("------------------------------\n\n")

def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_memo(n, memo = {'1': 1, '2': 1}):
    key = str(n)
    if key in memo:
        return memo[key]
    memo[key] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[key]

def fib_memo_list(n, memo = []):
    if not memo or len(memo) < 2:
        memo = [0] * (n+2)
    memo[1] = 1
    memo[2] = 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib_memo_list(n-1, memo) + fib_memo_list(n-2, memo)
    return memo[n]

def fib_loop(n):
    a, b = 1, 1
    idx = 2
    while (idx < n):
        a, b = b, a+b
        idx += 1
    return b

def fib_table(n):
    table = [0] * (n+2)
    table[1] = 1

    for i in range(0, n):
        table[i+1] += table[i]
        table[i+2] += table[i];

    return table[n]


print_and_time(fib_rec, 10)
print_and_time(fib_memo, 2000)
print_and_time(fib_loop, 2000)
print_and_time(fib_table, 2000)
print_and_time(fib_memo_list, 2000)
