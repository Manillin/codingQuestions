class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
        {
            return false;
        }
        Map<Character, Integer> dict = new HashMap<>();
        Map<Character, Integer> dict2 = new HashMap<>();
        for(int i=0; i<s.length();i++)
        {
            dict.put(s.charAt(i), dict.getOrDefault(s.charAt(i), 0)+1);
            dict2.put(t.charAt(i), dict2.getOrDefault(t.charAt(i), 0)+1);
        }
        return dict.equals(dict2);
    }
}
