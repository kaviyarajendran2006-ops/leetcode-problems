class Solution:
    def minSubArrayLen(self, target, nums):
        sum = 0
        min_val = float('inf')
        left = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_val = min(min_val,right-left+1)
                sum -= nums[left]
                left += 1

        if min_val ==  float('inf'):
            return 0
        return min_val       


obj = Solution()
print(obj.minSubArrayLen( 7,[1,3,1,2,4,3]))
print(obj.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))