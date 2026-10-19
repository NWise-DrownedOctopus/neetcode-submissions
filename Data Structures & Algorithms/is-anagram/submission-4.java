class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sWord = new HashMap<>();
        HashMap<Character, Integer> tWord = new HashMap<>();

        for (Character c: s.toCharArray()) {
            int count = sWord.getOrDefault(c, 0);
            sWord.put(c, count + 1);
        }

        for (Character c: t.toCharArray()) {
            int count = tWord.getOrDefault(c, 0);
            tWord.put(c, count + 1);
        }

        boolean areEqual = sWord.equals(tWord); 
        return areEqual;
    }
}
