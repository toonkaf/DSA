"""Calculator"""
def calculator(n):
    """---"""
    count = 0
    if n != 1:
        for i in range(1,n+1):
            count += len(str(i))+1
    else:
        count = 1
    return count

print(calculator(int(input())))