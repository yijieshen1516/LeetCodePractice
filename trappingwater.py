#define left/right max
#which max is higher, which side is moving pointer
#once the pointer moved, calculate the difference between height and max and add to ans

class Solution(object):
    def trappingwater(self, height):

        if (len(height)==0): return 0
        left = 0
        right = len(height) -1
        leftMax=0
        rightMax=0
        ans = 0
        while (left < right):
            if height[left] > leftMax:
                leftMax = height[left]
            if height[right] > rightMax:
                rightMax = height[right]
            if leftMax < rightMax:
                ans += max(0, leftMax-height[left])
                left += 1
            else:
                ans += max(0, rightMax-height[right])
                right -= 1

        return ans



#height = [4, 2, 3]
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(Solution().trappingwater(height))




