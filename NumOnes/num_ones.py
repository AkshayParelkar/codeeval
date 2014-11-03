import sys

i = 0
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    try:
        num = int(test)
    except ValueError:
        num = None

    if num != None:
        while num > 0:
            if num%2==1:
                i += 1
            num = int(num/2)
    print i
    i = 0
            
        