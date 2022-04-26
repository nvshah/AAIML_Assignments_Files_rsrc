from itertools import accumulate
from math import copysign

# 1 Linear Appraoch  O(n)
def find_peak_elem_linear(l):
    ans = []
    # Edge case 1
    if l[0] > l[1]:
        ans.append(0)
    
    for i in range(1, len(l)-1):
        if l[i-1]<=l[i]>= l[i+1]:
            ans.append(i)
    
    # edge case 2
    if l[-1] > l[-2]:
        ans.append(len(l)-1)
    
    return ans 

# ref -> https://iq.opengenus.org/peak-element-in-array/
# 2 Divide & Conquer Approach (Recursive) - O(logn)
def find_peak_elem_dq(l):
    def peak_finder(l, s, e):
        if s == e: # only 1 element left hence peak
            return s 
        elif s+1 == e: # 2 elements left
            return s if l[s] > l[e] else e 
        else:
            m = s + (e-s)//2
            if l[m-1] < l[m] > l[m+1]:
                # peak element found
                return m 
            elif l[m-1] > l[m] > l[m+1]:
                # here if elements are equal then considering Right Most as Peak
                return peak_finder(l, s, m-1)
            else:
                # l[m-1] < l[m] < l[m+1]
                # As we need to find only 1 peak so not exploring case l[m-1] > l[m] < l[m+1], where 2 peaks can be found probably
                return peak_finder(l, m+1, e)
    return peak_finder(l, 0, len(l)-1)


def diff(l):
    return [l[i+1]-l[i] for i in range(len(l)-1)]

'''When you need to find all the peaks or plummets find below methods'''

def find_peak_elem_via_diff(l):
    ''' O(n) '''
    size = len(l)
    if len(l) == 1:
        return l[0]

    # if >0 then >prev if <0 then <prev
    elm_diff = diff(l)
    sign_diff = [copysign(1, x) for x in elm_diff]

    thresolds = diff(sign_diff)
    print(thresolds)

    peaks_idx = [x+1 for x in range(len(thresolds)) if thresolds[x]==-2]

    return peaks_idx

def find_plummet_elem_via_diff(l):
    '''O(n)'''
    size = len(l)
    if len(l) == 1:
        return l[0]

    # if >0 then >prev if <0 then <prev
    elm_diff = diff(l)
    sign_diff = [copysign(1, x) for x in elm_diff]

    thresolds = diff(sign_diff)
    print(thresolds)

    peaks_idx = [x+1 for x in range(len(thresolds)) if thresolds[x]==2]

    return peaks_idx

l = [2,3,5,6,4,3,8,7,4,1,9]
#p_dq = find_peak_elem_dq(l)
#p_linear = find_peak_elem_linear(l)

#print(p_dq)     # 3
#print(p_linear) # [3, 6, 10]

ans = find_peak_elem_via_diff(l)
print([l[i] for i in ans])
ans = find_plummet_elem_via_diff(l)
print([l[i] for i in ans])


