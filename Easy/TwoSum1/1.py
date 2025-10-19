# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


# Idea:
# Use a set to track seen numbers.

class Solution:
    def sumToK(self, nums, k):
        seen = set()
        for num in nums:
            if k - num in seen:
                return True
            seen.add(num)
        return False
    

# Example usage:
solution = Solution().sumToK([10, 15, 3, 7], 17)
solution2 = Solution().sumToK([1, 2, 3, 4], 8)

print(solution)  # Output: True
print(solution2)  # Output: False


# Complexity Analysis:
# Time Complexity: O(n) where n is the number of elements in the list.
# Space Complexity: O(n) for the set used to track seen numbers.