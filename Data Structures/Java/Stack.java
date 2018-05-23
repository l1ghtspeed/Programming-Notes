//Simple Array implementation of Stack

public class Stack<E> {

    private E[] stack = new E[8];
    private int counter = 0;

    public Stack(){
    }

    public void push(E value){

        if (counter == stack.length){
            this.increaseStack();
        }

        stack[counter] = value;
        counter++; 

    }
    
    public void pop(){
        stack[counter] = null;
        counter--;
    }

    public E top(){
        return stack[counter];
    }

    public Boolean isEmpty(){
        return counter==0;
    }

    private void increaseStack(){
        E[] oldStack = this.stack;
        this.stack = new E[oldStack.length*2];
        for (int i = 0; i < oldStack.length; i++){
            this.stack[i] = oldStack[i];
        }
    }

}