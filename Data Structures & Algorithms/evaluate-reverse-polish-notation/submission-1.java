class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        Set<String> signs = new HashSet<>(List.of("+", "-", "*", "/"));
        for(String s: tokens){
            if(signs.contains(s)){
                int op2=stack.pop();
                int op1 = stack.pop();
                if(s.equals("+")){
                    stack.push(op1+op2);
                }else if( s.equals("-")){
                    stack.push(op1-op2);
                }else if(s.equals("*")){
                    stack.push(op1*op2);
                }else{
                    stack.push(op1/op2);
                }
            }else{
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.pop();
    }
}
