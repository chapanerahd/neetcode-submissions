class Solution {
    public int longestConsecutive(int[] nums) {
        var set = new HashSet<Integer>();
        int count = 0;
        int maxCount = 0;

        for(int num: nums){
            set.add(num);
        }

        for(int num: nums){
            if(!set.contains(num - 1)){
                while(set.contains(num)){
                    count = count + 1;
                    num = num + 1;
                }
                maxCount = Math.max(maxCount, count);
                count = 0;
            }
        }

        return maxCount;
    }
}
