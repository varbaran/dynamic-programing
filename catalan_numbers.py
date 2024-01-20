def catalan_numbers(a, catalan):
    n = a - 1
    if a <= 1:
        return 1
    if a < len(catalan):
        return catalan[a]
    c = 0
    for i in range(a):
        ci = 0
        if i < len(catalan):
            ci = catalan[i]
        else:
            ci = catalan_numbers(i, catalan)
        cn_i = 0
        if n - i < len(catalan):
            cn_i = catalan[n - i]
        else:
            cn_i = catalan_numbers(n - i, catalan)

        c += ci * cn_i
    catalan.append(c)
    return c

a = 20
catalan = [1, 1]
print(catalan_numbers(a, catalan))
print(catalan)