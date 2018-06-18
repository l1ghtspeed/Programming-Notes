/* Priority Queue Implementation using Heaps (Binary tree such that parent is always >= children) 

Insertion is random, we do not care, but extract Max always returns the greatest node

*/

public class PriorityQueue {
    /* Remember to make complete trees using pointer to keep track of latest leaf */
    private Node<E> root = new Node<E>();
    

    public PriorityQueue(){

    }

    public int extractMax(){
        return 0;
    }
    
    public int getMax(){
        return 0;
    }

    public void remove(){
    }

    public void insert(){
    }

    private void siftup(){
    }

    private void siftdown(){
    }

    public String toString(){
        return "";
    }

    private class Node<E> {
        public Node<E> left;
        public Node<E> right; 
        public Node<E> parent; 
        public E value;
    
        public Node(E _value){
            this.parent = null;
            this.left = null;
            this.right = null;
            this.value = _value;
        }

        public boolean isLeaf(){
            return this.left != null && this.right != null;
        }
    }

}