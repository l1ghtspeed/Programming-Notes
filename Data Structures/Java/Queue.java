public class Queue {

    private int[] queue = new int[4];
    private int head = -1;
    private int tail = 0;

    public Queue(){    
    }

    public void enqueue(int value){
        this.head++;
        if (this.head >= this.queue.length && this.tail > 0){
            this.head = 0;
        } else if (this.head >= this.queue.length){
            increase(false);
        } else if (this.head == this.tail){
            increase(true);
        }
        this.queue[this.head] = value;
    }

    public void dequeue(){
        if (this.head != this.tail){
            this.queue[this.tail] = 0;
            this.tail++;
            if (this.tail >= this.queue.length){
                this.tail = 0;
            }    
        }
    }


    public int peek(){
        return this.queue[this.head];
    }

    public boolean isEmpty(){
        return this.head == this.tail;
    }

    private void increase(boolean state){
        int[] curr = this.queue;
        this.queue = new int[curr.length*2];
        if (state){
            for (int i = 0; i < this.head; i++) {
                this.queue[i] = curr[i];
            }
            for (int i = curr.length+this.tail; i < this.queue.length; i++){
                this.queue[i] = curr[i-curr.length];
            }
        } else {
            for (int i = 0; i < curr.length; i++){
                this.queue[i] = curr[i];
            }
        }
    }

    public String toString(){
        String temp = "";
        for (int i = this.tail; i < this.head; i++){
            temp += this.queue[i];
            temp += ", ";
        }
        return temp;
    }

}