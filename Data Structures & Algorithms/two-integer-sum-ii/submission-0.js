class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let left = 0;
        let right = numbers.length-1;
        while (left < right) {
            const leftNum = numbers[left];
            const rightNum = numbers[right];
            if (leftNum + rightNum > target) {
                right--;
            } else if (leftNum + rightNum < target) {
                left++;
            } else {
                return [left+1, right+1]
            }
        }
    }
}
