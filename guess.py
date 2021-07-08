import itertools

s = 'HRISBAD'
s = sorted(list(s))
n = 6

result = []
for x in range(2):
    y = sorted([''.join(i) for i in itertools.combinations(s, x + 1)])
    result.extend(y)
    
for r in result:
    print(r)