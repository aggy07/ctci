def permutation(s : str) -> bool:
    # if odd length then 1 unmatched charactor ok
    # if even then all characters must have match
    # check if each letter has a balancing match
    charset = {} # space and time of dict?
    odd_flag = 0
    print('\n')
    for c in s.lower(): # 1st for loop through string
        if c != ' ':
            if c in charset: # check charset for members - this is inside a for loop - runs length of s times (less count of spaces)
                charset[c] += 1
                # Alternate sulution: check if odd here.  
            else:
                charset[c] = 1
    for key, value in charset.items(): # 2nd for loop, through dict
        print('{} : {}'.format(key,value))
        if odd_flag < 2:
            if value % 2 != 0:
                odd_flag += 1 
        else:
            return False
    return True







if __name__ == '__main__':

    print(permutation(''))
    print(permutation('a'))
    print(permutation('aab'))
    print(permutation('brick'))
    print(permutation('asdf dfdfs'))
    print(permutation('TAct Coa'))
    print(permutation('amanapanama'))


#assumptions case insensitive, letters and spaces only, 
#MISTAKES make own table - make own hash table?, dictionary usage, find resource for learning about time and space complexity for python's standard library data structures and methods like dict, list, set, for, replace, etc...., learn about bitvector, binary, bit manipulation