def isvalid(input):

    s = []
    match = {'(': ')', '{':'}', '[':']'}

    for p in input:
        if p in match:
            s.append(p)
        elif not s or match[s[-1]] != p:
            return False
        else:
            s.pop()
    return True

input = '{[]}'
torf = isvalid(input)
print(torf)
