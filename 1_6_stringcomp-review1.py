def comp(s):
    i = 0
    count = 0
    compressed = ''    
    while i < len(s):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed = compressed + s[i] + str(count)
            count = 0
        i += 1
    return s if len(s) < len(compressed) else compressed

if __name__ == '__main__':
    print(comp(''))
    print(comp('a'))
    print(comp('aabcccccaaa'))
    print(comp('aAvbbbBBbcaaaa'))
    print(comp('aAvbbbBBBBBBBBBBBBBBBBBBBBBBbcaaaa'))
    print(comp('abbccdf'))
    print(comp('abc'))

#MISTAKES: = / ==, left off : in flow control, didn't account for all paths/logic, refactor logic