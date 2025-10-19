# Question:
# Given a list of numbers, 
# create an algorithm that arranges them in order to form the largest possible integer.
# For example, given [10, 7, 76, 415], you should return 77641510.


# Ideation:
# Sorting normally wont work as: 415 > 76 but 76415 < 7676
# For any two numbers x and y, compare x+y and y+x as STRINGS


class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key

        def compareStrings(x,y):
            if x+y > y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        
        # convert all numbers to string
        nums = list(map(str, nums))

        # sort using custom comparator
        nums.sort(key=cmp_to_key(compareStrings))

        # join the sorted strings
        largest_num = ''.join(nums)

        return '0' if largest_num[0] == '0' else largest_num
    
    #-----------------------

    def largestNumberWoComparator(self, nums):
        # '10' * 10 = '1010101010'
        # '7'  * 10 = '7777777777'
        # '76' * 10 = '7676767676'
        # '415'* 10 = '4154154154'

        # convert all numbers to string
        nums = list(map(str, nums))

        # sort using custom key; descending based on repeated pattern
        nums.sort(key=lambda x: x*10, reverse=True)

        # join the sorted strings
        largest_num = ''.join(nums)
        return '0' if largest_num[0] == '0' else largest_num

#------------------------
# Example usage:

solution = Solution().largestNumber([10, 2, 706, 415])

solution2 = Solution().largestNumberWoComparator([10, 2, 96, 415])


print(solution)  # Output: 706415210

print(solution2)  # Output: 966415210

#-------------------------

# Complexity Analysis:
# Time Complexity: O(n log n * k) where n is the number of elements in the list 
# and k is the maximum length of the numbers when converted to strings.
# Space Complexity: O(n) for storing the string representations of the numbers.