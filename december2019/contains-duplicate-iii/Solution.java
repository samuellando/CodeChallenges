class Solution {
    public static boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        long[] numsl = new long[nums.length];
        for (int i = 0; i < nums.length; i++)
            numsl[i] = nums[i];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 1; j <= k && i + j < nums.length; j++) {
                if (Math.abs(numsl[i] - numsl[i+j]) <= t) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {7,1,3};
        System.out.println(containsNearbyAlmostDuplicate(nums, 2, 3));
    }
}