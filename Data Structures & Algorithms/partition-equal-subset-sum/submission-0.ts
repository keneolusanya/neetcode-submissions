class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canPartition(nums: number[]): boolean {
        let sums = new Set<number>();
        sums.add(0);

        let total = 0;
        for (let n of nums) {
            let newSums = new Set<number>();
            for (let s of sums) {
                newSums.add(s + n);
                newSums.add(s);
            }
            sums = newSums;
            total += n;
        }

        if (total % 2 == 1) {
            return false;
        }

        if (sums.has(total / 2)) {
            return true;
        } else {
            return false;
        }
    }

}