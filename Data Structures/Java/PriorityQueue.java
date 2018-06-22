/* Priority Queue Implementation using Heaps (Binary tree such that parent is always >= children) 

Insertion is random, we do not care, but extract Max always returns the greatest node

*/

public class PriorityQueue {
    /* Remember to make complete trees using pointer to keep track of latest leaf */
    private int[] arr;
    private int maxSize = 4;
    private int currentSize = 0;

    public PriorityQueue(){
        this.arr = new int[maxSize];
        this.arr[0] = 0;
    }

    public int extractMax(){
        int temp = this.arr[1];
        this.arr[1] = this.arr[currentSize];
        this.currentSize-=1;
        this.siftdown(1);
        return temp;
    }

    public int getMax(){
        return arr[1];
    }

    private int getRight(int id){
        return this.arr[id*2+1];
    }

    private int getLeft(int id){
        return this.arr[id*2];
    }

    public void insert(int value){
        if (this.currentSize == this.maxSize-1){
            this.enlarge();
        }
        if(this.arr[0] <= value){
            this.arr[0] = value+1;
        }
        this.arr[this.currentSize+1] = value;
        this.currentSize++;
        if (this.isLeft(this.currentSize)){
            this.siftup(this.currentSize, this.currentSize/2);
        } else {
            this.siftup(this.currentSize, (this.currentSize-1)/2);
        }
    }

    private void siftup(int child_id, int parent_id){
        if(this.arr[child_id] > this.arr[parent_id]){
            int temp = this.arr[parent_id];
            this.arr[parent_id] = this.arr[child_id];
            this.arr[child_id] = temp; 
            if (this.isLeft(child_id)){
                this.siftup(parent_id, parent_id/2);
            } else {
                this.siftup(parent_id, (parent_id)/2);
            }
        }
    }

    private void siftdown(int id){
        if (id*2+1 <= this.currentSize){
            if (this.leftIsBigger(id)){
                if (this.arr[id] < this.arr[id*2]){
                    int temp = this.arr[id*2];
                    this.arr[id*2] = this.arr[id];
                    this.arr[id] = temp; 
                    this.siftdown(id*2);
                }
            } else {
                if (this.arr[id] < this.arr[id*2+1]){
                    int temp = this.arr[id*2+1];
                    this.arr[id*2+1] = this.arr[id];
                    this.arr[id] = temp; 
                    this.siftdown(id*2+1);
                }
            }
        } else if (id*2 <= this.currentSize) {
            if (this.arr[id] < this.arr[id*2]){
                int temp = this.arr[id*2];
                this.arr[id*2] = this.arr[id];
                this.arr[id] = temp; 
                this.siftdown(id*2);
            }
        } 
    }

    public String toString(){
        String temp = "";
        for (int i = 1; i <= this.currentSize; i++){
            temp+= this.arr[i];
            temp+= " ";
        }
        return temp;
    }

    private void enlarge(){
        int[] temp = this.arr;
        this.arr = new int[temp.length*2];
        this.maxSize = temp.length*2;
        for (int i = 0; i < temp.length; i++){
            this.arr[i] = temp[i];
        }
    }

    private boolean isLeft(int id){
        return (id & 1) == 0; 
    }

    private boolean leftIsBigger(int id){
        return this.arr[id*2] >= this.arr[id*2+1];
    }

}