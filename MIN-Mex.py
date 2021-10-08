for t in range(int(input())):
    s = input()
    z = s.count('0')
    if z== 0:
        print(0)
        continue
 
    first = s.find('0')
    last = s.rfind('0')
 
    if last - first + 1 == z:
        print(1)
    else:
        print(2)
