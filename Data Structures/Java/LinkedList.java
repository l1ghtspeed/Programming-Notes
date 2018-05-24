//Doubly Linked List Example

public class LinkedList<E> {

    private Node<E> head = new Node();
    private Node<E> tail = new Node();

    public LinkedList(){
        this.head.next = this.tail;
        this.tail.previous = this.head;
    }

    public void pushFront(E value){
        if (this.head.next == this.tail) {
            Node<E> temp = new Node(this.head, this.tail, value);
            head.setNext(temp);
            tail.setPrevious(temp);
        } else {
            Node<E> temp = new Node(this.head, this.head.next, value);
            head.next.setPrevious(temp);
            head.setNext(temp);            
        }
    }

    public void pushBack(E value){
        if (this.tail.previous == this.head) {
            Node<E> temp = new Node(this.head, this.tail, value);
            head.setNext(temp);
            tail.setPrevious(temp);
        } else {
            Node<E> temp = new Node(this.tail.previous, this.tail, value);
            tail.previous.setNext(temp);
            tail.setPrevious(temp);            
        }
    }

    public void popFront(){
        if (this.head.next != this.tail && this.head.next.next != this.tail){
            this.head.next = this.head.next.next;
            this.head.next.previous = this.head;
        } else if (this.head.next != null){
            this.head.next = this.tail;
            this.tail.previous = this.head;
        }
    }

    public void popBack(){
        if (this.tail.previous != null && this.tail.previous.previous != null){
            this.tail.previous = this.tail.previous.previous;
            this.tail.previous.next = this.tail;
        } else if (this.tail.previous != null){
            this.tail.previous = this.head;
            this.head.next = this.tail;
        }
    }

    public boolean isEmpty(){
        if (this.head.next == this.tail){
            return true;
        }
        return false;
    }

    public void Erase(E value){
        Node<E> curr = this.head;
        while (curr.next != this.tail){
            System.out.println(2);
            if (curr.next.value == value){
                if (curr.next.next != this.tail){
                    curr.next.next.previous = curr;
                    curr.next = curr.next.next;
                    break;
                } else {
                    curr.next = this.tail;
                    break;
                }
            }
            curr = curr.next;
        }
    }

    public String toString(){
        String holder = "";
        Node<E> curr = this.head;

        while(curr.next != this.tail){
            holder += curr.next.value;
            holder += " ";
            curr = curr.next;
        } 

        return holder;
    }

    private class Node<E> {

        public Node<E> previous;
        public Node<E> next; 
        public E value;
    
        public Node(Node<E> _previous, Node<E> _next, E _value){
    
            this.previous = _previous;
            this.next = _next;
            this.value = _value;
            
        }

    
        public Node(){
            this.previous = null;
            this.next = null;
            this.value = null;
        }
    
        /**
         * @param next the next to set
         */
        public void setNext(Node<E> _next) {
            this.next = _next;
        }
    
        public void setPrevious(Node<E> _previous){
            this.previous = _previous;
        }
    }
}
