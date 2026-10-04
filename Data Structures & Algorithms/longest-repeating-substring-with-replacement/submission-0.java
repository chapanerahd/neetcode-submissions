class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0; int right = 0;

        HashMap<Character,Integer> map = new HashMap<Character,Integer>();

        int maxFreq = 0;
        int maxCount = 0;

        while(right < s.length()){
            map.put(s.charAt(right),map.getOrDefault(s.charAt(right),0)+1);
            maxFreq = Math.max(maxFreq,map.get(s.charAt(right)));

            if((right-left+1 - maxFreq) <= k){
                maxCount = Math.max(maxCount,right-left+1);
            }
            else{
                map.put(s.charAt(left),map.get(s.charAt(left))-1);
                left++;
            }
            right++;
        }

        return maxCount;
        
    }
}
