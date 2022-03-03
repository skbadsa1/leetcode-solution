class Solution(object):
    
    def intersect(self, nums1, nums2):
        m = {}
        if len(nums1)<len(nums2):
            
            nums1,nums2 = nums2,nums1
        for i in nums1:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        result = []
        for i in nums2:
            if i in m and m[i]:
                m[i]-=1
                result.append(i)
        return result
    