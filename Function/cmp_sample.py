# coding=utf-8

__author__ = 'zengyuetian'

"""
它的返回值只有三个，正数，0，负数，下面来看一下：
cmp(x, y)
中文说明：比较两个对象x和y，如果x < y ,返回负数；x == y, 返回0；x > y,返回正数。
版本：该函数只有在python2中可用，而且在python2所有版本中都可用。但是在python3中该函数已经被删减掉，这点要特别注意。
"""


# -1, 0, 1

print cmp(1, 2)
print cmp(1, 1)
print cmp(5, 2)

# #注意：这时候它会先比较第一个字符，然后比较第二个字符，逐个比较知道能判断出大小为止。
print cmp('abcd', 'a')
