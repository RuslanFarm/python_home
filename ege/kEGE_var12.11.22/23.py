def f(s, e):
    if s>e: return 0
    elif s == e: return 1
    return f(s+1, e)+f(s+2,e) +f(s*2,e)
print(f(3,25))
#28657 + 1 + 28
print(43776-28657-1-28)