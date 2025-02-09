"""isIntersect"""
import json
def isintersect(a,b,c):
    """---"""
    checker = False
    for i in a:
        if i in b and i in c:
            checker = True
            break
    return checker

print(isintersect(json.loads(input()),json.loads(input()),json.loads(input())))
