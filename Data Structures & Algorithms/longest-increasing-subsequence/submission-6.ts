class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums: number[]): number {
        let LIS = [];
        LIS[nums.length - 1] = 1;

        for (let i = nums.length - 2; i >= 0; i--) {
            let cand = 1;
            for (let j = i; j < nums.length; j++) {
                if (nums[i] < nums[j]) {
                    cand = Math.max(cand, 1 + LIS[j]);
                }
            }
            LIS[i] = cand;
        }

        return Math.max(...LIS);
    }

}
