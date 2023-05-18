q = 'tenet'
for i in range(len(q)):
    if q[i] == q[-(i+1)]:
        print('yes')
    else:
        print('no')
