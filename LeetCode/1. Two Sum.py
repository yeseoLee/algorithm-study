def twoSum(nums, target):
    nums_sorted=sorted(nums)
    i,j=0,len(nums)-1
    min_i,max_j=i,j
    i_idx,j_idx=-1,-1
    while(1):
        if(nums_sorted[i]+nums_sorted[j]<target):
            i+=1
            min_i=i
            j=max_j
        elif(nums_sorted[i]+nums_sorted[j]>target):
            j-=1
            max_j=j
            i=min_i
        else: #nums_sorted[i]+nums_sorted[j]==target
            for idx,val in enumerate(nums):
                if(val==nums_sorted[i] or val==nums_sorted[j]):
                    if(i_idx==-1):
                        i_idx=idx
                    else:
                        j_idx=idx
                        return [i_idx,j_idx]

'''
def twoSum(nums, target):
    for idx, val in enumerate(nums):
        diff = target - val
        if nums.count(diff)==1 and nums.index(diff) != idx:
            return [idx, nums.index(diff)]
        elif nums.count(diff)==2:
            return [idx, nums.index(diff,idx+1)]

print(twoSum([2,5,5,11],10))
'''
