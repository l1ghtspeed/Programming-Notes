public class BinarySearchTree{

    private Node<E> root = null;
    
    public BinarySearchTree(){
    }

    public void insert(E value){
        if (this.root == null){
            this.root = new Node<E>(value);
        } else {
            this.insert(value, this.root);
        }
    }

    public void insert(E value, Node<E> curr){
        if (value <= curr.value && curr.left == null){
            curr.left = new Node<E>(value);
            curr.left.parent = curr;
        } else if (value <= curr.value){
            this.insert(value, curr.left);
        } else if (value > curr.value && curr.right == null){
            curr.right = new Node<E>(value);
            curr.right.parent = curr;
        } else {
            this.insert(value, curr.right);
        }
    }

    public void delete(){

    }

    public Boolean Find(E value){

    }

    public String display(String notation){
        String temp = "";
        Node<E> curr = this.root;
        if (notation == "in-order"){
            while (curr.left != null){
                curr = curr.left;
            }
            while (curr.parent != null){

            }
            return temp;
        } else if (notation == "pre-order"){
            return temp;
        } else if (notation == "post-order"){
            return temp;
        } else {
            return "Invalid notation format";
        }
        
    }

    private class Node<E> {

        public Node<E> left;
        public Node<E> right; 
        public Node<E> parent; 
        public E value;
    
        public Node(E _value){
            this.parent = null;
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