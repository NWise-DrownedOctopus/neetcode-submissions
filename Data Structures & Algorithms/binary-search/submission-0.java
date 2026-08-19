class Solution {
    public int search(int[] nums, int target) {
        int leftPointer = 0;
        int rightPointer = nums.length - 1;        

        while (leftPointer <= rightPointer) {
            int middlePointer = leftPointer + (rightPointer - leftPointer) / 2;
            int testValue = nums[middlePointer];

            if (testValue == target) {
                return middlePointer;
            }
            else if (testValue < target) {
                leftPointer = middlePointer + 1;
            }
            else {
                rightPointer = middlePointer - 1;
            }
        }
        return -1;
    }
}
