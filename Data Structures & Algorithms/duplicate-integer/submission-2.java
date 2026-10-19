class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Let's use a hashmap to track each encounter with a number, as soon as we find a an entry that already exisit we can return true
        HashMap<Integer, Integer> numsMap = new HashMap<>();

        // Let's iterate through the provided collection
        for (int num: nums) {
            // Let's check if we have the value in the hashmap
            int count = numsMap.getOrDefault(num, 0);
            if (count == 1) {
                return true;
            }
            else {
                numsMap.put(num, count + 1);
            }
        }
        return false;
    }
}