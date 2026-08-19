class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int index1 = 0;
        int index2 = numbers.length - 1;

        while (true) {
            int sum = numbers[index1] + numbers[index2];
            
            if (sum == target) {
                int[]answer = {index1 + 1, index2 + 1};
                return answer;
            }
            else if (sum > target) {
                index2 -= 1;
            }
            else {
                index1 += 1;
            }
        }        
    }
}
