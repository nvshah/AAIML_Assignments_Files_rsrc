# Recursive Approach
from typing import List

# Complexity -> O(n!)
def permutation(l: List[int]):
    '''
    Find Permutation using Recurssion
    :param: l -> list
    :return: -> all permutations i.e npn
    '''
    # Base Case -> At Most 1 element
    if len(l) <= 1:
        return [l]

    ans = []

    # indxd_l = list(enumerate(l))

    # for i in range(len(l)):
    #     fix_i = [e for j, e in indxd_l if j!=i]
    #     perm_rest = permutation(fix_i)
    #     ans.extend(([l[i], *p] for p in perm_rest))

    for e in l:
        fix_e = [i for i in l if e != i]
        perm_rest = permutation(fix_e)
        ans.extend(([e, *p] for p in perm_rest))

    return ans


l = [1, 2, 3]
p = permutation(l)
print(p)




    

