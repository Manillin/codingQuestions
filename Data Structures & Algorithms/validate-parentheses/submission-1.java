class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        HashSet<Character> keys = new HashSet<>();
        keys.add(')');
        keys.add(']');
        keys.add('}'); 
        for(char c: s.toCharArray()){
            if(keys.contains(c)){
                if(stack.peek() == map.get(c)){
                    stack.pop();
                }else{
                    return false;
                }

            }else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
