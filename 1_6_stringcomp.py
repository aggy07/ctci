def writestring(s, c, count):
    return s + c + str(count)

def comp(s):
    i = 0
    count = 1
    compressed = ''    
    while i < len(s):
        if i > 0:
            if s[i] == s[i-1]:
                count += 1
                if i == len(s)-1:
                    compressed = writestring(compressed, s[i-1], count)
            else:
                compressed = writestring(compressed, s[i-1], count)
                count = 1
                if i == len(s)-1:
                    compressed = writestring(compressed, s[i], count)
        i += 1
    if len(s) < len(compressed):
        return s
    return compressed

if __name__ == '__main__':
    print(comp(''))
    print(comp('a'))
    print(comp('aabcccccaaa'))
    print(comp('aAvbbbBBbcaaaa'))
    print(comp('aAvbbbBBBBBBBBBBBBBBBBBBBBBBbcaaaa'))
    print(comp('abbccdf'))
    print(comp('abc'))

#MISTAKES: = / ==, left off : in flow control, didn't account for all paths/logic