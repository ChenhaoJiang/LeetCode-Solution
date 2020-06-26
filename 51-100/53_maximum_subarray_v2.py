def get(a,l,r):
    # 递归（分治法）
    if l==r:
        return {'isum':a[l],'lsum':a[l],'rsum':a[l],'msum':a[l]}
    m = int((l+r)/2)
    isum = get(a,l,m)['isum'] + get(a,m+1,r)['isum'] # isum为[l,r]的区间和
    # lsum为[l,r]内以l为左端点的最大子段和
    lsum = max(get(a,l,m)['lsum'] , get(a,l,m)['isum'] + get(a,m+1,r)['lsum']) 
    # rsum为[l,r]内以r为右端点的最大子段和
    rsum = max(get(a,m+1,r)['rsum'] , get(a,m+1,r)['isum'] + get(a,l,m)['rsum']) 
    # msum为[l,r]内最大子段和
    msum = max(get(a,l,m)['msum'],get(a,m+1,r)['msum'],get(a,l,m)['rsum']+get(a,m+1,r)['lsum'])
    return {'isum':isum,'lsum':lsum,'rsum':rsum,'msum':msum}
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        return get(nums,0,len(nums)-1)['msum']
"""
思路：分治法，维护四个量（见注释），区间长度为1时结束递归。但事实上DP时间复杂度为O(n)，而分治法时间复杂度为O(nlogn)。精妙是精妙，但架不住代码长，复杂度高啊。
"""
