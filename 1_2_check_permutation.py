# 1_2 check if one string is a permutation of other string
# case sensitive, count white space
# a. sort the strings and compare
# b. # b. Use a python Counter: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter%201/2_Check%20Permutation/CheckPermutation.py similar to book solution: array sized to charset (check if ascii or unicode) and set char count using char code for index


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    counter = Counter()

    for c in s1:
        counter[c] += 1
    for c in str2:
        if counter[c]  == 0:
            return False
        counter[c] -= 1
    return True


if __name__ == '__main__':
    print(is_permutation('bat', 'tab'))