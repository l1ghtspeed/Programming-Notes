/* 

Disjoint set data structure using forest of tree data structures - makes it easy to keep id of head

One way to solve if you can get from point A to point B in a Maze.

*/


public class DisjointSet{

    private Node<E> root = new Node<E>();

    public DisjointSet(){  
        
    }

    public void union(){
    }

    public void MakeSet(int value){
    }

    public void Find(){
    } 

    private class Node<E> {
        public Node<E> parent; 
        public E value;
    
        public Node(E _value){
            this.parent = null;
            this.value = _value;
        }

        public boolean isLeaf(){
            return this.left != null && this.right != null;
        }
    }

}

