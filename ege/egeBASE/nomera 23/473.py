def f(start,stop):
    if start>stop or start == 43:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start+2,stop) + f(start+(start-1),stop) + f(start+start+1,stop)
print(f(7,63))