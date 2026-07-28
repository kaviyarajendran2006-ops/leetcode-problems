'''
class Solution:
    def maxArea(self, height):
        l = 0 
        r = len(height)-1
        max_1 = 0
        while l < r:
            if height[l] <= height[r]:
                min_1 = height[l]
                index =  r - l
                a = min_1 * index
                max_1 = max(a,max_1)
                l += 1
            elif height[l] >= height[r]:
                min_1 = height[r]
                index = r - l
                a = min_1 * index
                max_1 = max(a,max_1)
                r -= 1
        return max_1        

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))
print(obj.maxArea([2,9,4,7,3,8,5]))
'''

class Solution:
    def maxArea(self, height):

        max_water = 0
        i = 0
        j = len(height)-1

        while i < j:
            if height[i] <= height[j]:
                total_water = height[i] * abs(i-j)
                max_water = max(total_water,max_water)
                i += 1
            if height[i] > height[j]:
                total_water = height[j] * abs(i-j)
                max_water = max(total_water,max_water)
                j -= 1    
        return max_water

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))
print(obj.maxArea([2,9,4,7,3,8,5]))
















