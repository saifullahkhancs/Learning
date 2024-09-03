class Solution():
    def removeElement(self, nums, val):
        count = 0
        index = 0
        end = len(nums) - 1
        while index <= end:
            if nums[index] != val:
                count = count +1
                index = index + 1
            else:
                 nums.remove(nums[index])
                 end -= 1
                 
        return count 
object = Solution()
nums = [3,2,2,3]
val = 3
k = object.removeElement( nums , val)  
print(k)
print(nums)