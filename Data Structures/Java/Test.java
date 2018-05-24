public class Test {

    public static void main (String[] args){

        Queue a = new Queue();
        
        
        a.enqueue(2);
        a.enqueue(3);

        System.out.println(a);
        
        a.dequeue();

        System.out.println(a);
        
        System.out.println(a.peek());
        

    }

}