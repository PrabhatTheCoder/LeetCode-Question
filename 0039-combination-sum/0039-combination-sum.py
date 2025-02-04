from typing import List

class Solution:
    def solve(self, nums, target, ans, result, index):
        if sum(ans) == target:
            result.add(tuple(ans))  # ✅ Store as a tuple to ensure uniqueness
            return
        if sum(ans) > target:
            return

        for i in range(index, len(nums)):  # ✅ Start from current index to allow reusing the same element
            ans.append(nums[i])
            self.solve(nums, target, ans, result, i)  # ✅ Keep 'i' to reuse the same number
            ans.pop()  # ✅ Backtrack

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)  # ✅ Sort for consistent output
        result = set()
        self.solve(candidates, target, [], result, 0)
        return [list(comb) for comb in result]  # ✅ Convert tuples back to lists

