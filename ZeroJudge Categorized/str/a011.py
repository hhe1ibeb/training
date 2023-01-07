try:
    while True:
        s = input()
        for i in s:
            if i.isalpha() == False and i.isspace() == False:
                s = s.replace(i, ' ')
        s = s.split()
        print(len(s))
except EOFError:
    pass