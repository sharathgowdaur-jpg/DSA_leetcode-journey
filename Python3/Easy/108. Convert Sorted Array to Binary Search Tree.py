#SOLUTION - 1
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def built(left,right):
            if left > right:
                return None

            mid = (left + right)//2

            root = TreeNode(nums[mid])

            root.left = built(left,mid-1)

            root.right = built(mid + 1,right)

            return root

        return built(0,len(nums)-1)

#SOLUTION - 2
from typing import List,Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root