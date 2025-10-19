package Easy.TwoSum1;

// Question:
// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

// Bonus: Can you do this in one pass?

import java.util.HashSet;

public class TwoSum1 {
    
    public static boolean twoSum(int[] nums, int k) {
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            int target = k - num;
            if (seen.contains(target)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {10, 15, 3, 7};
        int k = 17;
        System.out.println("Answer is: ");
        System.out.println(twoSum(nums, k)); // Output: true
    }
}

// ----------
// Analysis:
// Time Complexity: O(n) where n is the number of integers in the list.
// Space Complexity: O(n) for storing the seen numbers in the HashSet.
