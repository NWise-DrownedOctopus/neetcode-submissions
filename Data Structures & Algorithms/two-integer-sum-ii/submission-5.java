class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int front_index = 0;
        int back_index = numbers.length - 1;

        while(true) {
            // If answer is found, return it
            if (numbers[front_index] + numbers[back_index] == target) {
                int[] answer = {front_index + 1, back_index + 1};
                return answer;
            }
            // if found sum is too small, increase sum by moving front index forward
            else if (numbers[front_index] + numbers[back_index] < target){
                front_index += 1;
            }
            // if found sum is too large, decrese sum by moving back index backward
            else {
                back_index -= 1;
            }
        }   
    }
}
