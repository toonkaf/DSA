"""Longest Common Substring"""
def LCS(word_a,word_b):
    cell = [[ 0 for _ in range(len(word_a))] for _ in range(len(word_a))]
    long_common = 0
    row_common = 0
    for i in range(len(word_a)):
        for j in range(len(word_a)):
            if word_a[i] == word_b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            if cell[i][j] > long_common:
                long_common = cell[i][j]
                row_common = i
    if long_common > 0:
        print(word_a[row_common - long_common+1: row_common+1])
        print(long_common)
    else:
        print("No common substring.")

LCS(input(),input())