def one_away(s1: str, s2: str) -> bool:

    # insert, remove, replace
    # string length - must be from -1 to +1 in length.
    # letters must match from -1 to +1 difference.
    # order can differ only once.
    if abs(len(s1)-len(s2)) > 1:
        return(False)

    if len(s1) > len(s2):
        longest = s1
        shortest = s2
    else:
        longest = s2
        shortest = s1

    index1 = 0
    index2 = 0
    foundDifference = False
    while ( index2 < len(longest) and index1 < len(shortest) ):
        if shortest[index1] != longest[index2]:
            # check that this is first difference
            if foundDifference:
                return False
            foundDifference = True

            if len(shortest) == len(longest):
                index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True


    












if __name__ == '__main__':

    print(one_away('pale','ple'))
    print(one_away('pales','pale'))
    print(one_away('pale','bale'))
    print(one_away('pale','bake'))
    print(one_away('pall','pale'))
    print(one_away('palll','palel'))
    print(one_away('palll','palllel'))
    print(one_away('ale','pale'))
    print(one_away('tree','sapree'))




#assumptions case insensitive, letters only, 
#MISTAKES set details,