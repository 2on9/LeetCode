class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        for _ in range(cnt):
            nums.remove(val)