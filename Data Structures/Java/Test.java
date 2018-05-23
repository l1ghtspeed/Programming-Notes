public class Test {

    public static void main (String[] args){

        Stack a = new Stack();
        
        a.push(5);
        a.push(2);
        a.push(3);

        System.out.println(a);
        
        a.pop();

        System.out.println(a);
        
        System.out.println(a.top());
        

    }

}