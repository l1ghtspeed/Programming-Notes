public class Test {

    public static void main (String[] args){

        Queue a = new Queue();
        
        
        a.enqueue(1);
        a.enqueue(2);
        a.enqueue(3);
        System.out.println(a);
        a.dequeue();
        a.dequeue();
        a.enqueue(4);
        a.enqueue(5);
        a.enqueue(6);

        System.out.println(a);
        
        System.out.println(a.peek());
        

    }

}