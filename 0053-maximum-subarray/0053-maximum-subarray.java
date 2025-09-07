class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int maxSum = nums[0];
        int curSum = 0;
        for(int st=0; st<n; st++){
            //Base Case:
            if (curSum < 0) curSum = 0;
            curSum += nums[st];    
            maxSum = Math.max(maxSum, curSum);
        }return maxSum;
    }
}