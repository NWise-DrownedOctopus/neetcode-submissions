class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) { return false; }

        HashMap<Character, Integer> s_map = new HashMap<>();
        HashMap<Character, Integer> t_map = new HashMap<>();

        for (char c: s.toCharArray()) {
            int count = s_map.getOrDefault(c, 0);
            s_map.put(c, count + 1);
        }

        for (char c: t.toCharArray()) {
            int count = t_map.getOrDefault(c, 0);
            t_map.put(c, count + 1);
        }

        for (char key: s_map.keySet()) {
            if (!s_map.get(key).equals(t_map.get(key))) { return false; }
        }

        return true;
    }
}
