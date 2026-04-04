class Solution {
    public boolean isAlpha(char c){
        if( (c >= 'a' && c <= 'z') || (c>='A' && c<='Z') 
            || (c >= '0' && c <= '9') ){
            return true;
        }
        return false;
    }

    public boolean isPalindrome(String s) {
        int l = 0; 
        int r = s.length()-1;
        while(l<r)
        {
            while(l < r && (isAlpha(s.charAt(l)) == false) ){
                l++;
            }
            while( l < r && (isAlpha(s.charAt(r)) == false) ){
                r--;
            }

            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}