class ListNode {
    int val = 0;
    ListNode next = null;

    public ListNode(int val){
        this.val = val;
    }
}

class MyHashSet {
    ListNode[] hashset = new ListNode[10000];

    public MyHashSet() {
        for(int i = 0; i < 10000; i++){
            hashset[i] = new ListNode(0);
        }
        
    }
    
    public void add(int key) {
        int hashVal = key % 10000;

        ListNode curr = hashset[hashVal];

        while(curr.next != null){
            if(curr.next.val == key){
                return;
            }
            curr = curr.next;
        }

        curr.next = new ListNode(key);
        
    }
    
    public void remove(int key) {
        int hashVal = key % 10000;

        ListNode curr = hashset[hashVal];

        while(curr.next != null){
            if(curr.next.val == key){
                curr.next = curr.next.next;
                return;
            }

            curr = curr.next;
        }
        
    }
    
    public boolean contains(int key) {
        int hashVal = key % 10000;

        ListNode curr = hashset[hashVal];

        while(curr.next != null){
            if(curr.next.val == key){
                return true;
            }

            curr = curr.next;
        }

        return false;
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */