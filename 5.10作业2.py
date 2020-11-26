j=0
while 1:
    i = input('please enter  numbers\n')
    if i == 'done':
        break
    try:
        b = int(i)
        if j==0:
            n=b
            m=b
            j+=1
        if b>n:
            n=b
        if b<m:
            m=b
    except:
        print('com')
        continue
print('max=',n)
print(m)
