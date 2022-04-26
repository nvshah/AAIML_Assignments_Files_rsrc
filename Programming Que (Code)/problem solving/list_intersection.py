
from collections import Counter

def list_intersection(l1, l2):
    '''
        Compelxity -> O(n + m) , n = len(l1) & m = len(l2)
    '''
    if len(l1) > len(l2):
        s_l, b_l = l2, l1 
    else:
        s_l, b_l = l1, l2 
    freq_s_l = Counter(s_l)
    ans = []
    for n in b_l:
        cnt = freq_s_l.get(n, 0)
        if cnt:
            ans.append(n)
            freq_s_l[n] -= 1
    return ans

l1 = [1,4,2,9,6,8,8,10,2]
l2 = [2,2,4,5,6]

ans = list_intersection(l1, l2)
print(ans)


    