public class Queue {

    private int[] queue = new int[4];
    private int head = 0;
    private int tail = -1;

    public Queue(){    
    }

    public void enqueue(int value){
        this.tail++;
        this.queue[this.tail] = value;
    }

    public void dequeue(int value){
        if (this.head != this.tail){
            this.queue[this.head] = 0;
            this.head++;
            if(this.head == ){
                
            }
        }

    }


    public int peek(){
        return this.queue[this.head];
    }

    public Boolean isEmpty(){
        return this.head == this.tail;
    }

    private void increase(){

    }

    public String toString(){

    }

}