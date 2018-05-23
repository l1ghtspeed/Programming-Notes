public class Test {

    public static void main (String[] args){

        LinkedList a = new LinkedList();
        
        a.pushFront(5);
        a.pushFront(2);
        a.pushBack(3);

        System.out.println(a);
        
        a.popFront();
        a.pushFront(6);

        System.out.println(a);

        
        a.Erase(4);
        a.popBack();
        System.out.println(a);
        


    }

}