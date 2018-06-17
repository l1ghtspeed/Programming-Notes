public class Test {

    public static void main (String[] args){

        BinarySearchTree tree = new BinarySearchTree();

        tree.insert(5);
        tree.insert(8);
        tree.insert(2);
        tree.insert(7);
        tree.insert(3);
        tree.insert(10);
        tree.insert(9);
        tree.insert(1);
        tree.insert(6);
        tree.insert(0);

        System.out.println(tree);

        /*

        System.out.println(tree.find(10));
        
        System.out.println(tree.find(36));

        tree.delete(3);

        System.out.println(tree);

        */

    }

}