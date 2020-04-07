with open("test.txt","r+")as r:
    with open("test_new.txt","w+")as r1:
        linenum = 0
        high = ""
        low = ""
        for line in r:
            if linenum ==0:
                low = line
                linenum=1
            elif  linenum ==1:
                high = line.strip('\n')
                linenum=2
            elif linenum==2:

                linenum = 1
                full = high+low
                low = line
                r1.write(full)


