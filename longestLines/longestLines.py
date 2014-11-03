import sys

i = 0
longestLines = []
limit = 0
strings = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if (i == 0):
        limit = int(test)
        longestLines = [0 for i in range(limit)]
    else:
        strings.append(test)

test_cases.close()
lines = [0 for m in range(limit)]                        
for i in range(len(strings)):
    for j in range(limit):
        if len(strings[i]) > longestLines[j]:
            for k in range(limit-1, j-1, -1):
                longestLines[k] = longestLines[k-1]
                lines[k] = lines[k-1]
            longestLines[j] = len(strings[i])
            lines[j] = i
            break

for i in range(limit):
    print strings[lines[i]],
