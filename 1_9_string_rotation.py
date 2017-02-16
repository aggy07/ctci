def string_rotation(s1, s2):
    #  Hints: #34, #88, # 104
    if len(s1) != len(s2) or s1 == s2:
        return False
    starts = []
    if s1[0] in s2: # O(N)
        i = 0
        while i < len(s2): # O(N)
            if s2[i] == s1[0]:
                starts.append(i)
            i += 1
    else:
        return False
    for start in starts: # O(N)
        i = 1
        rotation = True
        while i < len(s1): # O(N)
            calculated_index = start + i
            if calculated_index >= len(s2):
                calculated_index = calculated_index - len(s2)
            if s1[i] == s2[calculated_index]:
                i += 1
            else:
                rotation = False
                i = len(s1)
    return rotation

def string_rotation2(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False
    
    starts = []
    if s1[0] in s2: # O(N)
        i = 0
        while i < len(s2): # O(N)
            if s2[i] == s1[0]:
                starts.append(i)
            i += 1
    else:
        return False
    
    for start in starts: # O(N)
        print(s2[start:]+s2[:start])
        if s1 == s2[start:]+s2[:start]:
            return True
    return False

def string_rotation3(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False
    
    return (s1 in (s2+s2))

if __name__ == '__main__':

    print('1. ',string_rotation('', ''))
    print('2. ',string_rotation('w', 'w'))
    print('3. ',string_rotation('abcdef', 'defab'))
    print('4. ',string_rotation('waterbottle', 'waterbottle'))
    print('5. ',string_rotation('terbottlewa', 'erbottlewat'))
    print('6. ',string_rotation('alexandria', 'andriaalex'))
    print('7. ',string_rotation('waterbottle', 'bottlebottt'))

    print('1. ',string_rotation2('', ''))
    print('2. ',string_rotation2('w', 'w'))
    print('3. ',string_rotation2('abcdef', 'defab'))
    print('4. ',string_rotation2('waterbottle', 'waterbottle'))
    print('5. ',string_rotation2('terbottlewa', 'erbottlewat'))
    print('6. ',string_rotation2('alexandria', 'andriaalex'))
    print('7. ',string_rotation2('waterbottle', 'bottlebottt'))

    print('1. ',string_rotation3('', ''))
    print('2. ',string_rotation3('w', 'w'))
    print('3. ',string_rotation3('abcdef', 'defab'))
    print('4. ',string_rotation3('waterbottle', 'waterbottle'))
    print('5. ',string_rotation3('terbottlewa', 'erbottlewat'))
    print('6. ',string_rotation3('alexandria', 'andriaalex'))
    print('7. ',string_rotation3('waterbottle', 'bottlebottt'))

# MISTAKES difference between in and .find ? , not remembering/following instructions, get comforable with slices