with open('24 (6).txt') as f:
    st = f.readline()
    st = st.replace('ABA', '*').replace("AAA", '*').replace('ACA', "*").replace('CAC', '*').replace('CBC', "*").replace('CCC', '*')
    cnt = 0
    cur = -1
    for i in range(len(st)-1):
        if st[i] == "*" and st[i+1] == '*':
            cnt += 1
        else:
            cur = max(cnt, cur)
            cnt = 0
    print(cur)