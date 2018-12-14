public class AVLTree {

    Node root;

    // Constructor
    public AVLTree(){
    }
   
    // function to insert new node
    public void insert(float val){
        if (!this.root){
            this.root = new Node(val);
            this.root.parent = null;
        }
    }

    // function to remove a node
    public void remove(){

    }

    // function to find and return a node
    public Node find(){

    }

    // Checks for balance when node is inserted / deleted
    private boolean isBalanced(Node n){
        return true;
    }

    // Custom node class
    private class Node {
        Node leftChild;
        Node rightChild;
        Node parent;
        boolean isLeaf;
        int leftChildCount = 0;
        int rightChildCount = 0;
        float val;
        public Node(float _val) {
            this.val = _val;
        }
    }

}