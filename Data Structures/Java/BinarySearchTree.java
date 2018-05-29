public class BinarySearchTree{


    public BinarySearchTree(){
    }

    public void insert(E value){

    }

    public void delete(){

    }

    public E Find(){

    }

    public void display(){
        
    }

    private class Node<E> {

        public Node<E> left;
        public Node<E> right; 
        public Node<E> parent; 
        public E value;
    
        public Node(Node<E> _left, Node<E> _right, Node<E> _parent, E _value){
    
            this.left = _left;
            this.right = _right;
            this.parent = _parent;
            this.value = _value;
            
        }
    
        public Node(E _value){
            this.parent = null;
            this.left = null;
            this.right = null;
            this.value = _value;
        }

        public Node(Node<E> _parent, E _value){
            this.parent = _parent;
            this.left = null;
            this.right = null;
            this.value = _value;
        }
    
        /**
         * @param left the next to set
         */
        public void setLeft(Node<E> _left) {
            this.left = _left;
        }
    
        public void setRight(Node<E> _right){
            this.right = _right;
        }

        public void setParent(Node<E> _parent){
            this.parent = _parent;
        }
    }


}