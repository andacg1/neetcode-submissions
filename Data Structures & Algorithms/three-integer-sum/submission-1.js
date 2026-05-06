class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const result = []
        nums.sort()
        for (let i=0;i<nums.length-2;i++) {
            if (i > 0 && nums[i-1] === nums[i]) {
                continue;
            }
            for (let j=i+1;j<nums.length-1;j++) {
                if (j > i+1 && nums[j-1] === nums[j]) {
                    continue;
                }
                for (let k=j+1;k<nums.length;k++) {
                    if (k > j+1 && nums[k-1] === nums[k]) {
                        continue;
                    }
                    if (nums[i] + nums[j] + nums[k] === 0) {
                        result.push([nums[i],nums[j],nums[k]])
                    }
                }
            }
        }
        return result;
    }
}
