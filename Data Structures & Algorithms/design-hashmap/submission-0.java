class ListNode {
    int key = -1;
    int val = -1;
    ListNode next = null;

    public ListNode(int key, int val){
        this.key = key;
        this.val = val;
    }
}

class MyHashMap {

    ListNode[] buckets = new ListNode[10000];

    public MyHashMap() {
        for(int i = 0; i < 10000; i++){
            buckets[i] = new ListNode(-1, -1);
        }
        
    }

    private int getHashVal(int key){
        return key % 10000;
    }
    
    public void put(int key, int value) {
        int hashVal = getHashVal(key);

        ListNode node = buckets[hashVal];

        while(node.next != null){
            if(node.next.key == key){
                node.next.val = value;
                return;
            }
            node = node.next;
        }

        node.next = new ListNode(key, value);
    }
    
    public int get(int key) {
        int hashVal = getHashVal(key);

        ListNode node = buckets[hashVal];

        while(node.next != null){
            if(node.next.key == key){
                return node.next.val;
            }
            node = node.next;
        }

        return -1;
        
    }
    
    public void remove(int key) {
        int hashVal = getHashVal(key);

        ListNode node = buckets[hashVal];

        while(node.next != null){
            if(node.next.key == key){
                node.next = node.next.next;
                return;
            }
            node = node.next;
        } 
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */