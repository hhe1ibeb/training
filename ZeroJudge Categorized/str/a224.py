try:
    while True:
        inp = list(input()); valid = []
        isReverse = True; isOdd = False; isSingleTaken = False
        for i in inp:
            if ord(i) >= 65 and ord(i) <= 122:
                i = i.lower()
                valid.append(i)

        if len(valid) % 2 != 0:
            isOdd = True

        for j in valid:
            if valid.count(j) % 2 == 0:
                pass
            else:
                if isOdd:
                    if isSingleTaken == False:
                        isSingleTaken = True
                        valid.remove(j)
                    else:
                        isReverse = False
                        break
                else:
                    isReverse = False
                    break
        
        if isReverse:
            print('yes !')
        else:
            print('no...')
except EOFError:
    pass