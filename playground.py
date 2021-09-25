mydict = {
    "carl": [40, 2],
    "alan": [2, 3],
    "bob": [2, 1],
    "danny": [3, 4],
}

#print(mydict.items())
#print(sorted(mydict.items(), key=lambda x:x[0]))
#print(sorted(mydict.items(), key=lambda x:x[1][0], reverse=True))
#print(sorted(mydict.items(), key=lambda x: [-x[1][0], x[0]], reverse=False))
#print(ord('a'))

#from collections import deque

#queue = deque([1, 2])

#print(queue.popleft())

from collections import defaultdict

mydict = defaultdict(int)

mydict[1] = 1
mydict[2] = 7
mydict[3] = -1

print(mydict.items())
print(max(mydict.items(), key=lambda k:k[1]))