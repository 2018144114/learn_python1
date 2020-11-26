n=0
m=0
while 1:
    i = input('please enter  numbers\n')
    if i == 'done':
        j = 1
        break
    try:
        b = int(i)
        n = n + 1
        m = m + b
        avg = m/n
    except:
        print('com')
        continue
print(n)
print(m)
print(avg)

