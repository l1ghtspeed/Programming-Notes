//Simple Array implementation of Stack

public class Stack {

    private int[] stack = new int[8];
    private int counter = -1;

    public Stack(){
    }

    public void push(int value){

        counter++;

        if (counter == stack.length){
            this.increaseStack();
        }

        stack[counter] = value;
         

    }
    
    public void pop(){
        stack[counter] = 0;
        counter--;
    }

    public int peek(){
        return stack[counter];
    }

    public Boolean isEmpty(){
        return counter==0;
    }

    private void increaseStack(){
        int[] oldStack = this.stack;
        this.stack = new int[oldStack.length*2];
        for (int i = 0; i < oldStack.length; i++){
            this.stack[i] = oldStack[i];
        }
    }

    public String toString(){
        String holder = "";
        for (int i = 0; i < this.counter+1; i++){
            holder+=this.stack[i];
        }
        return holder;
    }

}