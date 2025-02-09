"""Summation (แบบที่ 1)"""
def main(n):
    """loop"""
    x = 0
    for i in range(1,n+1):
        x += i
    print(x)
main(int(input()))
