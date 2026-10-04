class Solution {

    public String encode(List<String> strs) {
        String encode = "";

        for(int i = 0; i < strs.size(); i++){
            encode += strs.get(i).length() + "/" + strs.get(i);
        }

        return encode;
    }

    public List<String> decode(String str) {
        int i = 0;
        int n = str.length();
        List<String> decode = new ArrayList<String>();

        while(i < n){
            char c = str.charAt(i);
            String digit = "0";
            int len = 0;
            
            while(Character.isDigit(str.charAt(i))){
                digit += str.charAt(i);
                i++;
            }
            len = Integer.valueOf(digit);

            if(str.charAt(i) == '/'){
                int start = i + 1;
                int end = i + len;

                decode.add(str.substring(start, end + 1));

                i = end + 1;
            }
            
        }

        return decode;
    }
}
