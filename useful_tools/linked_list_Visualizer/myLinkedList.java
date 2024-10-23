public class myLinkedList {

    public class Node {
        char data;
        Node next;
        Node(char data, Node next) { 
            this.data = data;
            this.next = null;
        }
        public Node(char data){
            this(data,null);
        }
    }

    Node first,last;
    public myLinkedList(){
        first=last=null;
    }

    public boolean isEmpty(){
        return first==null;
    }   
    public void add(char c){
        Node n = new Node(c);
        if(isEmpty()){
            first=last=n;
        }
        else{
           last.next = n; 
           last = last.next;
        }
    }

    public void print(){
        print(first);
    }
    private void print(Node n){
        StringBuilder middleLine = new StringBuilder();
        while (n != null){
            if(n.next == null){
                middleLine.append(" | ").append(n.data).append(" |");
            }else{
                // topLine.append(" ------");
                middleLine.append(" | ").append(n.data).append(" | ->");
                // BottomLine.append(" ------");
            
            }
            n = n.next;
        }
        // System.out.println(topLine.toString());
        System.out.println(middleLine.toString());
        // System.out.println(BottomLine.toString());
        System.out.println();
    }
    private String R_block(Node n){
        return " -------" + "|   " + n.data + "   |  -->"+ " -------";
    }
    private String last_block(Node n){
        return " -------" + "|   " + n.data + "   |"+ " -------";
    }
}
