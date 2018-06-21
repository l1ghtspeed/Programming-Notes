/* Priority Queue Implementation using Heaps (Binary tree such that parent is always >= children) 

Insertion is random, we do not care, but extract Max always returns the greatest node

*/

public class PriorityQueue {
    /* Remember to make complete trees using pointer to keep track of latest leaf */
    private int[] arr;
    
    public PriorityQueue(){
        this.arr = new int[7];
    }

    public int extractMax(){
        int temp = arr[0];
        this.remove(arr[0]);
        return temp;
    }
    
    public int getMax(){
        return arr[0];
    }

    public void remove(){
    }

    private int getRight(int id){
        return this.arr[id*2+1];
    }

    private int getLeft(int id){
        return this.arr[id*2];
    }



    public void insert(E value){
    }

    private void siftup(){
    }

    private void siftdown(){
    }

    public String toString(){
        String temp = "";
        Node<E> curr = this.root;
        temp = this.inOrderTraversal(curr);
        return temp;
    }

    private String inOrderTraversal(Node<E> curr){
        String temp = "";
        if (curr.left != null){
            this.inOrderTraversal(curr.left);
        } 

        temp += curr.value;
        temp += " ";

        if (curr.right != null){
            this.inOrderTraversal(curr.right);
        } 
        return temp;
    }

    private void enlarge(){
        int[] temp = this.arr;
        this.arr = new int[temp.length*2+1];
        for (int i = 0; i < temp.length; i++){
            this.arr[i] = temp[i];
        }
    }
}