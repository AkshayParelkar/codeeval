import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = int(test)
    #print "num: " + str(num)
    iter = 0
    sumSq = 0
    found = 0
    while (found != 1 and iter < 1000):
        while num > 0:
            sumSq += pow(num%10, 2)
            num = int(num/10)
        if (sumSq == 1):
            found = 1
            print "1"
        num = sumSq    
        sumSq = 0    
        iter += 1
    if (iter >= 1000 and found != 1):
       print "0"
            
test_cases.close()

