package Medium.LargestInteger764;

// Question:
// Given a list of numbers, 
// create an algorithm that arranges them in order to form the largest possible integer.
// For example, given [10, 7, 76, 415], you should return 77641510.


// Ideation:
// Sorting normally wont work as: 415 > 76 but 76415 < 7676
// For any two numbers x and y, compare x+y and y+x as STRINGS

import java.util.Arrays;
import java.util.Comparator;

public class LargestInteger {
    public static String largestInteger(int[] nums) {
        // Convert integers to strings
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }

        // Sort strings based on custom comparator
        Arrays.sort(strNums, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                String order1 = a + b;
                String order2 = b + a;
                return order2.compareTo(order1); // Descending order
            }
        });

        // Build the largest number
        StringBuilder largestNum = new StringBuilder();
        for (String num : strNums) {
            largestNum.append(num);
        }

        return largestNum.toString();
    }

    public static void main(String[] args) {
        int[] nums = {10, 7, 16, 415};
        System.out.println("Answer is: ");
        System.out.println(largestInteger(nums)); // Output: 74151610
    }
}
// ----------

// Analysis:
// Time Complexity: O(n log n * k) where n is the number of integers 
// and k is the average length of the integers when converted to strings.
// Space Complexity: O(n) for storing the string representations of the integers.