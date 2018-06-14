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

    public void delete(E value){
        this.delete(value, this.root);
    }

    public void delete(E value, Node<E> curr){
        if (curr.value == value){
            this.findSuccessor();
            return("Value removed, tree altered");
        } else {
            if (value < curr.value && curr.left == null){
                console.log("Value not found");
            } else if (value < curr.value){
                this.Find(value, curr.left);
            } else if (value > curr.value && curr.right == null){
                console.log("Value not found");
            } else {
                this.Find(value, curr.right);
            }
        }
        
    }

    public void findSuccessor(Node<E> curr){
        if (curr.isLeaf()){
            if (curr.isLeaf()){
                if (curr.parent != null && curr.parent.left == curr){
                    curr.parent.left = null; 
                } else if (curr.parent != null){
                    curr.parent.right = null;
                } else {
                    this.root = null;
                }
            } 
        } else if (curr.right!=null and curr.left ==null){
            if (curr = this.root){
                this.root = curr.right;
                this.root.parent = null;
            } else {
                curr.parent.right = curr.right;
                curr.right.parent = curr.parent;
            } 
        } else if (curr.right==null and curr.left!=null){
            if (curr = this.root){
                this.root = curr.left;
                this.root.parent = null;
            } else {
                curr.parent.left = curr.left;
                curr.left.parent = curr.parent;
            }
        } else {
            this.findSuccessor(curr.right);
        }
    }

    public boolean Find(E value){
        return this.Find(value, this.root);
    }

    public boolean Find(E value, Node<E> curr){
        if (curr.value == value){
            return true;
        } else {
            if (value < curr.value && curr.left == null){
                return false;
            } else if (value < curr.value){
                return this.Find(value, curr.left);
            } else if (value > curr.value && curr.right == null){
                return false;
            } else {
                return this.Find(value, curr.right);
            }
        }
    }

    public String toString(){
        String temp = "";
        Node<E> curr = this.root;
        temp = this.inOrderTraversal(curr);
        return temp;
    }

    private String inOrderTraversal(Node<E> curr){
        String temp = "";
        if (curr.left != null){
            this.inOrderTraversal(curr.left);
        } 

        temp += curr.value;
        temp += " ";

        if (curr.right != null){
            this.inOrderTraversal(curr.right);
        } 
        return temp;
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

        public boolean isLeaf(){
            return this.left != null && this.right != null;
        }
    }
}