public class Test {

    public static void main (String[] args){

        PriorityQueue newQ = new PriorityQueue();
        newQ.insert(2);
        newQ.insert(1);
        newQ.insert(5);
        System.out.println(newQ);
        newQ.insert(3);
        System.out.println(newQ);
        System.out.println(newQ.getMax());
        System.out.println(newQ.extractMax());
        System.out.println(newQ);
    }
}