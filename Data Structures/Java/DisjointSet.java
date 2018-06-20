/* 

Disjoint set data structure using forest of tree data structures - makes it easy to keep id of head

Tree data structure implemented using array to save time and space complexity

One way to solve if you can get from point A to point B in a Maze.

*/


public class DisjointSet{
    public int[] rank;
    public int[] forest;

    public DisjointSet(int size){
        this.rank = new int[size];
        this.forest = new int[size];      
    }

    public void Union(int t1, int t2){
        int t1Parent = this.Find(t1);
        int t2Parent = this.Find(t2);
        if (t1Parent != t2Parent){
            if (this.rank[t1Parent] > this.rank[t2Parent]){
                this.forest[t2Parent] = t1Parent;
            } else {
                this.forest[t1Parent] = t2Parent;
                if (this.rank[t1Parent] == this.rank[t2Parent]){
                    this.rank[t2Parent] += 1;
                }
            }
        } 
    }

    public void MakeSet(int value){
        this.forest[value] = value;
        this.rank[value] = 1;
    }

    public int Find(int value){
        if (this.forest[value] != value){
            this.forest[value] = this.Find(this.forest[value]);
        }
        return this.forest[value];
    } 

    public String toString(){
        String temp = "";
        for (int i = 0; i < this.forest.length; i++){
            temp += "(" + i + ", " + this.forest[i] + ") ";
        }
        return temp;
    }

}

