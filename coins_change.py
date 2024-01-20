# def change(s, coins_remaining, coins_used):
#     if s == 0:
#         return [coins_used]
#     if s < 0:
#         return None
#     # we know that s > 0
#     if len(coins_remaining) == 0:
#         return None
#     result1 = change(s, coins_remaining[0:len(coins_remaining) - 1],coins_used)
#     result2 = change(s - coins_remaining[-1], coins_remaining,coins_used + [coins_remaining[-1]])
#     result = []
#     if result1 is not None:
#         result += result1
#     if result2 is not None:
#         result += result2
#     return None if len(result) == 0 else result

# def change(s, coins_remaining):
#     if s <= 0 or (s > 0 and len(coins_remaining) == 0):
#         return [[]]
#     change1 = change(s, coins_remaining[0:len(coins_remaining) - 1])
#     change2 = change(s - coins_remaining[-1], coins_remaining)
#     result = []
#     for c in change1:
#         if sum(c) == s:
#             result.append(c)
#     for c in change2:
#         if sum(c) == s - coins_remaining[-1]:
#             result.append(c + [coins_remaining[-1]])
#     return result

def change(s, coins_remaining, mem):
    mem_key = str(s) + "_"
    coins_remaining_sorted = sorted(coins_remaining)
    for c in coins_remaining_sorted:
        mem_key += "_"
        mem_key += str(c)
    if mem_key in mem:
        return mem[mem_key]
    if s <= 0 or (s > 0 and len(coins_remaining) == 0):
        return [[]]
    change1 = change(s, coins_remaining[0:len(coins_remaining) - 1], mem)
    change2 = change(s - coins_remaining[-1], coins_remaining, mem)
    result = []
    for c in change1:
        if sum(c) == s:
            result.append(c)
    for c in change2:
        if sum(c) == s - coins_remaining[-1]:
            result.append(c + [coins_remaining[-1]])
    mem[mem_key] = result
    return result

mem = {}
s = 5
coins = [1, 2 , 3]
print(change(s, coins, mem))
print(mem)
