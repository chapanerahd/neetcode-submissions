class Solution {
    public List<Integer> majorityElement(int[] nums) {
        var majorityElements = new ArrayList<Integer>();
        var countOfElements = new HashMap<Integer, Integer>();
        int k = (nums.length / 3);

        for(int num: nums){
            countOfElements.put(num, countOfElements.getOrDefault(num, 0) + 1);
        }

        for(int num: countOfElements.keySet()){
            int count = countOfElements.get(num);
            if(count > k) majorityElements.add(num);
        }

        return majorityElements;
        
    }
}

