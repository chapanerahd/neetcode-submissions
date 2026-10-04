class Solution {
    public boolean isValidSudoku(char[][] board) {
        var seen = new HashSet<String>();

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                char val = board[i][j];

                if(val == '.') continue;

                String rowKey = val + " is in row " + i;
                String colKey = val + " is in col " + j;
                String boxKey = val + " is in box " + i/3 + " - " + j/3;

                if(!seen.add(rowKey) || !seen.add(colKey) || !seen.add(boxKey)){
                    return false;
                }
            }
        }
        return true;
        
    }
}
