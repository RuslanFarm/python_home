def f(start, step, stop):
    if start > step or start == stop:
        return 0
    elif step == stop:
        return 1
    else:
        return f(start, step + 1, stop) + f(start, step+2, stop)
print(f(11,17,29))