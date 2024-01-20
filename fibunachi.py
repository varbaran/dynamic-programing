def fibonachi(l, mem):
    if l == 0 or l == 1:
        return 1
    fib_n_1 = 0
    fib_n_2 = 0
    if l - 1 not in mem:
        fib_n_1 = fibonachi(l - 1, mem)
    else:
        fib_n_1 = mem[l - 1]
    if l - 2 not in mem:
        fib_n_2 = fibonachi(l - 2, mem)
    else:
        fib_n_2 = mem[l - 2]
    mem[l] = fib_n_2 + fib_n_1
    return mem[l]


l = int(input())
memory = {}
result = fibonachi(l, memory)
print(memory)
print(result)
