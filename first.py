__author__ = 'dev'


# print formatting replacements in python 2 vs 3

for i in range(1, 20):
    print('No. %2d squared is %4d and cubed is %4d' % (i, i ** 2, i ** 3))

for i in range(1, 20):
    print('No. {0:2} squared is {1:4} and cubed is {2:4}'.format(i, i ** 2, i ** 3))

'''
No.  1 squared is    1 and cubed is    1
No.  2 squared is    4 and cubed is    8
No.  3 squared is    9 and cubed is   27
No.  4 squared is   16 and cubed is   64
No.  5 squared is   25 and cubed is  125
No.  6 squared is   36 and cubed is  216
No.  7 squared is   49 and cubed is  343
No.  8 squared is   64 and cubed is  512
No.  9 squared is   81 and cubed is  729
No. 10 squared is  100 and cubed is 1000
No. 11 squared is  121 and cubed is 1331
No. 12 squared is  144 and cubed is 1728
No. 13 squared is  169 and cubed is 2197
No. 14 squared is  196 and cubed is 2744
No. 15 squared is  225 and cubed is 3375
No. 16 squared is  256 and cubed is 4096
No. 17 squared is  289 and cubed is 4913
No. 18 squared is  324 and cubed is 5832
No. 19 squared is  361 and cubed is 6859

No.  1 squared is    1 and cubed is    1
No.  2 squared is    4 and cubed is    8
No.  3 squared is    9 and cubed is   27
No.  4 squared is   16 and cubed is   64
No.  5 squared is   25 and cubed is  125
No.  6 squared is   36 and cubed is  216
No.  7 squared is   49 and cubed is  343
No.  8 squared is   64 and cubed is  512
No.  9 squared is   81 and cubed is  729
No. 10 squared is  100 and cubed is 1000
No. 11 squared is  121 and cubed is 1331
No. 12 squared is  144 and cubed is 1728
No. 13 squared is  169 and cubed is 2197
No. 14 squared is  196 and cubed is 2744
No. 15 squared is  225 and cubed is 3375
No. 16 squared is  256 and cubed is 4096
No. 17 squared is  289 and cubed is 4913
No. 18 squared is  324 and cubed is 5832
No. 19 squared is  361 and cubed is 6859
'''
