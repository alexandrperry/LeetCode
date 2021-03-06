from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      hash1 = Counter(nums1)
      hash2 = Counter(nums2)
      commonKeys = list(hash1 & hash2)
      res = []
      for key in commonKeys:
        for _ in range(min(hash1[key],hash2[key])):
          res.append(key)
        
      return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      counts = collections.Counter(nums1)
      res = []
      for num in nums2:
          if counts[num] > 0:
              res.append(num)
              counts[num] -= 1

      return res
