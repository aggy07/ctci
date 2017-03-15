# 1_3 URLify - replace spaces with '%20', and remove trailing whitespace.

# inplace solution
# from https://github.com/careercup/CtCI-6th-Edition-Python/commit/43af771a8fb7b8a0de2333bb72bbea25615d4738
# review how to shift elements

def urlify(string, length):
    '''replace spaces with '%20', and remove trailing whitespace.'''
    new_index = len(string)

    for i in reversed(range(length)):

        if string[i] == ' ':
            string[new_index - 3:new_index] = '%20'
            print(new_index-3,new_index)
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1
        print(i ,new_index)
        print(string)
    return string




if __name__ == '__main__':
    print(''.join(urlify(list('Mr John Smith    '), 13)))
    print(''.join(urlify(list('much ado about nothing      '), 22)))