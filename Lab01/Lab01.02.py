"""Max...Min...Avg"""
import json
def mma(lst):
    """mma"""
    m_ax , m_in = 0,1000000000000000000000000000
    s = 0
    for i in lst:
        if round(i,2) > m_ax:
            m_ax = round(i,2)
        if round(i,2) < m_in:
            m_in = round(i,2)
        s += round(i,2)
    avg = round(s / len(lst),2)
    print(f"({m_ax}, {m_in}, {avg})")

mma(json.loads(input()))
