class Solution:
    def threeSum(self, nums):
        nums.sort()
        temp = []

        for m in range(len(nums)):
            if m > 0 and nums[m] == nums[m - 1]: 
                continue


            i = m+1
            j = len(nums)-1

            while i < j:
                sum = nums[m]+nums[i]+nums[j]

                if sum == 0:
                    temp.append([nums[m],nums[i],nums[j]])
                    i += 1
                    j -= 1 

                    while i < j and nums[i-1] == nums[i]:
                        i += 1    


                elif sum > 0:
                    j -=1
                else:
                    i += 1
        return temp                


obj = Solution()
print(obj.threeSum([-1,0,1,2,-1]))         
print(obj.threeSum([0,0,0,0,0]))
print(obj.threeSum([-1,0,1,2,2,-1,-4]))