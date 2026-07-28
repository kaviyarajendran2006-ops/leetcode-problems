'''
class Solution:
    def moveZeroes(self,nums)-> None:
        dum = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[dum] = nums[i]
                dum += 1
        for j in range(dum,len(nums)):
            nums[j] = 0
        return nums
                    

obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))
print(obj.moveZeroes([0]))

'''
class Solution:
    def moveZeroes(self, arr):

        count = 0
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.remove(arr[i])
                count += 1
            else:    
                i += 1    

        for j in range(len(arr),len(arr)+count):
            arr.append(0)

            
obj = Solution()
a = [1, 2, 0, 4, 3, 0, 5, 0]
obj.moveZeroes(a)
print(a)

b = [0, 0]
obj.moveZeroes(b)
print(b)
