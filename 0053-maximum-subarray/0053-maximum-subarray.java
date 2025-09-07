class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int st, end, f;
        int maxSum = Integer.MIN_VALUE;
        int curSum = 0;
        for(st=0; st<n; st++){
            //Base Case:
            if (curSum < 0) curSum = 0;
            curSum += nums[st];    
            maxSum = Math.max(maxSum, curSum);
        }return maxSum;
    }
}