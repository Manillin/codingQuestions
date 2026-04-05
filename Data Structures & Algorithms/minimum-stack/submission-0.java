class MinStack {
    Deque<Integer> stack;
    Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.size() > 0){
            int min = minStack.peek();
            if(val < min){
                minStack.push(val);
            }else{
                minStack.push(min);
            }
        }else{
            minStack.push(val);
        }        
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
