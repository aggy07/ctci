
# First Try
def isunique(str):
    chars = {}
    for char in str:
        if char in chars:
            return False
        else:
            chars[char] = 1
    return True

# Book Solution 1 pg 192


# Book Solution 2 pg 193




if __name__ == '__main__':
    print("Is Unique: Implment an algorithm to determine if a string has all unique characters." +
          "\nWhat if you cannot use additional data structures?\n")
    print('Test #1: {0}'.format(isunique("")))
    print('Test #2: {0}'.format(isunique("a")))
    print('Test #3: {0}'.format(isunique("asdf")))
    print('Test #4: {0}'.format(isunique("aasssssddfdfdfdfddfwefasdfwefadfewfd")))

    print('Test #1: {0}'.format(isUniqueChars("")))
    print('Test #2: {0}'.format(isUniqueChars("a")))
    print('Test #3: {0}'.format(isUniqueChars("asdf")))
    print('Test #4: {0}'.format(isUniqueChars("aasssssddfdfdfdfddfwefasdfwefadfewfd")))

# MISTAKES: dict syntax, string format syntax, built in method len(s)
# NEXT: https://github.com/careercup/ctci/blob/master/python/Chapter%201/Question1_1/ChapQ1.1.py optimize space and time complexity, implment for ascii and unicode, implement without extra data structure, http://wiki.python.org/moin/TimeComplexity