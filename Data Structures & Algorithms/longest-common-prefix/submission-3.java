class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 1) return strs[0];
        
        String result = getEqualString(strs[0], strs[1]);

        for(int i = 2; i < strs.length; i++){
            result = getEqualString(result, strs[i]);
        }

        return result;
        
    }

    private String getEqualString(String s1, String s2){
        int i = 0; int j = 0;

        String result = "";

        while(i < s1.length() && j < s2.length()){
            if(s1.charAt(i) == s2.charAt(j)){
                result += s1.charAt(i);
            }
            else{
                break;
            }
            i++;
            j++;
        }

        return result;
    }
}