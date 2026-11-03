class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answers = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

        int first_index = 0;
        int second_index = first_index + 1;
        int third_index = nums.length - 1;

        while(first_index < nums.length - 2){
            second_index = first_index + 1;
            third_index = nums.length - 1;

            while (second_index < third_index) {
                int three_sum = nums[first_index] + nums[second_index] + nums[third_index];
                // Sum is too large
                if (three_sum > 0) {
                    third_index -= 1;
                }
                // Sum is too small
                else if (three_sum < 0) {
                    second_index += 1;
                }
                // Sum is an answer 
                if (three_sum == 0) {
                    List<Integer> new_answer = new ArrayList<>();
                    new_answer.add(nums[first_index]);
                    new_answer.add(nums[second_index]);
                    new_answer.add(nums[third_index]);
                    answers.add(new_answer);
                    second_index += 1;
                    while (second_index < third_index && nums[second_index] == nums[second_index - 1] ) {
                        second_index += 1;
                    }
                }                
            }    

            int old_first_index = first_index;
            while (first_index < nums.length - 2 && nums[first_index] == nums[first_index + 1]) {
                first_index++;
            }  
                 
            first_index++;
        }
        return answers;        
    }
}
