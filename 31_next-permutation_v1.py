"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #My code starts here
        if not nums:
            return []
        flag=0  
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:  
            #To find the first pair of two successive numbers nums[i] and nums[i+1] from the right, which satisfy nums[i+1] > nums[i]
                flag=1
                index=i
                break
        if flag==0:  #If not find, rearrange it as the lowest possible order
            return nums.reverse()
        j=1
        while index+j<len(nums):
        #We need to find number which is just larger than nums[i] among the numbers lying to its right section
            if nums[index]<nums[index+j]:
                j+=1
            else:
                break
        tmp=nums[index+j-1]
        nums[index+j-1]=nums[index]
        nums[index]=tmp
        #Swap nums[i] and nums[i+j-1]
        nums[index+1:]=list(reversed(nums[index+1:]))
        #At last, reverse the numbers following nums[i] to get the next smallest lexicographic permutation
        return nums
"""
My thinking: First, we observe that for any given sequence that is in descending order, no next larger permutation is possible. Then, we 
need to find the first pair of two successive numbers nums[i] and nums[i+1] from the right, which satisfy nums[i+1]> nums[i]. After that,
we need to find number which is just larger than nums[i] among the numbers lying to its right section. We swap nums[i] and nums[i+j-1].
At last, reverse the numbers following nums[i] to get the next smallest lexicographic permutation.
"""
                
            
