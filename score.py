# -*- coding: utf-8 -*-
"""score.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OyARrt3WEjJN2oeXKLPdZaDCBY3-pCx-
"""

def count(score_list):
    total = 0
    for i in score_list:
        total += i
    return total
score_list = list(map(int, input().split()))
answer = count(score_list)
average = answer // len(score_list)
print(average)